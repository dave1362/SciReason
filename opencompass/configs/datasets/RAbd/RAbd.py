# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import RAbd_Dataset, RAbd_Evaluator, RAbd_postprocess


reader_cfg = dict(input_columns=['input'], output_column='output')

infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                # Optional but recommended: A system prompt for better instructions.
                dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions by answering protein patterns.'),
                # The placeholder is the ice_token string itself, used as a direct list element.
                '</E>',
            ],
            round = [
                dict(role='HUMAN', prompt='Query: {input}'),
                dict(role='BOT', prompt=''),
            ]
        ),
        ice_token="</E>",
    ),
    ice_template=dict(
        type=PromptTemplate,
        template = dict(
            round = [
                dict(role='HUMAN', prompt='Query: {input}'),
                dict(role='BOT', prompt='{output}'),
            ]
        )
    ),
    # retriever 负责检索并使用 ice_template 来格式化示例
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0,], # 使用前1个示例
    ),

    # prompt_template=dict(
    #     type=PromptTemplate,
    #     template="{input} Answer with <protein> </protein> tags.\n{output}",
    # ),
    # retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer, max_out_len=1024))

eval_cfg = dict(
    evaluator=dict(type=RAbd_Evaluator,),
    pred_postprocessor=dict(type=RAbd_postprocess),
    dataset_postprocessor=dict(type=RAbd_postprocess),
)


RAbd_datasets = [
    dict(
        abbr='RAbd',
        type=RAbd_Dataset,
        train_path='/fs-computility/ai4sData/scidata/SFT_processed/protein/test/RAbD_benchmark_test_protein_tagged.json',
        test_path='/fs-computility/ai4sData/scidata/SFT_processed/protein/test/RAbD_benchmark_test_protein_tagged.json',
        reader_cfg=reader_cfg,
        infer_cfg=infer_cfg,
        eval_cfg=eval_cfg
    ),

]
