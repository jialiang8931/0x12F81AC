# Role design

核心角色是 Architect、Test Designer、Implementer、Reviewer、Test Runner。只有風險需要時，才加入 Legacy Explorer、Test-harness Implementer、Orchestrator/Binder 與 Static Validator。

角色切分依 decision ownership，不依檔案數。Architect 決定邊界；Test Designer 在實作前固定行為；Implementer 只做核准範圍；Reviewer 獨立判讀 diff；Runner 只執行既定命令。

沒有被授權派發 subagent 時，由當前 agent 在相同邊界內工作，不模擬多人簽核。業務 owner 永遠是使用者或具名 domain owner，不建立 AI business-owner 角色。
