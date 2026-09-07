# Testing contract

固定升級順序：

```text
input format / schema → unit → integration → end-to-end
```

每層狀態只有 `PASSED`、`FAILED`、`NOT_EXECUTED`、`NOT_APPLICABLE`。前一層沒有通過，下一層不能執行。不得從 E2E 開始，也不得用一個大流程掩蓋 unit 或 integration 的缺口。

- Input：證明資料可以安全進入系統。
- Unit：證明純核心與局部規則。
- Integration：證明真實邊界與元件協作。
- E2E：證明已核准的使用者旅程，不重新發明底層 assertions。

驗證應比較語意、狀態與可觀察行為。嚴禁以 SHA、checksum、commit identity 或 image digest 作為等價、進度、證據綁定或 suite 升級條件。測試結果記錄 suite、case、branch、task、時間、命令名稱與結果即可。
