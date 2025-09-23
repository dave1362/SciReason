# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import Mol_Instructions_postprocess_Mol, Mol_Instructions_Evaluator_Mol, Mol_Instructions_Dataset

TASKS = [
         'property_prediction_str',
         'description_guided_molecule_design',
         'forward_reaction_prediction',
         'retrosynthesis',
         'reagent_prediction',
         'molecular_description_generation'
         ]

reader_cfg = dict(input_columns=['input'], output_column='output')

mol_mol_datasets = []

infer_cfg_1shot = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                # original prompts: There is a single choice question. Your answer should start with "The final answer is"
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions. Your final answer should be bounded within a <SMILES> </SMILES> tag.'),
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

infer_cfg_1shot_figure = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                # original prompts: There is a single choice question. Your answer should start with "The final answer is"
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions. Your final answer should be a float number.'),
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
    # retriever 负责检索并使用 ice_template 来格式化示例
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0, ], # 使用前1个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=8192)
)

infer_cfg_1shot_molecular_description = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                # original prompts: There is a single choice question. Your answer should start with "The final answer is"
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions. Your final answer should start with "The molecule is".'),
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
                dict(role='HUMAN', prompt='Query: {input}'), # for Qwen3
                dict(role='BOT', prompt='Response: {output}'),
                # dict(role='HUMAN', prompt='{input}'),
                # dict(role='BOT', prompt='{output}'),
            ]
        )
    ),
    # retriever 负责检索并使用 ice_template 来格式化示例
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0, ], # 使用前1个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=8192)
)


for task in TASKS:
    eval_cfg = dict(
        evaluator=dict(type=Mol_Instructions_Evaluator_Mol, task=task),
        pred_postprocessor=dict(type=Mol_Instructions_postprocess_Mol, task=task),
        dataset_postprocessor=dict(type=Mol_Instructions_postprocess_Mol, task=task),
    )

    if task not in ['property_prediction_str', 'molecular_description_generation']:
        mol_mol_datasets.append(
            dict(
                abbr=f'mol_instruction_{task}',
                type=Mol_Instructions_Dataset,
                train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
                test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
                hf_hub=True,
                reader_cfg=reader_cfg,
                infer_cfg=infer_cfg_1shot,
                eval_cfg=eval_cfg)
        )
    elif task == 'property_prediction_str':
        mol_mol_datasets.append(
            dict(
                abbr=f'mol_instruction_{task}',
                type=Mol_Instructions_Dataset,
                train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
                test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
                hf_hub=True,
                reader_cfg=reader_cfg,
                infer_cfg=infer_cfg_1shot_figure,
                eval_cfg=eval_cfg)
            )
    elif task == 'molecular_description_generation':
        mol_mol_datasets.append(
            dict(
                abbr=f'mol_instruction_{task}',
                type=Mol_Instructions_Dataset,
                train_path=f'SciReason/Mol-Instructions-test/{task}/dev/data.json',
                test_path=f'SciReason/Mol-Instructions-test/{task}/test/data.json',
                hf_hub=True,
                reader_cfg=reader_cfg,
                infer_cfg=infer_cfg_1shot_molecular_description,
                eval_cfg=eval_cfg
            )
        )



