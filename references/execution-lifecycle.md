# Execution lifecycle

核准後仍採最小變更：先建立 contracts 與入口，再建立執行骨架，最後驗證。每一步只寫提案列出的路徑。

可執行專案的公開命令從 root script 開始。script 驗證 argv，啟動固定版本容器，使用 repository-root build context 與 `infra/docker/Dockerfile.dockerignore`，限制 network、user、mount 與 writable output，然後只委派一次。

部署型專案同樣由 script 啟動 Terraform 工具容器。`plan` 與 `apply` 是不同入口；`apply` 必須取得使用者當次明確核准。不可讓開發機安裝的 Python、Node、Go、Terraform 或 provider 成為驗收來源。
