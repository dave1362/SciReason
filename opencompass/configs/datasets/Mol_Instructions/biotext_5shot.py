# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import Mol_Instructions_postprocess_BioText, Mol_Instructions_Evaluator_BioText, Mol_Instructions_Dataset_BioText

TASKS = [
         'chemical_disease_interaction_extraction',
         'chemical_entity_recognition',
         'chemical_protein_interaction_extraction',
         'multi_choice_question',
         'open_question',
         'true_or_false_question'
         ]

reader_cfg = dict(input_columns=['input'], output_column='output')

mol_biotext_datasets = []

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
        fix_id_list=[0, 1, 2, 3, 4], # 使用前5个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=32000)
)


for task in TASKS:
    eval_cfg = dict(
        evaluator=dict(type=Mol_Instructions_Evaluator_BioText, task=task),
        pred_postprocessor=dict(type=Mol_Instructions_postprocess_BioText, task=task),
        dataset_postprocessor=dict(type=Mol_Instructions_postprocess_BioText, task=task),
    )

    mol_biotext_datasets.append(
        dict(
            abbr=f'mol_instruction_{task}',
            type=Mol_Instructions_Dataset_BioText,
            train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
            test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
            hf_hub=True,
            reader_cfg=reader_cfg,
            infer_cfg=infer_cfg,
            eval_cfg=eval_cfg)
    )

