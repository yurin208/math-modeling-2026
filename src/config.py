"""全局配置：路径与随机种子集中在此，对应论文「模型假设」里的可复现性说明。"""

from pathlib import Path

# 随机种子：所有涉及随机的脚本统一从这里取，保证队友机器上结果一致
SEED = 42

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"


def ensure_dirs() -> None:
    """确保输出目录存在（results/ 与 figures/ 不进版本库，克隆后是空的）。"""
    for d in (RESULTS, FIGURES):
        d.mkdir(parents=True, exist_ok=True)
