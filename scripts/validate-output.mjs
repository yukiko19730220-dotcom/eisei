#!/usr/bin/env node
// Final self-check for a weekly research run. Exits 0 only if the expected
// deliverables for the given date all exist and look structurally sound.
// Run this yourself before finishing, AND it is run again as an independent
// CI step after the Claude step, so a run that silently produced nothing
// still shows a clear red failure in the GitHub Actions UI.
//
// Usage: node scripts/validate-output.mjs --date 2026-09-01

import { existsSync, readFileSync } from "node:fs";
import path from "node:path";

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const ROOT = path.resolve(new URL("..", import.meta.url).pathname);
const date = arg("date", new Date().toISOString().slice(0, 10));
const VALID_DECISIONS = new Set(["BUILD_NOW", "TEST", "WATCH", "AVOID"]);

const failures = [];
const warnings = [];

const reportPath = path.join(ROOT, "research", "reports", `${date}-weekly-report.md`);
let reportText = "";
if (!existsSync(reportPath)) {
  failures.push(`レポートファイルが存在しません: research/reports/${date}-weekly-report.md`);
} else {
  reportText = readFileSync(reportPath, "utf8");
  if (reportText.trim().length < 500) {
    failures.push(`レポートファイルの内容が短すぎます(${reportText.trim().length}文字): research/reports/${date}-weekly-report.md`);
  }
}

const incomplete = /RESEARCH\s+INCOMPLETE/i.test(reportText);

const logPath = path.join(ROOT, "logs", "run-log.md");
if (!existsSync(logPath)) {
  failures.push("logs/run-log.md が存在しません");
} else {
  const logText = readFileSync(logPath, "utf8");
  if (!logText.includes(date)) {
    failures.push(`logs/run-log.md に ${date} の実行記録が見つかりません`);
  }
}

if (incomplete) {
  warnings.push("レポートが RESEARCH INCOMPLETE を宣言しているため、themes.json / history の完全性チェックはスキップしました。");
} else {
  const themesPath = path.join(ROOT, "research", "themes", "themes.json");
  if (!existsSync(themesPath)) {
    failures.push("research/themes/themes.json が存在しません");
  } else {
    try {
      const themes = JSON.parse(readFileSync(themesPath, "utf8"));
      const list = Array.isArray(themes) ? themes : themes.themes;
      if (!Array.isArray(list) || list.length === 0) {
        failures.push("themes.json にテーマが1件も含まれていません");
      } else {
        list.forEach((t, i) => {
          if (!t.theme_id) failures.push(`themes.json[${i}] に theme_id がありません`);
          if (t.decision && !VALID_DECISIONS.has(t.decision)) {
            failures.push(`themes.json[${i}] (${t.theme_id}) の decision が不正な値です: ${t.decision} (BUILD_NOW/TEST/WATCH/AVOIDのいずれかにすること)`);
          }
        });
      }
    } catch (e) {
      failures.push(`themes.json が不正なJSONです: ${e.message}`);
    }
  }

  const csvPath = path.join(ROOT, "research", "history", "trend-history.csv");
  if (!existsSync(csvPath)) {
    failures.push("research/history/trend-history.csv が存在しません");
  } else {
    const csvText = readFileSync(csvPath, "utf8");
    if (!csvText.split("\n").some((line) => line.startsWith(date))) {
      failures.push(`trend-history.csv に ${date} の行が見つかりません`);
    }
  }

  const jsonHistPath = path.join(ROOT, "research", "history", "trend-history.json");
  if (!existsSync(jsonHistPath)) {
    failures.push("research/history/trend-history.json が存在しません");
  } else {
    try {
      const rows = JSON.parse(readFileSync(jsonHistPath, "utf8"));
      if (!Array.isArray(rows) || !rows.some((r) => r.date === date)) {
        failures.push(`trend-history.json に ${date} のレコードが見つかりません`);
      }
    } catch (e) {
      failures.push(`trend-history.json が不正なJSONです: ${e.message}`);
    }
  }
}

console.log(`=== validate-output: ${date} ===`);
console.log(incomplete ? "モード: RESEARCH INCOMPLETE (簡易チェックのみ)" : "モード: 通常チェック");
if (warnings.length) {
  console.log("\n--- 警告 ---");
  warnings.forEach((w) => console.log(`  ⚠ ${w}`));
}
if (failures.length) {
  console.log("\n--- 失敗 ---");
  failures.forEach((f) => console.log(`  ✗ ${f}`));
  console.log(`\n${failures.length}件の必須チェックに失敗しました。`);
  process.exit(1);
} else {
  console.log("\n✓ すべての必須チェックに合格しました。");
  process.exit(0);
}
