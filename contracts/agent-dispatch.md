# Agent dispatch contract

`agents/` 是角色與權限藍圖，不是自動派發清單。只有使用者、平台規則或已核准 task 明確允許 subagent 時，才能派發。

每次派發只給一個 bounded outcome、唯讀 providers、明確 writable paths、forbidden paths、驗證與交接格式。角色不因同一模型而合併；需要獨立性時，必須是不同 task、不同 agent、不同產物。

所有 subagent 只能使用 `scripts/manifest.json` 公開入口。不得自行安裝套件、直接執行內部模組、擴大 mount、跳過測試層級或追加未核准的探索工作。
