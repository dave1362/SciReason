from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.datasets import Uncond_RNA_Dataset, RNA_Evaluator, RNA_postprocessor

uncond_RNA_reader_cfg = dict(input_columns=['input'], output_column='output')

generation_kwargs = dict(
    do_sample=True,
    top_p=1,
    temperature=1.8,
    top_k=80,
)

uncond_RNA_infer_cfg = dict(
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

uncond_RNA_eval_cfg = dict(
            evaluator=dict(type=RNA_Evaluator),        
            pred_postprocessor=dict(type=RNA_postprocessor),
        )

uncond_RNA_datasets = [
    dict(
        abbr='unconditional_RNA_generation',
        type=Uncond_RNA_Dataset,
        num=5000,
        prompt='Generate a natural RNA sequence with a length of no more than 1024 nucleotides. The sequence should only contain the bases C, U, A, and G. Your response should start with "<rna>" and end with "</rna>", with the RNA sequence in between. No additional text.',
        reader_cfg=uncond_RNA_reader_cfg,
        infer_cfg=uncond_RNA_infer_cfg,
        eval_cfg=uncond_RNA_eval_cfg,
    )
]
