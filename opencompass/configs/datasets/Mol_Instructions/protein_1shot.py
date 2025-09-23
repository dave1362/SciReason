# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import (Mol_Instructions_postprocess_Protein, Mol_Instructions_Evaluator_Protein,
                                  Mol_Instructions_Dataset, Mol_Instructions_postprocess_Protein_Design,
                                  Mol_Instructions_Evaluator_Protein_Design, Mol_Instructions_Dataset_Protein_Design)

TASKS = [
    'catalytic_activity',
    'domain_motif',
    'general_function',
    'protein_function',
]

reader_cfg = dict(input_columns=['input'], output_column='output')

infer_cfg = dict(
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
    inferencer=dict(type=GenInferencer, max_out_len=32000)
)

eval_cfg = dict(
    evaluator=dict(type=Mol_Instructions_Evaluator_Protein),
    pred_postprocessor=dict(type=Mol_Instructions_postprocess_Protein),
    dataset_postprocessor=dict(type=Mol_Instructions_postprocess_Protein),
)

eval_cfg_protein_design = dict(
    evaluator=dict(type=Mol_Instructions_Evaluator_Protein_Design),
    pred_postprocessor=dict(type=Mol_Instructions_postprocess_Protein_Design),
    dataset_postprocessor=dict(type=Mol_Instructions_postprocess_Protein_Design),
)

dataset_root = '/fs-computility/ai4sData/scidata/SFT_processed/protein'

mol_protein_datasets = []

for task in TASKS:
    mol_protein_datasets.append(
        dict(
            abbr=f'mol_instruction_{task}',
            type=Mol_Instructions_Dataset,
            train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
            test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
            hf_hub=True,
            reader_cfg=reader_cfg,
            infer_cfg=infer_cfg,
            eval_cfg=eval_cfg))

task = 'protein_design'
mol_protein_datasets.append(
    dict(
        abbr='mol_instruction_protein_design',
        type=Mol_Instructions_Dataset_Protein_Design,
        train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
        test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
        hf_hub=True,
        reader_cfg=reader_cfg,
        infer_cfg=infer_cfg,
        eval_cfg=eval_cfg_protein_design))
