# Dependency management contract

標準函式庫優先。安裝套件前要證明必要性，並檢查 owner、維護狀態、授權、已知風險與替代方案。

依賴由 service 自己擁有：Python 使用 `requirements.txt` 與 `requirements.lock`；Node 使用 `package.json` 與一種 lockfile；Go 使用 `go.mod`、`go.sum`；Rust 使用 `Cargo.toml`、`Cargo.lock`。除非核准真正的 shared workspace，根目錄不放依賴 manifest。

只在 Docker build 安裝固定版本。禁止 floating version、`latest`、任意 Git URL、未知 archive、`curl | sh` 與 runtime download。lockfile 必須提交；其中套件管理器自動產生的完整性欄位視為不透明資料，不手工計算或拿來追專案進度。
