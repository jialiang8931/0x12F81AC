# Gitignore policy

核心忽略類別是 OS/editor、log/runtime、tmp/generated/output、coverage、真實 env、credentials、Terraform runtime、語言 cache 與 build output。

只有目標專案實際使用的語言區塊才保留。永遠不要忽略 lockfile。Terraform 追蹤 `.tf`、`.terraform.lock.hcl` 與安全的 `*.tfvars.example`；忽略 `.terraform/`、state、plan、crash、override、CLI config 與真實 tfvars。

`vendor/` 預設既不忽略也不提交。若離線、授權或供應鏈政策要求 vendoring，必須在提案中獨立決定 owner、更新方式與驗證。
