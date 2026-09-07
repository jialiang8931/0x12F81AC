# Validation method

先確認 BDD 與 `docs/init.md`，再建立 Docker gate。TDD frozen、Implement 完成後，依公開 scripts 執行 Test（input/schema → unit/contract）、Integration、E2E；通過才進 Release。每個結果只保存 stage、suite、case、task、branch、command、時間、狀態與必要訊息。

不要計算或比較 SHA、checksum、commit identity、archive hash 或 image digest。檔案等價要比較解析後語意；流程正確要比較狀態與可觀察行為；release 身分使用人可讀的 release 名稱與 immutable tag。
