---
name: project-arch-init
description: Assess and initialize software-project architecture and governance through an approval-first, Sepia-dependent workflow. Use when a user asks to start or retrofit a project with AGENTS.md, contracts, role policies, task gates, repository layout, testing or evidence rules, Git workflow, Docker lifecycle, Terraform deployment, or subagent management. Require an existing user-authored docs/init.md, present and iterate on a proposal before writing, and never use for ordinary feature implementation.
---

# Project Architecture Init

建立治理之前，先承認一件事：業務不是由 skill 發明的。

## 不可協商的前提

1. 先載入目前環境中正式可用的 `sepia` skill，完整遵守它的指示。若 Sepia 不存在或無法讀取，停止本 skill；不得自行模仿它。
2. 後續提案、文件與對使用者的回覆預設都經 Sepia 處理。只有使用者在當次要求明確排除 Sepia 時，才可停用書寫風格；Sepia 的缺席仍不得被視為可以執行本 skill。
3. 目標 repository 必須已存在由使用者撰寫的 `./docs/init.md`。本 skill 不得建立、代寫、補完或猜測該檔案。
4. `docs/init.md` 是 BDD 與業務理解的起點。它不必完美，但必須足以說明問題、使用者、範圍、規則、情境、輸入輸出、驗收、風險與未決事項。
5. 在提案獲得明確核准前，只能唯讀盤點與討論；不得新增、修改、刪除或重新命名專案檔案，不得建立分支、安裝套件或啟動生成器。

## 執行流程

### 0. 宣告依賴與邊界

告知使用者正在使用本 skill 與 Sepia。列出目標 repository、唯讀範圍、目前禁止的寫入，以及預期的決策點。

### 1. 驗證 business-init gate

依 [business-init-gate.md](references/business-init-gate.md) 檢查 `docs/init.md`。若不存在、由 AI 代寫、仍有關鍵佔位符、未標示 `READY_FOR_GOVERNANCE`，或沒有可驗證的行為情境，停止。只回報缺口與使用者應自行補充的問題，不提供代寫內容。

### 2. 唯讀盤點

依 [assessment.md](references/assessment.md) 讀取 repository 的技術現況、既有規則、資料風險與可部署性。既有檔案是證據，不會自動成為規範。保留使用者未提交的工作。

### 3. 選擇最小治理輪廓

依 [governance-profiles.md](references/governance-profiles.md) 選擇 `docs-only`、`service` 或 `deployable`。不為尚未存在的需求預建框架、共用套件、第二個 service 或角色。

### 4. 只提出提案，不落盤

依 [governance-schema.md](references/governance-schema.md) 向使用者交付一份可修改的治理提案，至少包含：

- 從 `docs/init.md` 讀到的業務邊界與未決事項。
- 建議保留、新增、刪減的規範及理由。
- 目錄樹與每個檔案的責任。
- Docker、scripts-only、依賴、環境檔、Git 與部署規則。
- input → unit → integration → E2E 的升級條件。
- subagent 角色、權限、交接與何時根本不該派發。
- 預計寫入路徑、禁止路徑、驗證命令與回復方式。

不得把「建議」寫成已定案。使用者可以反覆修改提案；每次迭代都要顯示變更與仍未決事項。

### 5. 等待明確核准

只有使用者清楚表示提案可以實作，才進入下一步。模糊肯定、一般討論、要求解釋或只核准其中一段，都不算整體核准。核准後若 scope 發生實質變化，回到提案階段。

### 6. 依核准內容建立治理

遵守 [execution-lifecycle.md](references/execution-lifecycle.md)：先建立最小必要檔案，再用 root `scripts/manifest.json` 公開允許的命令。可執行專案以 Docker 為第一道防線；部署型專案必須以 Docker 建置與執行 Terraform。

根目錄直接檔案只允許：

```text
.gitignore
AGENTS.md
README.md
SKILL.md
```

`agents/openai.yaml` 是巢狀 metadata，不是根目錄直接檔案。Docker 宣告放在 `infra/docker/`，Terraform 放在 `infra/terraform/`，環境範例放在 `env/<service>/`。

### 7. 依序驗證

驗證順序不可顛倒：

```text
input format / schema → unit → integration → end-to-end
```

前一層不是 `PASSED`，下一層就是 `NOT_EXECUTED`。不得以 E2E 反推輸入、單元或整合契約。進度以 branch、task、suite 狀態、diff、測試結果與 release tag 表達；嚴禁自訂 SHA、commit SHA、檔案 checksum、image digest 或 hash 比對作為治理、綁定或升級 gate。套件管理器在 lockfile 中自動維護的完整性欄位可以保留，但不得手工計算或作為專案進度身分。

## 核心規則

- Docker：見 [docker-lifecycle.md](references/execution-lifecycle.md)。專案程式、測試、生成器與 Terraform 都在固定版本的容器中執行。
- Scripts-only：所有人與 subagent 只能呼叫 `scripts/manifest.json` 允許的 root scripts；script 只驗證參數、編排容器、管理精確 mount、傳遞 exit code 與保存證據。
- 程式設計：功能與正確性相同時，優先純函數、不可變資料、明確輸入輸出與最少可讀程式碼。side effect 留在 adapter 或 imperative shell。
- 依賴：標準函式庫優先；非必要不安裝。必要依賴由各 service 的 manifest 與 lockfile 管理，只在 Docker 內安裝。見 [dependency-governance.md](references/dependency-governance.md)。
- Git：`main` 建立 `dev`；任何工作從 `dev` 切分支，完成驗證後合併回 `dev`。見 [git-governance.md](references/git-governance.md)。
- 部署：只從乾淨、已通過 gate 的 `dev` 狀態部署。Docker image 與 Terraform plan 使用 release 名稱，不使用 SHA。見 [deployment-governance.md](references/deployment-governance.md)。
- Agents：`agents/` 保存角色藍圖，不授權自動派發。使用者或上層規則未允許 subagent 時，不得因藍圖存在就派發。見 [role-design.md](references/role-design.md)。

## 完成條件

只有下列條件同時成立，才能說初始化完成：核准的檔案已建立；未碰禁止路徑；公開入口與 manifest 一致；依賴與機密規則可驗證；測試依序通過；未用 SHA 類比對替代語意驗證；文件以臺灣繁體中文寫成並經 Sepia 處理；使用者取得實際 diff 與仍待決事項。
