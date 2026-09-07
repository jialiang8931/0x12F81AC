# Deliverable code contract

這份契約管的是對外原始碼交付。目的不是削弱產品，而是把產品和內部 Agent 協作控制面分開。接收方必須拿到可執行、可測試、可部署、可由人維護的程式；不會拿到治理方法、業務起始文件或開發歷程。

## 建立時機

只有專案架構、服務邊界、公開腳本與部署目標已定案，且使用者在提案中核准交付流程後，才能建立 root `scripts/build_deliverable_code.sh`。Greenfield 與由 Brownfield 重建的新 Greenfield 都適用。專案仍在 discovery、BDD 或治理迭代時不得預建。

## 公開入口

`scripts/build_deliverable_code.sh` 必須：

- 不接受任何參數；收到參數即失敗，不猜測用途。
- 列入目標專案的 `scripts/manifest.json`，由人或 CI 從 repository root 呼叫。
- 維持 thin script：只做前置檢查、讀取專案名稱與目前 commit 前七碼、啟動固定 Docker 工具環境、傳遞結果及 exit code。ZIP 選檔與驗證邏輯放在容器內可測試的 packaging module。
- 在 `./output/` 產生 `<project>_<current-commit-short-7>.zip`。`<project>` 預設取專案根目錄名稱；若專案已核准其他穩定名稱，必須由 versioned config 提供，不得要求呼叫者輸入。
- 若目標檔已存在，安全失敗，不覆寫既有交付品。
- 不把 `.git/` 帶入容器或 ZIP。Host 只能透過這支 script 做必要的唯讀 commit metadata 查詢。

commit 前七碼只是一個方便人員辨認的檔名片段。不得拿它比較內容、證明正確性、通過測試、升級 gate、綁定 evidence 或判斷開發進度。

## 必須交付

只要專案實際使用，下列內容必須保留：

```text
.gitignore
README.md
docs/api/
docs/user/
docs/operations/
services/
test/
env/<service>/*.example
infra/docker/
infra/terraform/
scripts/check_input.sh
scripts/local_invoke.sh
scripts/start-service.sh
scripts/test_unit.sh
scripts/test_integration.sh
scripts/test_e2e.sh
scripts/deploy_to_<approved-target>.sh
service dependency manifests and lockfiles
approved runtime assets and configuration
```

路徑不存在或不適用時不建立 placeholder。Dockerfile、成對的 ignore file、Terraform、產品測試、環境範例及已核准的執行／部署 script 不能因為「保護 know-how」而被移除。`scripts/build_deliverable_code.sh` 是交付方工具，不放進它產生的 ZIP。

## 必須排除

下列是內部 Agent 協作、治理與業務來源，不得進入 ZIP：

```text
AGENTS.md
SKILL.md
agents/
.agents/
contracts/
tasks/
.codex/
.git/
docs/init.md
```

`docs/init.md` 是使用者的業務理解、BDD 起點與決策脈絡。只排除這一個內部文件，不排除 `docs/api/`、`docs/user/` 或 `docs/operations/`。不得為規避本規則而把受保護內容改名、複製或透過 symlink 帶入交付包。

下列屬一般交付衛生，也應排除：

```text
tmp/
output/
generated/test-evidence/
real .env files
secrets and credentials
private keys and certificates
dependency caches
language build caches
local logs and transient artifacts
```

若產品在執行時需要某個 generated asset，必須在提案中具名、說明來源與 consumer，通過驗證後才列入；不能用整個 `generated/` 的寬鬆例外帶入測試證據或敏感資料。

## 對外 README

交付包內的 `README.md` 是產品交接與操作說明，只允許：

1. **業務邏輯**：產品解決的問題、輸入、業務處理流程、輸出，以及使用者可觀察的錯誤情況。
2. **腳本使用方法**：執行前提、必要順序、每支公開 script 的精確呼叫方式、用途與結果。

README 可以告訴接收方「怎麼操作」，不能解釋內部治理為什麼這樣設計。不得包含或引用：

- 系統架構、目錄設計理由與 dependency direction。
- Agent、subagent、模型、角色、權限、隔離或交接方式。
- BDD／TDD 治理、contracts、change gate、evidence gate 或 promotion 設計。
- 分支、task、commit、release 的內部治理方式。
- Skill 的設計、安裝、觸發或使用方法。
- 交付排除清單、防禦策略，或任何未交付內部文件。
- `AGENTS.md`、`SKILL.md`、`agents/`、`.agents/`、`contracts/`、`tasks/`、`.codex/`、`.git/`、`docs/init.md` 的引用。

## 驗證

Packaging validation 必須同時做正反兩面：

- 展開 ZIP 的 entry list，確認所有 hard exclusions、秘密、中繼產物與 builder 本身都不存在。
- 拒絕 absolute path、`..` traversal、重複 entry，以及會帶入受保護路徑或 repository 外部內容的 symlink。
- 依專案核准的 manifest 確認必要 production source、tests、Docker、Terraform、environment examples、operator scripts 與公開文件存在。
- 在不使用 `.git/`、Agent 設定或內部治理文件的條件下，從交付包執行既有 input、unit、integration 與 E2E 公開入口。未執行的 suite 必須標成 `NOT_EXECUTED`，不能宣稱交付包完整通過。

這個邊界只保護交付方的 Agent 控制面、治理方法、BDD 原始脈絡與 Git／task 歷史。它不宣稱能阻止接收方把已取得的產品原始碼交給其他工具分析；若需要保護產品原始碼本身，交付型態必須另案改成 image、binary 或 hosted service。
