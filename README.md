# 数学建模协作仓库

数学建模竞赛（新秀杯 / CUMCM）协作用仓库：代码、论文、结果都放这里，队友通过 GitHub Desktop 同步。

## 目录约定

```
data/      原始数据（只读，禁止修改；单个文件 > 50MB 走网盘，不要提交）
src/       建模与求解代码
figures/   输出图片（png 300dpi + pdf 各一份）
paper/     论文 LaTeX 源码（一人一个 .tex 文件，别共用 main.tex）
results/   中间结果与日志（csv/json 摘要可提交，.npy/.pkl 不提交）
tools/     辅助脚本
```

新文件按此放，不要在根目录乱建。

## 环境

Python 3.13。首次使用：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- 运行一律在仓库根目录，路径用相对路径。
- 随机种子固定 42，见 `src/config.py`。

## 协作规矩（先看这条）

1. **一人一个文件，不要两个人同时改同一个文件。** 不同文件的改动 Git 会自动合并；同一文件同一处被两人改，必然冲突。
2. **动手前 Pull，做完立刻 Push。** 顺序：Pull origin → 改 → Commit → Push origin。
3. **提交信息写清楚做了什么**，格式 `范围: 动作`：
   - `src: 加入灰色预测 GM(1,1)`
   - `paper: 补写 4.2 灵敏度分析`
   - `data: 修正 2020 年缺失值`
4. **不要提交**：`.venv/`、`__pycache__/`、单个超过 50MB 的文件、`.dsh/`。
5. 大文件（数据集、原始 PDF、视频）走网盘，链接写进 `data/README.md`。

## GitHub Desktop 三步

1. **File → Add local repository** → 选本文件夹（已克隆则跳过）
2. 改完在左侧 **Changes** 勾选文件 → 右下 **Summary** 写一句 → **Commit to main**
3. 顶部 **Push origin** 上传；动手前先点 **Pull origin** 下载队友改动

英文对照：Fetch=抓取，Pull=拉取，Push=推送，Commit=提交，Discard=放弃修改，History=历史。

## 分工

| 成员 | 负责 |
|---|---|
| 李乐 | `data/`、`results/`、`paper/main.tex` 总装 |
| 队友 A | `src/model_*.py` |
| 队友 B | `paper/` 各章节 |

## 出冲突了怎么办

GitHub Desktop 提示 `Conflicts` 时，最省事：**保留对方版本，把自己的改动另存一份再贴回去**，比手动解冲突快得多。
