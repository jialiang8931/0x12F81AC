# Repository layout contract

根目錄直接檔案只允許 `.gitignore`、`AGENTS.md`、`README.md`、`SKILL.md`。其他內容必須進入有責任名稱的目錄。

- `agents/openai.yaml`：skill UI metadata。
- `agents/core/`：一般專案的必要角色藍圖。
- `agents/strict/`：高風險或 brown-field 才啟用的隔離角色。
- `infra/docker/Dockerfile` 與 `infra/docker/Dockerfile.dockerignore`：容器宣告與 build-context 排除規則。
- `infra/terraform/`：部署宣告；只有 deployable 輪廓才建立。
- `env/<service>/`：可提交的環境變數範例。

空目錄不提交。若工具要求新的根目錄直接檔案，必須回到提案並取得例外核准。
