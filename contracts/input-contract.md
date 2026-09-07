# Input contract

TDD 階段先固定輸入 cases 與預期結果。Implement 完成後，Test 階段最先驗證輸入格式，再執行 unit/contract。驗證至少涵蓋 schema、必要欄位、型別、允許值、邊界、編碼、檔案存在性與資料分類。

輸入不合格時應在進入業務核心前失敗，並給出不洩漏機密的明確訊息。格式正確只代表可進入 unit gate，不代表業務內容正確。
