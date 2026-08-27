#!/usr/bin/env node
// Ensures the research/ and logs/ directory structure exists, then prints a
// compact JSON context dump (today's date, previous snapshot info, recent
// reports) so the weekly-research prompt can orient itself without spending
// extra tool calls on discovery.
//
// Usage: node scripts/prepare-research.mjs

import { existsSync, mkdirSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";

const ROOT = path.resolve(new URL("..", import.meta.url).pathname);
const configPath = path.join(ROOT, "config", "research-config.json");
const config = JSON.parse(readFileSync(configPath, "utf8"));

const dirs = [
  ...config.markets.map((m) => m.raw_dir),
  "research/themes",
  "research/reports",
  "research/history",
  "logs",
];

const created = [];
for (const rel of dirs) {
  const abs = path.join(ROOT, rel);
  if (!existsSync(abs)) {
    mkdirSync(abs, { recursive: true });
    created.push(rel);
  }
}

function todayUTC() {
  return new Date().toISOString().slice(0, 10);
}

function nowJST() {
  return new Intl.DateTimeFormat("sv-SE", {
    timeZone: "Asia/Tokyo",
    dateStyle: "short",
    timeStyle: "short",
  }).format(new Date());
}

const reportsDir = path.join(ROOT, "research", "reports");
const recentReports = existsSync(reportsDir)
  ? readdirSync(reportsDir)
      .filter((f) => f.endsWith(".md"))
      .sort()
      .slice(-5)
  : [];

const historyJsonPath = path.join(ROOT, "research", "history", "trend-history.json");
let historyRecordCount = 0;
let lastSnapshotDate = null;
if (existsSync(historyJsonPath)) {
  try {
    const rows = JSON.parse(readFileSync(historyJsonPath, "utf8"));
    if (Array.isArray(rows)) {
      historyRecordCount = rows.length;
      const dates = rows.map((r) => r.date).filter(Boolean).sort();
      lastSnapshotDate = dates.length ? dates[dates.length - 1] : null;
    }
  } catch {
    // leave defaults; validate-output.mjs will flag malformed JSON separately
  }
}

const themesPath = path.join(ROOT, "research", "themes", "themes.json");
const themesExists = existsSync(themesPath);

console.log(
  JSON.stringify(
    {
      today_utc: todayUTC(),
      now_jst: nowJST(),
      directories_created_this_run: created,
      recent_report_files: recentReports,
      themes_json_exists: themesExists,
      history_json_record_count: historyRecordCount,
      history_json_last_snapshot_date: lastSnapshotDate,
      is_first_ever_run: historyRecordCount === 0,
    },
    null,
    2
  )
);
