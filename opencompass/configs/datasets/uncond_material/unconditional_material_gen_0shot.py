from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.datasets import Uncond_material_Dataset, material_Evaluator, material_postprocessor

uncond_material_reader_cfg = dict(input_columns=['input'], output_column='output')

generation_kwargs = dict(
    do_sample=True,
    top_p=1,
    temperature=1.8,
    top_k=80,
)

uncond_material_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(
                    role='HUMAN',
                    prompt='{input}',
                ),
            ],
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer, generation_kwargs=generation_kwargs),
)

uncond_material_eval_cfg = dict(
            evaluator=dict(type=material_Evaluator),        
            pred_postprocessor=dict(type=material_postprocessor),
        )

uncond_material_datasets = [
    dict(
        abbr='unconditional_material_generation',
        type=Uncond_material_Dataset,
        num=5000,
        prompt='Generate a material composition with arbitrary elements and a specified space group. Your response should start with "<material>" and end with "</material>", with the flattened composition and space group tokens in between. A material with formula X₂Y₃ and space group number N should be represented as: <material>X X Y Y Y ⟨sg⟩ ⟨sgN⟩</material> No additional text.',
        reader_cfg=uncond_material_reader_cfg,
        infer_cfg=uncond_material_infer_cfg,
        eval_cfg=uncond_material_eval_cfg,
    )
]
