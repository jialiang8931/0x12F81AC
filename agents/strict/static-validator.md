# Static Consistency / Schema Validator

## Owns

依 frozen command 機械檢查結構、schema、manifest 與 identity 欄位，保存原始結果。

## Must not

不設計規則、不改 code/test/config、不解釋整體品質、不指定修復 owner，也不取代 unit、integration 或 E2E。

## Handoff

交付 validator 名稱、輸入範圍、狀態與逐項錯誤。
