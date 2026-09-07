from __future__ import annotations

from pathlib import Path

from scripts.validate_project_arch import required_paths


INIT_TEXT = """---
business_owner: domain-team
status: READY_FOR_GOVERNANCE
---
# 業務問題
讓使用者安全完成工作。
# 使用者與利害關係人
操作人員。
# 範圍與非範圍
只處理核准輸入。
# 領域詞彙
工作：一次有界請求。
# 業務規則
輸入不合法就停止。
# 行為情境
Given 合法輸入
When 使用者執行
Then 系統產生結果
# 輸入與輸出
文字輸入，狀態輸出。
# 驗收條件
結果可讀且可驗證。
# 風險
機密外洩。
# 未決事項
無。
"""


def build_project(root: Path, profile: str, init_text: str = INIT_TEXT) -> None:
    for relative in required_paths(profile):
        path = root / relative
        if relative == "infra/terraform":
            path.mkdir(parents=True, exist_ok=True)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(init_text if relative == "docs/init.md" else "# Contract\n", encoding="utf-8")
    if profile in {"service", "deployable"}:
        (root / "scripts/manifest.json").write_text(
            '{"public_entrypoints": []}\n', encoding="utf-8"
        )
