from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import FixKRetriever
from opencompass.datasets import Bulk_modulus_material_Dataset, material_Evaluator, material_postprocessor

modulus_train_path = "SciReason/Conditional_generation/bulk_modulus_material/dev/data.json"
modulus_test_path = "SciReason/Conditional_generation/bulk_modulus_material/test/data.json"


modulus_material_reader = dict(input_columns=['input'], output_column='output')


generation_kwargs = dict(
    do_sample=True,
    # top_p=0.8,
    # min_p=0,
    #temperature=0.70,
    # top_k=20,
    # repetition_penalty=1,
        # "<|endoftext|>": 151643 "<|im_end|>": 151645
    # eos_token_id=[151643, 151645],
)

modulus_material_infer_cfg_5shot = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=[
                dict(role='SYSTEM', fallback_role='HUMAN', prompt=''),
                '</E>',
            ],
            round=[
                dict(role='HUMAN', prompt='{input}'),
            ],
        ),
        ice_token="</E>",
    ),
    ice_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='{input}'),
                dict(role='BOT', prompt='{output}'),
            ]
        )
    ),
    retriever=dict(
        type=FixKRetriever,
        fix_id_list=[0, 1, 2, 3, 4],  # 前5个示例
    ),
    inferencer=dict(type=GenInferencer, max_out_len=32000, generation_kwargs=generation_kwargs),
)

modulus_material_eval_cfg = dict(
    evaluator=dict(
        type=material_Evaluator,
        data_path=modulus_test_path,
    ),
    pred_postprocessor=dict(type=material_postprocessor),
)

modulus_material_datasets = [
    dict(
        abbr='bulk_modulus_to_material_generation_5shot',
        type=Bulk_modulus_material_Dataset,
        train_path=modulus_train_path,
        test_path=modulus_test_path,
        hf_hub=True,
        reader_cfg=modulus_material_reader,
        infer_cfg=modulus_material_infer_cfg_5shot,
        eval_cfg=modulus_material_eval_cfg,
    )
]