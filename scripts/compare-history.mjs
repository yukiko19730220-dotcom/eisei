#!/usr/bin/env node
// Compares a freshly-drafted list of this week's theme records against the
// most recent prior snapshot found in research/history/trend-history.json,
// and prints a JSON diff (new / rising / falling / flat / disappeared).
//
// This exists so Claude does not have to hold the entire history in its own
// context and manually diff it by eye -- the arithmetic is done in code, and
// the model only has to interpret the resulting summary.
//
// Usage:
//   node scripts/compare-history.mjs --current path/to/this-weeks-draft.json [--history research/history/trend-history.json]
//
// --current must be a JSON array of objects shaped like:
//   { theme_id, theme_name_en, rank, opportunity_score, trend_stage, decision, sources_count }
//
// Output (stdout): JSON with { baseline, previous_snapshot_date, stale_comparison, comparisons: [...], disappeared: [...] }

import { existsSync, readFileSync } from "node:fs";
import path from "node:path";

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const ROOT = path.resolve(new URL("..", import.meta.url).pathname);
const currentPath = arg("current");
const historyPath = path.resolve(arg("history", path.join(ROOT, "research", "history", "trend-history.json")));

if (!currentPath || !existsSync(currentPath)) {
  console.error("ERROR: --current <path> is required and must point to an existing JSON file (this week's draft theme list).");
  process.exit(1);
}

const current = JSON.parse(readFileSync(currentPath, "utf8"));
if (!Array.isArray(current)) {
  console.error("ERROR: --current file must contain a JSON array of theme records.");
  process.exit(1);
}

let history = [];
if (existsSync(historyPath)) {
  try {
    history = JSON.parse(readFileSync(historyPath, "utf8"));
    if (!Array.isArray(history)) history = [];
  } catch {
    console.error("WARNING: existing trend-history.json is not valid JSON; treating history as empty. Fix or recreate it manually.");
    history = [];
  }
}

// Find each theme's most recent record strictly before today's draft.
const today = current[0]?.date || new Date().toISOString().slice(0, 10);
const previousByTheme = new Map();
let previousSnapshotDate = null;

for (const row of history) {
  if (!row.date || row.date >= today) continue;
  if (!previousSnapshotDate || row.date > previousSnapshotDate) previousSnapshotDate = row.date;
}

if (previousSnapshotDate) {
  for (const row of history) {
    if (row.date === previousSnapshotDate) {
      previousByTheme.set(row.theme_id, row);
    }
  }
}

const baseline = previousByTheme.size === 0;

let staleComparison = false;
if (previousSnapshotDate) {
  const daysSince = (new Date(today) - new Date(previousSnapshotDate)) / 86400000;
  if (daysSince > 10) staleComparison = true;
}

const RISE_THRESHOLD = 8;
const FALL_THRESHOLD = -8;

const comparisons = current.map((row) => {
  const prev = previousByTheme.get(row.theme_id);
  if (!prev) {
    return {
      theme_id: row.theme_id,
      theme_name_en: row.theme_name_en,
      status: "new_entry",
      previous: null,
      current_opportunity_score: row.opportunity_score ?? null,
      current_trend_stage: row.trend_stage ?? null,
    };
  }
  const prevScore = typeof prev.opportunity_score === "number" ? prev.opportunity_score : null;
  const currScore = typeof row.opportunity_score === "number" ? row.opportunity_score : null;
  const scoreDelta = prevScore !== null && currScore !== null ? currScore - prevScore : null;
  const stageDelta =
    typeof prev.trend_stage === "number" && typeof row.trend_stage === "number"
      ? row.trend_stage - prev.trend_stage
      : null;
  const prevRank = typeof prev.rank === "number" ? prev.rank : null;
  const currRank = typeof row.rank === "number" ? row.rank : null;

  let status = "flat";
  if (scoreDelta !== null) {
    if (scoreDelta >= RISE_THRESHOLD) status = "rising";
    else if (scoreDelta <= FALL_THRESHOLD) status = "falling";
  } else if (stageDelta !== null) {
    if (stageDelta > 0) status = "rising";
    else if (stageDelta < 0) status = "falling";
  }

  const velocity_candidate =
    (prevRank === null || prevRank > 10) && currRank !== null && currRank <= 10
      ? true
      : (row.sources_count ?? 0) - (prev.sources_count ?? 0) >= 2
        ? true
        : stageDelta !== null && stageDelta >= 1 && (prev.trend_stage ?? 0) < 2 && (row.trend_stage ?? 0) >= 2
          ? true
          : false;

  return {
    theme_id: row.theme_id,
    theme_name_en: row.theme_name_en,
    status,
    score_delta: scoreDelta,
    stage_delta: stageDelta,
    previous_rank: prevRank,
    current_rank: currRank,
    velocity_candidate,
    previous: { opportunity_score: prevScore, trend_stage: prev.trend_stage ?? null, decision: prev.decision ?? null },
  };
});

const currentIds = new Set(current.map((r) => r.theme_id));
const disappeared = [...previousByTheme.values()]
  .filter((prev) => !currentIds.has(prev.theme_id))
  .map((prev) => ({ theme_id: prev.theme_id, theme_name_en: prev.theme_name_en, last_seen_date: prev.date, last_opportunity_score: prev.opportunity_score }));

console.log(
  JSON.stringify(
    {
      baseline,
      previous_snapshot_date: previousSnapshotDate,
      stale_comparison: staleComparison,
      comparisons,
      disappeared,
    },
    null,
    2
  )
);
