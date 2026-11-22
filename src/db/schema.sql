-- GTA VI Vietnamese Translation System — Phase 2 schema
-- Source: TDD v1.3, Chapter 4.4–4.5
-- DEVIATION from TDD text (documented, data-driven):
--   TDD prints `id INTEGER PRIMARY KEY` for source_strings, but the real
--   `id` in all_rows.tsv is TEXT, e.g. 'C0000_B381007C' / 'S0849_...'.
--   Using INTEGER would lose the key. So id is TEXT PRIMARY KEY here,
--   and every FK referencing it is TEXT as well. No other change.
--   `table` / `group` are SQL keywords, so columns are table_name / group_name.
--   Added db_meta (mentioned in TDD 4.6, no DDL given there).

PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS db_meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS source_strings (
  id TEXT PRIMARY KEY,
  pack TEXT,
  table_name TEXT,
  idx INTEGER,
  hash TEXT,
  category TEXT,
  group_name TEXT,
  keep TEXT,
  ukey TEXT,
  en TEXT NOT NULL,
  en_display TEXT,
  markers TEXT,
  priority_tier TEXT,
  is_template INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS translations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_id TEXT NOT NULL REFERENCES source_strings(id),
  vi TEXT NOT NULL,
  version INTEGER NOT NULL,
  status TEXT NOT NULL,
  origin TEXT NOT NULL,
  context_key TEXT,
  created_at TEXT,
  supersedes INTEGER,
  UNIQUE(source_id, version, context_key)
);

CREATE TABLE IF NOT EXISTS match_index (
  source_id TEXT PRIMARY KEY REFERENCES source_strings(id),
  en_norm TEXT NOT NULL,
  en_skel TEXT,
  len_bucket INTEGER,
  first_token TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS match_fts
  USING fts5(source_id UNINDEXED, en_norm);
-- Standalone FTS5 (NOT external-content): the TDD's external-content form
-- (content='match_index') corrupted on bulk DELETE/rebuild in this
-- environment (sqlite3.DatabaseError: database disk image is malformed).
-- Standalone FTS5 is populated by the importer from match_index and is
-- fully rebuildable from it, so no data is lost; matching queries join
-- on source_id. Rebuild = DELETE + INSERT ... SELECT from match_index.

CREATE TABLE IF NOT EXISTS string_templates (
  source_id TEXT PRIMARY KEY REFERENCES source_strings(id),
  pattern TEXT NOT NULL,
  slots TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ocr_cache (
  ocr_norm_hash TEXT PRIMARY KEY,
  ocr_text TEXT,
  source_id TEXT,
  confidence REAL,
  match_tier TEXT,
  context_key TEXT,
  hit_count INTEGER DEFAULT 1,
  last_seen TEXT
);

CREATE TABLE IF NOT EXISTS glossary (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  en_term TEXT NOT NULL,
  vi_term TEXT NOT NULL,
  kind TEXT,
  do_not_translate INTEGER DEFAULT 0,
  note TEXT,
  UNIQUE(en_term, kind)
);

CREATE TABLE IF NOT EXISTS unmatched_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ocr_text TEXT,
  ocr_norm TEXT,
  screen_type TEXT,
  best_candidate_id TEXT,
  best_score REAL,
  reason TEXT,
  crop_path TEXT,
  seen_count INTEGER DEFAULT 1,
  status TEXT DEFAULT 'new',
  created_at TEXT,
  last_seen TEXT
);

CREATE TABLE IF NOT EXISTS screen_contexts (
  context_key TEXT PRIMARY KEY,
  category_hint TEXT,
  group_hint TEXT,
  boost REAL
);

CREATE INDEX IF NOT EXISTS idx_src_cat ON source_strings(category, group_name);
CREATE INDEX IF NOT EXISTS idx_src_hash ON source_strings(hash);
CREATE INDEX IF NOT EXISTS idx_src_ukey ON source_strings(ukey);
CREATE INDEX IF NOT EXISTS idx_src_tier ON source_strings(priority_tier);
CREATE INDEX IF NOT EXISTS idx_tr_cur ON translations(source_id, status);
CREATE INDEX IF NOT EXISTS idx_mi_bucket ON match_index(len_bucket, first_token);
CREATE INDEX IF NOT EXISTS idx_mi_norm ON match_index(en_norm);
