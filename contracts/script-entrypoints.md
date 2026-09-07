# Script entrypoints contract

所有人工操作、CI、agent、IDE 與部署流程只能呼叫 `scripts/manifest.json` 列出的 root scripts。subagent 不得自行拼接 Docker、測試、generator、Terraform 或 service runtime 命令。

每支 script 只做 argv 驗證、Docker 與 mount 編排、一次明確 delegation、exit code 傳遞及 evidence 保存。業務規則留在 production，assertion 留在 tests，Terraform 留在 `infra/terraform/`。

新增入口前要證明它有不同 actor、security policy、lifecycle、I/O contract 或 evidence schema。禁止按客戶或參數複製 wrapper，也禁止萬用 dispatcher 與不透明的 `run-all`。
