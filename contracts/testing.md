# Testing contract

測試是完整開發生命週期的一段。前置順序先由 `contracts/development-lifecycle.md` 固定為 BDD、Docker、TDD、Implement；implementation 完成後，測試順序是：

```text
Test(input/schema → unit/contract) → Integration → E2E
```

每層狀態只有 `PASSED`、`FAILED`、`NOT_EXECUTED`、`NOT_APPLICABLE`。前一層沒有通過，下一層不能執行。不得從 E2E 開始，也不得用一個大流程掩蓋 input、unit 或 integration 的缺口。

TDD 是 implementation 前的設計與 red gate；Test 是 implementation 後的執行 gate。兩者不能合併。Brown-field characterization 若記錄的是既有行為，可以沒有人工製造的 red state，但 cases 與 oracle 仍須先 frozen。

- Input：在 Test 階段最先執行，證明資料可以安全進入系統。
- Unit/contract：證明純核心、局部規則與協定。
- Integration：證明真實邊界與元件協作。
- E2E：證明已核准的使用者旅程，不重新發明底層 assertions。

驗證應比較語意、狀態與可觀察行為。嚴禁以 SHA、checksum、commit identity 或 image digest 作為等價、進度、證據綁定或 suite 升級條件。測試結果記錄 suite、case、branch、task、時間、命令名稱與結果即可。
