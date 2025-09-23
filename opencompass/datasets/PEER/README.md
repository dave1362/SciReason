# PEER_Evaluator · README

`PEER_Evaluator` 是一个轻量级的**自动评测器**：  
当普通规则难以判断模型输出是否正确时，它会调用 **GPT-4** 充当“裁判（Judge）”，给出 True / False 的裁决结果，再据此计算指标。

---

## 代码整体思路

| 步骤 | 具体做法（对应函数） | 目的 |
| ---- | ------------------- | ---- |
| 1. 初始化 | `__init__` 里接收 **GPT 模型名 / API Key / 并发线程数**，并创建 `OpenAI` 客户端 | 配置 LLM 环境 |
| 2. 调用重试 | `_retry_api` 用 **指数退避** 包裹任何函数（主要包裹 GPT 调用） | 保证网络不稳时依旧拿到结果 |
| 3. 单样本裁决 | `ask_gpt25` 构造 Prompt → GPT 返回 `True/False` | 让 LLM 判断一个回答对错 |
| 4. 批量并发裁决 | `ask_gpt25_batch` 用 `ThreadPoolExecutor` 并行跑 `ask_gpt25` | 加速大批量评测 |
| 5. 主评估流程 | `score`：<br>① 规范化预测，仅保留 “yes/no”<br>② 合法且与参考一致的直接打分<br>③ 其余样本丢进批量裁决<br>④ 把 LLM 裁决结果合并后 **计算 Accuracy / Precision / Recall / F1** | 完成整批数据的评测 |

---

## 核心 Prompt（在 `ask_gpt25` 中）

```text
请判断这个回答是否正确。
问题：{question}
参考答案：{answer}
模型回答：{prediction}
如果正确，请回答'True'；如果错误，请回答'False'。
请只回答'True'或'False'。
