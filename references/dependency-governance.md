# Dependency governance

每個新套件要回答五件事：標準函式庫為何不夠、誰擁有它、固定在哪個 service、如何鎖版、如何退出。

Python、Node、Go、Rust 依各自 manifest 與 lockfile 管理。不要混用兩種 Node lockfile。不要在 runtime 安裝，不要從未固定的 Git branch 或任意 URL 取程式碼。Node lifecycle scripts 預設關閉，只有核准 allowlist 才開。

lockfile 應提交。套件管理器自己的完整性欄位可以存在，但不手工重算，也不用它代表開發進度。
