from opencompass.models import DummyHuggingFaceModel

models = [
    dict(
        type=DummyHuggingFaceModel,
        abbr='',
        path='',
        max_out_len=32000,
        batch_size=1,
        run_cfg=dict(num_gpus=0),
    )
]