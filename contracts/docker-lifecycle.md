# Docker lifecycle contract

Docker 是可執行專案的第一道防線，涵蓋開發、測試、生成、建置、部署工具與 production runtime。

- Docker build context 固定為 repository root，Dockerfile 位於 `infra/docker/Dockerfile`。
- Docker 使用 `infra/docker/Dockerfile.dockerignore` 作為明確 context exclude file；root 不放 `.dockerignore`。
- 執行預設 `--network none`、`--read-only`、非 root user、精確唯讀 mount 與最小 writable output。
- 不掛載 home、SSH、cloud credentials、Docker socket、其他專案或寬泛 host path。
- build 階段才能取得固定版本依賴；runtime 不下載程式碼。
- Git metadata 留在 host。需要 Git 寫入時只能走核准的 root script，且必須清楚標示為 Docker 例外。
