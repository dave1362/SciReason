import json
import os.path as osp

from datasets import Dataset, DatasetDict

from opencompass.registry import LOAD_DATASET
from opencompass.utils import get_data_path

from .base import BaseDataset


@LOAD_DATASET.register_module()
class ChemBenchDataset(BaseDataset):

    @staticmethod
    def load(path: str, name: str):
        dataset = DatasetDict()
        path = get_data_path(path)
        # import pdb;pdb.set_trace()
        for split in ['dev', 'test']:
            raw_data = []
            filename = osp.join(path, split, f'{name}_benchmark.json')
            # if split == 'test':
            #     _name = 'Solvent_Prediction'
            #     filename = f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/test/tagged_json/{_name}_benchmark.json_processed.json'
            # if split == 'dev':
            #     _name = 'Solvent_Prediction'
            #     filename = f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/dev/tagged_json/{_name}_benchmark.json_processed.json'
            with open(filename, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            for item in data:
                raw_data.append({
                    'input': item['question'],
                    'A': item['A'],
                    'B': item['B'],
                    'C': item['C'],
                    'D': item['D'],
                    'target': item['answer'],
                })

            # if split == 'test':
            #     raw_data = raw_data[::10]

            dataset[split] = Dataset.from_list(raw_data)
        return dataset

@LOAD_DATASET.register_module()
class ChemBenchQADataset(BaseDataset):

    @staticmethod
    def load(path: str, name: str):
        dataset = DatasetDict()
        path = get_data_path(path)
        split = 'test'
        filename = f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/tagged_test/{name}_benchmark.json_processed.json'
        with open(filename, 'r', encoding='utf-8') as json_file:
            raw_data = json.load(json_file)
        # import pdb;pdb.set_trace()
        data = raw_data
        dataset[split] = Dataset.from_list(data)

        # dev_path = f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/tagged_test/{name}_benchmark.json_processed.json'
        dev_path = f'/fs-computility/ai4sData/scidata/SFT_processed/molecule/test/ChemBench4K/dev_converted/{name}_benchmark.json'
        with open(dev_path, 'r', encoding='utf-8') as json_file:
            dev_data = json.load(json_file)

        dataset['dev']= Dataset.from_list(dev_data)
        return dataset
