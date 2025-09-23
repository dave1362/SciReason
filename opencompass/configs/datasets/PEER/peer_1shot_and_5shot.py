# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import PEER_postprocess, PEER_Evaluator, PEER_Dataset, PEER_postprocess_float_compare, PEER_postprocess_default

TASKS = [
    'solubility',
    'stability',
    'human_ppi',
    'yeast_ppi',
]

reader_cfg = dict(input_columns=['input'], output_column='output')

infer_cfg_5shot = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions.'),
                # The placeholder is the ice_token string itself, used as a direct list element.
                '</E>',
            ],
            round=[
                dict(role='HUMAN', prompt='Query: {input}\nResponse: '),
            ]
        ),
        ice_token="</E>",
    ),
    ice_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='Query: {input}'),
                dict(role='BOT', prompt='Response: {output}'),
            ]
        )
    ),
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0, 1, 2, 3, 4], # 使用前5个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=8192)
)

infer_cfg_1shot = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                # original prompts: There is a single choice question. Your answer should start with "The final answer is"
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions.'),
                # The placeholder is the ice_token string itself, used as a direct list element.
                '</E>',
            ],
            round=[
                dict(role='HUMAN', prompt='Query: {input}\nResponse '),
            ]
        ),
        ice_token="</E>",
    ),
    ice_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='Query: {input}'),
                dict(role='BOT', prompt='Response: {output}'),
            ]
        )
    ),
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0, ], # 使用前1个示例
    ),
    inferencer=dict(
        type=GenInferencer,
        # max_out_len=8192,
    )
)

eval_cfg = dict(
    evaluator=dict(type=PEER_Evaluator,),
    pred_postprocessor=dict(type=PEER_postprocess),
    dataset_postprocessor=dict(type=PEER_postprocess),
)

# use default postprocess to remain the original output for LLM judgement.
# PEER_postprocess will be used in the evaluation stage to compare the output with the ground truth as a fast comparison.
eval_llm_cfg = dict(
    evaluator=dict(type=PEER_Evaluator),
    pred_postprocessor=dict(type=PEER_postprocess_default),
    dataset_postprocessor=dict(type=PEER_postprocess_default),
)

eval_stability_cfg = dict(
    evaluator=dict(type=PEER_Evaluator, task='stability'),
    pred_postprocessor=dict(type=PEER_postprocess_float_compare, compare_number=1),
    dataset_postprocessor=dict(type=PEER_postprocess_float_compare, compare_number=1),
)

PEER_datasets = []

for task in TASKS:
    if task in ['stability', 'solubility']:
        infer_cfg = infer_cfg_1shot
    else:
        infer_cfg = infer_cfg_5shot
    PEER_datasets.append(
        dict(
            abbr=task,
            type=PEER_Dataset,
            train_path=f'SciReason/PEER-test/{task}/dev/data.json',
            test_path=f'SciReason/PEER-test/{task}/test/data.json',
            hf_hub=True,
            reader_cfg=reader_cfg,
            infer_cfg=infer_cfg,
            eval_cfg=eval_llm_cfg),
    )

