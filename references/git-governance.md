# Git governance

首次設定由 `main` 開 `dev`。初始化 tasks 各自從 `dev` 開 `taskN/<english-purpose>`，通過規定的 gate 後合回 `dev`。

初始化完成後，不替使用者猜 branch type。先取得用途前綴與一句目標，再建立 `type/english-kebab-case`。例如主視覺配色是 `styles/adjust-main-visual-colors`；設定參數是 `chore/update-configuration-parameters`。

提交訊息採 `<type>(<scope>): <中文任務說明>`。Git write 是 Docker 例外，但只能走 manifest 核准的 root script。任何 commit、merge、tag、push、branch delete 或 conflict resolution 都需要符合當前授權，不連帶推定。
