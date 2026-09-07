# Execution lifecycle

核准後沿著固定生命週期工作：BDD → Docker → TDD → Implement → Test → Integration → E2E → Release。每一步只寫提案列出的路徑。

BDD 先由使用者把業務行為說清楚。Docker 隨後建立隔離環境。TDD 在 production code 之前固定 cases、oracle 與 input contract。Implement 只做最小變更；Test 階段先跑 input/schema，再跑 unit/contract。通過後才進 Integration、E2E，最後才有 Release。

可執行專案的公開命令從 root script 開始。script 驗證 argv，啟動固定版本容器，使用 repository-root build context 與 `infra/docker/Dockerfile.dockerignore`，限制 network、user、mount 與 writable output，然後只委派一次。

部署型專案在 Release 階段由 script 啟動 Terraform 工具容器。`plan` 與 `apply` 是不同入口；`apply` 必須取得使用者當次明確核准。不可讓開發機安裝的 Python、Node、Go、Terraform 或 provider 成為驗收來源。
