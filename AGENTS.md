# Repository working rules

本 repository 維護 `project-arch-init` skill。它保存通用治理方法，不保存任何目標專案的業務事實。

## 優先序

1. 使用者當前明確要求。
2. 本檔案。
3. `contracts/` 的可驗證規則。
4. `agents/` 的角色邊界。
5. `tasks/` 的核准工作範圍。

低順位規則不能放寬高順位規則。發現衝突時先停止修改並回報。

## 工作方式

- 每次處理本 skill，都必須載入正式 Sepia skill；除非使用者當次明確排除，回答與文件一律採 Sepia。
- 修改前先列 owner、objective、writable paths、forbidden paths、verification 與 rollback。
- 根目錄直接檔案只允許 `.gitignore`、`AGENTS.md`、`README.md`、`SKILL.md`。
- 公開程式入口只存在於 `scripts/manifest.json`。不得直接叫用內部 Python 模組代替公開 script。
- 執行驗證的順序固定為 input、unit、integration、E2E。前一層失敗或未執行，下一層不得執行。
- 不用 SHA、commit identity、checksum 或 image digest 作為進度、證據或升級 gate。
- 標準函式庫優先。新增依賴前必須說明不可替代性、owner、固定版本、lockfile 與供應鏈風險。
- 功能與正確性相同時，優先純函數、不可變資料、明確輸入輸出與最少可讀程式碼。
- 不自動 commit、push、部署、套用 Terraform、刪除分支或解決衝突。
- 發佈版本的 repository 根目錄必須可由 GitHub skill installer 以 path `.`、name `project-arch-init`、ref `main` 安裝；不得要求複製單一檔案或另找隱藏子目錄。

## Skill 邊界

`project-arch-init` 不得替目標專案建立或代寫 `docs/init.md`。缺少使用者完成並標示 `READY_FOR_GOVERNANCE` 的業務文件時，只能指出缺口。提案未獲核准前，不得落盤。
