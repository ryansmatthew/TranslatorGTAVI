"""Phase 2 gate benchmark (TDD ch.14): exact/normalized query p95 on 10k sample.
Opens the DB read-only. Sample queries are drawn from the TSV file itself
(sequential read), NOT via ORDER BY RANDOM() — a full scan + sort of
579k rows is cold-disk slow in this VM and is not what the gate measures.
The gate measures indexed lookup latency, which is what runtime does.

Usage: python3 tools/bench_phase2.py [db_path] [tsv_path]
Writes tools/bench_phase2_report.json as well as printing it.
"""
import collections
import csv
import json
import os
import random
import sqlite3
import statistics
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.common.normalize import normalize  # noqa: E402

DB = sys.argv[1] if len(sys.argv) > 1 else "data/gta6.db"
TSV = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/workspace/gta6-text-en/all_rows.tsv")

# --- sample 10,000 non-empty en_norm values from the TSV (reservoir) ---
random.seed(42)
sample = []
with open(TSV, encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh, delimiter="\t")
    for i, r in enumerate(reader):
        from src.common.markers import split_markers
        display, _, _ = split_markers(r["en"] or "")
        q = normalize(display)
        if not q:
            continue
        if len(sample) < 10000:
            sample.append(q)
        elif random.random() < 10000 / (i + 1):
            sample[random.randrange(10000)] = q
print(f"sampled {len(sample)} queries from TSV", flush=True)

con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
print("fts rows:", con.execute("SELECT COUNT(*) FROM match_fts").fetchone()[0], flush=True)
print("source rows:", con.execute("SELECT COUNT(*) FROM source_strings").fetchone()[0] if False else "(skipped: full scan, see import_report.json)", flush=True)

for raw in ["Hey! Eyes open!", "VICE CITY", "Stop your vehicle!"]:
    q = normalize(raw)
    rows = con.execute(
        "SELECT source_id,en FROM match_index JOIN source_strings ON source_id=id "
        "WHERE en_norm=? LIMIT 2", (q,)).fetchall()
    print(repr(raw), "->", rows, flush=True)

t, hits = [], 0
for q in sample:
    s = time.perf_counter()
    r = con.execute("SELECT source_id FROM match_index WHERE en_norm=? LIMIT 1", (q,)).fetchone()
    t.append((time.perf_counter() - s) * 1000)
    hits += bool(r)
t.sort()
report = {
    "n": len(t), "hit_rate": round(hits / len(t), 4),
    "exact_ms": {"p50": round(t[len(t)//2], 3), "p95": round(t[int(len(t)*0.95)], 3),
                 "p99": round(t[int(len(t)*0.99)], 3), "max": round(t[-1], 3),
                 "mean": round(statistics.mean(t), 3)},
}
print("exact/normalized 10k:", json.dumps(report, ensure_ascii=False), flush=True)

def fts_q(q):
    toks = [w for w in q.split() if w.isalnum()]
    return " ".join(f'"{w}"' for w in toks[:3])

t, ok, n = [], 0, 0
for q in sample[:2000]:
    fq = fts_q(q)
    if not fq:
        continue
    n += 1
    s = time.perf_counter()
    r = con.execute("SELECT source_id FROM match_fts WHERE en_norm MATCH ? LIMIT 5", (fq,)).fetchall()
    t.append((time.perf_counter() - s) * 1000)
    ok += bool(r)
t.sort()
report["fts5_2k"] = {"n": n, "hit_rate": round(ok / len(t), 4),
                     "p50_ms": round(t[len(t)//2], 3), "p95_ms": round(t[int(len(t)*0.95)], 3),
                     "max_ms": round(t[-1], 3)}
print("FTS5 2k:", json.dumps(report["fts5_2k"], ensure_ascii=False), flush=True)

out = os.path.join(os.path.dirname(__file__), "bench_phase2_report.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print("report:", out, flush=True)
