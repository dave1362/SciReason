from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import FixKRetriever, ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.datasets import ChemBenchDataset, ChemBenchQADataset
from opencompass.utils.text_postprocessors import first_capital_postprocess
from opencompass.datasets import ChemBenchQA_Evaluator, ChemBenchQA_postprocess


chembench_reader_cfg = dict(
    input_columns=['input', 'A', 'B', 'C', 'D'],
    output_column='target',
    train_split='dev')

our_reader_cfg = dict(input_columns=['input'], output_column='output', train_split='dev')

chembench_all_sets = [
    'Name_Conversion',
    'Property_Prediction',
    'Mol2caption',
    'Caption2mol',
    'Product_Prediction',
    'Retrosynthesis',
    'Yield_Prediction',
    'Temperature_Prediction',
    'Solvent_Prediction'
]

our_infer_cfg_5shot = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following chemistry questions. '),
                # The placeholder is the ice_token string itself, used as a direct list element.
                '</E>',
            ],
            round=[
                dict(role='HUMAN', prompt='Query: {input}\nResponse: '), # for Qwen3
                # dict(role='HUMAN', prompt='{input}'),
                # dict(role='BOT', prompt='Response: '),
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
        fix_id_list=[0, 1, 2, 3, 4], # 使用前5个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=2048)
)

chembench_datasets = []
for _name in chembench_all_sets:
    # _hint = f'There is a single choice question about {_name.replace("_", " ")}. Answer the question by replying A, B, C or D.'
    _hint = f'There is a single choice question about chemistry. Answer the question by replying A, B, C or D.'

    chembench_infer_cfg = dict(
        ice_template=dict(
            type=PromptTemplate,
            template=dict(round=[
                dict(
                    role='HUMAN',
                    prompt=
                    f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: '
                ),
                dict(role='BOT', prompt='{target}\n')
            ]),
        ),
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin='</E>',
                round=[
                    dict(
                        role='HUMAN',
                        prompt=
                        f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: '  #/no_think
                    ),
                ],
            ),
            ice_token='</E>',
        ),
        retriever=dict(type=FixKRetriever, fix_id_list=[0, 1, 2, 3, 4]),
        inferencer=dict(type=GenInferencer),
    )

    chembench_infer_cfg_change_answer_position = dict(
        ice_template=dict(
            type=PromptTemplate,
            template=dict(round=[
                dict(
                    role='HUMAN',
                    prompt=
                    f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n'
                ),
                dict(role='BOT', prompt='Answer: {target}\n')
            ]),
        ),
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin='</E>',
                round=[
                    dict(
                        role='HUMAN',
                        prompt=
                        f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n'  #/no_think
                    ),
                ],
            ),
            ice_token='</E>',
        ),
        retriever=dict(type=FixKRetriever, fix_id_list=[0, 1, 2, 3, 4]),
        inferencer=dict(type=GenInferencer),
    )

    chembench_infer_cfg_one_shot = dict(
        ice_template=dict(
            type=PromptTemplate,
            template=dict(round=[
                dict(
                    role='HUMAN',
                    prompt=
                    f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: '
                ),
                dict(role='BOT', prompt='{target}\n')
            ]),
        ),
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin='</E>',
                round=[
                    dict(
                        role='HUMAN',
                        prompt=
                        f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: '  #/no_think
                    ),
                ],
            ),
            ice_token='</E>',
        ),
        retriever=dict(type=FixKRetriever, fix_id_list=[0,]),
        inferencer=dict(type=GenInferencer),
    )

    chembench_infer_cfg_zero_shot = dict(
        ice_template=dict(
            type=PromptTemplate,
            template=dict(round=[
                dict(
                    role='HUMAN',
                    prompt=
                    f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: /no_think'
                ),
                dict(role='BOT', prompt='{target}\n')
            ]),
        ),
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin='</E>',
                round=[
                    dict(
                        role='HUMAN',
                        prompt=
                        f'{_hint}\nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer: /no_think'  #/no_think
                    ),
                ],
            ),
            ice_token='</E>',
        ),
        retriever=dict(type=ZeroRetriever),
        inferencer=dict(type=GenInferencer),
    )

    chembench_eval_cfg = dict(
        evaluator=dict(type=AccEvaluator),
        pred_postprocessor=dict(type=first_capital_postprocess))

    our_infer_cfg = dict(

        ### for our SFT models
        prompt_template=dict(
            type=PromptTemplate,
            template="{input}\n{output}", # In your answer, molecules should be contained with <SMILES> </SMILES> tags.
        ),
        retriever=dict(type=ZeroRetriever),
        inferencer=dict(type=GenInferencer, max_out_len=2048))

    our_eval_cfg = dict(
        evaluator=dict(type=ChemBenchQA_Evaluator),
        pred_postprocessor=dict(type=ChemBenchQA_postprocess))

    chembench_datasets.append(
        dict(
            abbr=f'ChemBench_{_name}',
            type=ChemBenchDataset,
            path='opencompass/ChemBench4K',
            # path=f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/test/{_name}_benchmark.json_processed.json',
            name=_name,
            reader_cfg=chembench_reader_cfg,
            infer_cfg=chembench_infer_cfg,
            eval_cfg=chembench_eval_cfg,
        ))


    # chembench_datasets.append(
    #     dict(
    #         abbr=f'ChemBench_{_name}',
    #         type=ChemBenchQADataset,
    #         path='opencompass/ChemBench4K',
    #         # path=f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/test/{_name}_benchmark.json_processed.json',
    #         name=_name,
    #         reader_cfg=our_reader_cfg,
    #         infer_cfg=our_infer_cfg_5shot,
    #         eval_cfg=our_eval_cfg,
    #     ))

del _name, _hint
