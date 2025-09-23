
import json
import multiprocessing
from functools import partial
import re
from os import environ
from typing import Union

import pandas as pd
from datasets import Dataset, DatasetDict
from rdkit import Chem, RDLogger
from rdkit.Chem import MACCSkeys
from rdkit import DataStructs
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
from tqdm import tqdm
from opencompass.registry import LOAD_DATASET, TEXT_POSTPROCESSORS
from opencompass.openicl import BaseEvaluator

@TEXT_POSTPROCESSORS.register_module("ChemBenchQA_postprocess")
def ChemBenchQA_postprocess(text, *args, **kwargs):
    # text = text.strip()
    # text = re.sub(r'<\|endoftext\|>', '', text)
    # text = re.sub(r'<\|im_end\|>', '', text)
    # num_match = re.search(r'[-+]?\d*\.\d+|\d+', text)
    # text = num_match.group(0) if num_match else 0

    return text

class ChemBenchQA_Evaluator(BaseEvaluator):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def score(self, predictions, references):
        if len(predictions) != len(references):
            return {
                'error': 'predictions and references have different '
                'length'
            }
        if not isinstance(predictions[0], list):
            predictions = [[pred] for pred in predictions]
        if not isinstance(references[0], list):
            references = [[ref] for ref in references]

        pred_list = predictions
        gold_list = references

        # import pdb;pdb.set_trace()

        total_num = len(pred_list)
        correct_num = 0
        for pred, gold in zip(pred_list, gold_list):
            if len(pred) != 1 or len(gold) != 1:
                continue
            pred = pred[0]
            gold = gold[0]
            if pred == gold:
                correct_num += 1

        return {
            'acc': correct_num / total_num if total_num > 0 else 0,
            'total_num': total_num,
            'correct_num': correct_num
        }


from openai import OpenAI
import numpy as np
import time
MAX_RETRIES = 3
BACKOFF_SEC = 2

def _retry_api(fn, *args, **kwargs):
    last_exc = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            result = fn(*args, **kwargs)
            if result is not None:
                return result
            raise ValueError("Received None")
        except Exception as e:
            last_exc = e
            sleep_time = BACKOFF_SEC ** attempt
            print(f"[retry] attempt {attempt} failed ({e}), retrying in {sleep_time}s…")
            time.sleep(sleep_time)
    raise last_exc

def ask_gpt25(client, answer, prediction):
    prompt = (
        "请判断这个回答是否正确。 定义：“正确”：模型回答的核心结论（如是否存在相互作用）与参考答案完全一致（不要求字面相同）；“错误”：模型回答的核心结论与参考答案相反，或未明确表达核心结论。"
        f"参考答案：{answer}"
        f"模型回答：{prediction}"
        "如果正确，请回答'True'；如果错误，请回答'False'。请只回答'True'或'False'。"
    )

    def _call():
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip().upper()
        print("=== GPT 判断结果 ===")
        print(f"Prompt:\n{prompt}")
        print(f"Output:\n{result}")
        return result

    try:
        return _retry_api(_call)
    except Exception as e:
        print(f"[GPT ERROR] Exception: {e}")
        return ''


def main():
    pass

if __name__ == '__main__':
    main()



