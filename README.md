# SciReasoner: Laying the Scientific Reasoning Ground Across Disciplines

[![arXiv](https://img.shields.io/badge/arXiv-Pending-B31B1B)](#)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-SciReason-FFAE1A)](https://huggingface.co/SciReason)
[![License](https://img.shields.io/badge/License-Apache_2.0-2D7DB1.svg)](https://www.apache.org/licenses/LICENSE-2.0)


This repository contains the evaluation code for the **SciReasoner** project.

---

## 🔧 Environment Setup

```bash
git clone https://github.com/open-sciencelab/SciReason.git
cd SciReason
conda create --name scireason python=3.10 -y
conda activate scireason
pip install -r requirements/training.txt
pip install -e .
```

> **Note**:
> The above instructions are for reference only.
> You may need to adjust them depending on your operating system and environment.

---

## 🚀 Running Evaluation

The evaluation script will automatically download the required datasets and models from [Hugging Face](https://huggingface.co/SciReason).
Please ensure your environment has internet access.

### Evaluate all datasets

```bash
opencompass examples_scireasoner/eval_all.py --max-num-worker 1
```

* **Default model:** [SciReasoner-8B](https://huggingface.co/SciReason/SciReasoner-8B)
* You can replace it with your own model if needed.
* The `--max-num-worker` option controls concurrency:

  * By default, each process uses one GPU.
  * Adjust it according to your available GPUs.

---

### Evaluate few-shot performance (e.g., for closed-source models like `o3`)

```bash
opencompass examples_scireasoner/eval_all_fewshot.py --max-num-worker 1
```

This script evaluates the few-shot capabilities of your model on all datasets.

---

### Evaluate specific datasets or custom models

* **To evaluate specific datasets:**
  Modify the configuration file to set `datasets` as a list of the datasets you want to test.

* **To use custom models:**
  Modify the configuration file to set `models` to your target model.

  * Reference format: `opencompass.configs.models.scireason.hf_scireasoner_8b`
  * For more model configuration options, please check the [OpenCompass documentation](https://opencompass.readthedocs.io/en/latest/).


Got it! I’ll add a **FAQ section** with the issue and solution clearly explained. Here’s how it fits into your README:


## ❓ FAQ

### 1. `meteor_score` Error

If you encounter an error related to `meteor_score`, you may need to download NLTK resources.

**Solution:**
In an environment with internet access, run:

```python
import nltk
nltk.download('wordnet')
```

By default, the files are downloaded to `/root/nltk_data`.
If you are using a **conda environment** and running on a compute node or container, download them into your conda environment instead:

```python
import nltk
import os

conda_path = os.path.join(os.environ["CONDA_PREFIX"], "nltk_data")
nltk.download('wordnet', download_dir=conda_path)
```

You can check all search paths using:

```python
import nltk
print(nltk.data.path)
```

### 2. Running on compute nodes without internet access

If your compute node cannot access the internet due to security policies, you need to **pre-download/cache the datasets and models** on a node with internet access first.

**Recommended steps:**

1. Set the environment variable `HF_HOME` to a **shared/public directory** for Hugging Face cache.
2. On a node with internet access, run a dummy model once to pre-cache everything:

   ```bash
   opencompass examples_scireasoner/eval_all_debug.py --max-num-worker 16
   ```
3. Now, you can run the actual evaluation code on the compute node without needing internet access.

### 3. Resuming from checkpoints & step-wise evaluation

Because the datasets are large and evaluation can be time-consuming, **OpenCompass supports resuming from checkpoints** and running evaluations in separate stages.

* To resume from a checkpoint, use the `-r` flag with the timestamp of the previous run:

  ```bash
  opencompass examples_scireasoner/eval_all.py -r <timestamp>
  ```

* To run specific stages only, use the `--mode` flag with one of the following options:

  * `all` – Run the full pipeline (default)
  * `infer` – Run inference only
  * `eval` – Run evaluation only
  * `viz` – Run visualization only

For more details, please refer to the [OpenCompass Quick Start Guide](https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html).

### 4. Dataset size cache issue  

If you only want to test a **subset** of a dataset by modifying the code to trim it, be aware that **OpenCompass caches the dataset size**.  

Before running the evaluation, it is recommended to either:  
- Delete the entire cache file:  
```
rm .cache/dataset_size.json
```
- Or remove the corresponding line for the modified dataset from the cache file.  

This ensures that OpenCompass recalculates the dataset size correctly.


---

## 🏗️ Codebase and References

This repository is built on top of [OpenCompass v0.4.2](https://github.com/open-compass/opencompass/tree/0.4.2) with custom modifications.
We plan to merge the changes back into the main OpenCompass branch in the future.

For more usage details, please refer to the [OpenCompass documentation](https://opencompass.readthedocs.io/en/latest/).


---

## 📜 License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).



You are free to use, modify, and distribute this project under the terms of the Apache 2.0 license.  
See the [LICENSE](LICENSE) file for full details.
