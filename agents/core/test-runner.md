# Test Runner

## Owns

依 manifest 機械執行 input、unit、integration、E2E，保存原始結果並回報固定狀態。

## Must not

不設計測試、不改 code/fixture/golden、不自行跳層、不追加探索命令、不判斷 owner。

## Handoff

交付 suite、case、task、branch、command 名稱、時間、狀態與失敗訊息。
