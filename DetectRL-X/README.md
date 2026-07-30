<p align="center">
    <img src="../image/logo_1.png" width="250" style="margin-bottom: 0.2;"/>
<p>

# DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection

<div align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![ACL 2026](https://img.shields.io/badge/ACL-2026-blue)](https://www.2026.aclweb.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-yellow)](https://huggingface.co/datasets/WUJUNCHAO/DetectRL-X)

⭐ [_**University of Macau**_](https://www.um.edu.mo) &nbsp; | &nbsp; [_**Alibaba Group**_](https://www.alibaba.com) &nbsp; | &nbsp; [_**Xiamen University**_](https://www.xmu.edu.cn) ⭐

:octocat: [**GitHub**](https://github.com/AIDC-AI/Marco-LLM) &nbsp; 🤗 [**Data**](https://huggingface.co/datasets/WUJUNCHAO/DetectRL-X) &nbsp; 📝 [**Paper**](https://arxiv.org/abs/2605.15518)

</div>

## 📖 Introduction

The effective detection and governance of Large Language Model (LLM) generated content has become increasingly critical due to the growing risk of misuse. Despite the impressive performance of existing detectors, their reliability and potential in multilingual, real-world scenarios remain largely underexplored.

**DetectRL-X** is the most large-scale and challenging multilingual benchmark for LLM-generated text (LGT) detection, containing **3.46 million samples** spanning **8 languages**, **6 domains**, **4 generators**, **8 attack strategies**, **4 text-length granularities**, and **3 types of refinement operations**, with **8 evaluation dimensions** comparing **12 detectors**.

We extend the traditional Binary classification task (HWT vs. LGT) to a **Ternary setting** that also identifies human-written & LLM-refined text (HLT), better reflecting real-world human-LLM collaboration. The benchmark reveals the strengths and limitations of current state-of-the-art detectors when applied to diverse linguistic resources, and provides a multilingual data augmentation framework for building adversarial benchmarks.

## 🔭 Benchmark Overview

<p align="center">
  <img src="imgs/DetectRL-X.png" width="90%" alt="DetectRL-X Benchmark Overview">
</p>

DetectRL-X evaluates detectors in a realistic, multilingual setting by combining human-written texts, LLM-generated texts, AI-refined texts, and attacked texts through multilingual paraphrasing and perturbation strategies.

### Comparison with Existing Benchmarks

DetectRL-X is the first benchmark to simultaneously support **Binary & Ternary classification** in a fully **multilingual** setting with balanced domain and generator distributions, as summarized in Table 1 of the paper.

| Benchmark | Size | Task | | Real-World | | | | | |       Multilingual       | | | |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:--:|:---:|:------------:|:---:|:---:|:---:|
| | | Binary | Ternary | Multi-Domain | Multi-Generator | Paraphrase Attack | Perturbation Attack | Multi-Length | Multi-Operation | Language Num | Domain Balance? | Generator Balance? | Multilingual Attacks? |
| TuringBench | 168K | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |      1       | ✗ | ✗ | ✗ |
| HC3 | 125K | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |      2       | ✗ | ✗ | ✗ |
| MGTBench | 21K | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |      1       | ✗ | ✗ | ✗ |
| MULTITuDE | 74K | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ |      11      | ✗ | ✓ | ✗ |
| M4 | 245K | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |      7       | ✗ | ✗ | ✗ |
| MAGE | 448K | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |      1       | ✗ | ✗ | ✗ |
| RAID | 6,287K | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |      1       | ✗ | ✗ | ✗ |
| Stumbling Blocks | 10K | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ |      1       | ✗ | ✓ | ✗ |
| DetectRL | 235K | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |      1       | ✗ | ✗ | ✗ |
| **DetectRL-X (Ours)** | **3,456K** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |    **8**     | **✓** | **✓** | **✓** |

## ✨ Key Features

### Language Coverage (8 Languages)

Spanning **5 language families** with 3 complexity levels based on morphological richness:

| Complexity | Languages | Families |
|:---|:---|:---|
| **High** | Arabic, Russian, Chinese | Semitic, Slavic, Sino-Tibetan |
| **Medium** | German, French, Spanish, Portuguese | Germanic, Romance |
| **Low** | English | Germanic |

### Domain Coverage (6 Domains)

Human-written texts are curated from domains highly susceptible to LLM misuse:

| Domain | Description |
|:---|:---|
| Academic | Scholarly writing and research papers |
| News | Journalistic reporting and articles |
| Novel | Creative fiction and literary works |
| SEO | Search engine optimization content and marketing copy |
| Wiki | Wikipedia-style encyclopedic entries |
| WebText | General web content from diverse online sources |

All texts are collected exclusively from publicly available internet sources published prior to 2022 to ensure authenticity.

### Generators (4 Commercial LLMs)

Texts are generated using 4 mainstream multilingual LLMs:

| Generator | Description |
|:---|:---|
| Deepseek-V3 | Latest large-scale MoE language model |
| Gemini-2.5-flash | Google's high-performance multilingual model |
| GPT-4o | OpenAI's flagship multimodal model |
| Qwen-Max | Alibaba's advanced multilingual LLM |

### Text Refinement, Attack & Length

- **3 refinement operations** (Polishing, Expanding, Condensing) applied to both HWT and LGT, defining three text categories: HWT, HLT, LGT
- **8 attack strategies**: 4 paraphrase (Encoder Paraphrasing, Seq2seq Paraphrasing, Decoder Paraphrasing, Back-Translation) + 4 perturbation (Character Insertion, Character Substitution, Character Deletion, Zero-width Insertion), uniformly applicable across all languages
- **4 text-length granularities**: 64, 128, 256, and 512 tokens

> See [Rewriting Strategies](#rewriting-strategies) below for detailed descriptions of each strategy.

### Evaluation Dimensions (8 Dimensions)

| Dimension | Description |
|:---|:---|
| **In-Distribution** | Mixed distribution across all languages, domains, and generators |
| **Cross-Domain** | Generalization to unseen domains |
| **Cross-Generator** | Generalization to unseen generators |
| **Cross-Language** | Generalization to unseen languages |
| **Cross-Paraphrase** | Robustness against 4 paraphrase attacks |
| **Cross-Perturbation** | Robustness against 4 perturbation attacks |
| **Cross-Length** | Robustness to 4 text length granularities |
| **Cross-Operation** | Robustness to 3 text refinement operations |

### Evaluation Metrics

- **Best F1 Score (F<sub>1</sub><sup>B</sup>)**: Optimal balance between precision and recall, with threshold determined by maximizing Youden's J statistic
- **F1 at FPR=0.01 (F<sub>1</sub><sup>F</sup>)**: F1 score at a fixed low false positive rate (0.01), reflecting reliability in minimal-tolerance scenarios

## 🛡️ Evaluated Detectors (12 Methods)

We benchmark 12 representative detectors covering both statistical and neural-based approaches:

**Statistical-based Methods** (9):
Log-Likelihood, Log-Rank, DetectLLM-LRR, GECScore, ReviseDetect, Fast-DetectGPT, Binoculars, Lastde++, RepreGuard

**Neural-based Methods** (3):
XLM-RoBERTa-Classifier (X-Rob-Classifier), mDeBERTa-Classifier, Biscope

### Main Results

| # | Finding                                                                                                                                                                                                                                                                                                                                                                     |
|:---|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | **Neural > Statistical**: Neural-based detectors consistently outperform statistical-based detectors. XLM-RoBERTa-Classifier ranks **1st** on the Binary leaderboard (avg F<sub>1</sub><sup>B</sup> **95.58%**, F<sub>1</sub><sup>F</sup> **91.31%**), while mDeBERTa-Classifier leads Ternary (F<sub>1</sub><sup>B</sup> **87.68%**, F<sub>1</sub><sup>F</sup> **81.10%**) |
| 2 | **Limitations of Statistical Methods**: Even in In-Distribution, statistical-based detectors average only F<sub>1</sub><sup>B</sup> **67.89%**, with the best (GECScore) reaching **83.22%**, indicating poor robustness to real-world heterogeneity                                                                                                                        |
| 3 | **Cross-Lingual Challenge**: Neural-based detectors drop F<sub>1</sub><sup>B</sup> from 95.3% → 91.4% (↓3.9%) in Binary and 87.10% → 66.28% (↓**20.82%**) in Ternary cross-lingual settings. Statistical methods show smaller but more variable degradation                                                                                                                 |
| 4 | **Cross-Domain > Cross-Generator**: Cross-Domain is substantially harder. Neural detectors drop **2.95%** in Binary cross-domain vs only **0.78%** in cross-generator. In Ternary, mDeBERTa-Classifier drops **18.2%** cross-domain vs **4.9%** cross-generator                                                                                                             |
| 5 | **Paraphrase & Perturbation Vulnerability**: Paraphrase attacks inflict the most damage — neural F<sub>1</sub><sup>B</sup> drops **28.1%** (Binary) and **16.8%** (Ternary). Perturbation attacks cause **13.1%** (Binary) and **4.3%** (Ternary) drops. Statistical detectors suffer even more (25–40%)                                                                    |
| 6 | **Length & Operation Sensitivity**: In Binary, neural F<sub>1</sub><sup>B</sup> drops ~4.5% (cross-length) and ~1% (cross-operation). In Ternary, declines reach **11.9%** and **13.4%**, with statistical methods dropping **35–40%** in both tasks                                                                                                                        |
| 7 | **Ternary Difficulty**: Ternary is inherently harder — statistical F<sub>1</sub><sup>B</sup> drops from 67.9% → 39.3% (↓**28.6%**), neural from 97.6% → 87.1% (↓**10.5%**). Overall average: statistical ↓23.0%, neural ↓13.7%                                                                                                                                              |
| 8 | **Low-FPR Usability Gap**: Many detectors achieve high F<sub>1</sub><sup>B</sup> but drop sharply in F<sub>1</sub><sup>F</sup>. For example, GECScore declines **12.7%** and Binoculars **14.0%** under strict FPR=0.01 constraints                                                                                                                                         |

### Analysis across Languages

| # | Finding |
|:---|:---|
| 9 | **Complexity Has Minimal Impact**: Language complexity affects detection only within **±3%** — high (81.9%), medium (83.5%), and low (80.5%) complexity languages show comparable Binary F<sub>1</sub><sup>B</sup>. No clear correlation between linguistic complexity and detection performance |
| 10 | **Best/Worst per Language**: Detectors perform best on **Arabic** (Binary/Ternary F<sub>1</sub><sup>B</sup>: 85.6%/63.4%) and worst on **Russian** (80.5%/53.6%), despite both being high-complexity languages |
| 11 | **Cross-Domain Language Sensitivity**: Domain variation significantly amplifies sensitivity in Ternary, with cross-domain drops widening from ~5% to larger gaps across languages. Formal vs informal domains show particularly divergent results |
| 12 | **Attack Robustness by Language**: Mean F<sub>1</sub><sup>B</sup> varies across languages under attacks. Paraphrase consistently degrades performance across all languages, with semantic-preserving transformations being the most challenging |
| 13 | **Length Benefits Complex Languages**: Longer text improves detection — the performance gap between complex and simple languages narrows as token count increases from 64 to 512 |
| 14 | **Refinement Varies by Language**: Cross-operation analysis reveals significant **language-dependent** variation, with complex languages showing greater sensitivity to refinement operations (polishing, expanding, condensing) |

## 📊 Dataset Statistics

The DetectRL-X dataset comprises **3,456,000 samples** with a 2:1 train-test split, balanced across all languages, domains, and generators.

| Category | Subcategory | Samples |
|:---|:---|:---:|
| **Original Samples** | Human-written (HWT) | 144,000 |
| | LLM-generated (LGT) | 144,000 |
| **LLM-refined Samples** | Human + Polishing | 144,000 |
| *(Various Operation Behaviour)* | Human + Expanding | 144,000 |
| | Human + Condensing | 144,000 |
| | LLM + Polishing | 144,000 |
| | LLM + Expanding | 144,000 |
| | LLM + Condensing | 144,000 |
| **Paraphrasing Attacks** | Encoder Paraphrasing | 144,000 |
| | Seq2seq Paraphrasing | 144,000 |
| | Decoder Paraphrasing | 144,000 |
| | Back-Translation | 144,000 |
| **Perturbation Attacks** | Character Insertion | 144,000 |
| | Character Substitution | 144,000 |
| | Character Deletion | 144,000 |
| | Zero-width Insertion | 144,000 |
| **Multi-length Samples** | 64 / 128 / 256 / 512 tokens | 1,152,000 |
| **Total** | | **3,456,000** |

The dataset is organized as follows:
- **Original samples**: 288K samples for human-LLM comparison, balanced across 8 languages, 6 domains, and 4 generators
- **LLM-refined samples**: 864K samples covering 3 operations applied to both HWT and LGT, reflecting real-world human-LLM collaboration
- **Attack samples**: 576K paraphrase + 576K perturbation = 1,152K samples for adversarial stress testing
- **Multi-length samples**: 1,152K samples across 4 length granularities to assess length sensitivity

### File Structure

```
DetectRL-X/
├── Binary/                    # 2-way classification (human vs. LLM)
│   ├── binary_general_open.json
│   ├── binary_general_64_open.json
│   ├── binary_general_128_open.json
│   ├── binary_general_256_open.json
│   ├── binary_general_512_open.json
│   ├── binary_backtranslation_open.json
│   ├── binary_encoder_paraphrasing_open.json
│   ├── binary_decoder_paraphrasing_open.json
│   ├── binary_seq2seq_paraphrasing_open.json
│   ├── binary_character_deletion_open.json
│   ├── binary_character_insertion_open.json
│   ├── binary_character_substitution_open.json
│   ├── binary_zero_width_insertion_open.json
│   ├── binary_polishing_open.json
│   ├── binary_expanding_open.json
│   └── binary_condensing_open.json
└── Ternary/                   # 3-way classification (human vs. LLM vs. LLM-refined)
    ├── trinary_general_open.json
    ├── trinary_general_64_open.json
    ├── trinary_general_128_open.json
    ├── trinary_general_256_open.json
    ├── trinary_general_512_open.json
    ├── trinary_backtranslation_open.json
    ├── trinary_encoder_paraphrasing_open.json
    ├── trinary_decoder_paraphrasing_open.json
    ├── trinary_seq2seq_paraphrasing_open.json
    ├── trinary_character_deletion_open.json
    ├── trinary_character_insertion_open.json
    ├── trinary_character_substitution_open.json
    ├── trinary_zero_width_insertion_open.json
    ├── trinary_expanding_open.json
    └── trinary_condensing_open.json
```

> **Note**: Only `*_open.json` files are publicly released. `*_heldout.json` files are reserved for a shared task and will be released later.

### Rewriting Strategies

Each strategy applies a specific transformation to LLM-generated text to simulate real-world evasion attempts. The strategies are organized into four categories:

**Paraphrasing Strategies** — Systematically rewrite text content to generate semantically equivalent yet expressionally diverse textual variants, while preserving the core meaning.

| Strategy | Description |
|:---|:---|
| encoder_paraphrasing | Employs advanced encoder architectures (Encoder-only model) to intelligently identify and mask key textual segments, generating alternative content that is strictly semantically equivalent but significantly varied at the lexical level, while ensuring linguistic fluency |
| seq2seq_paraphrasing | Leverages powerful sequence-to-sequence architectures (fine-tuned multilingual mT5) to enable fine-grained rewriting of complex structures and long passages, effectively simulating diverse patterns found in human-authored text |
| decoder_paraphrasing | Capitalizes on large-scale pretrained decoder-only language models (fine-tuned multilingual Qwen-2.5-7B via DPO) to demonstrate exceptional capability in creative paraphrasing, generating grammatically robust and semantically diverse variants |
| backtranslation | A classic paraphrasing technique that generates semantically faithful yet expressively novel textual variants by exploiting the linguistic transformations inherent in a "source → target → source" bidirectional pipeline (using multilingual mBART, with English as pivot for non-English inputs, Chinese as pivot for English) |

**Perturbation Strategies** — Language-agnostic and universally applicable adversarial perturbations designed to simulate pervasive perturbations that transcend specific languages and writing systems. All strategies adhere to a unified "low-level intervention" principle: independent of specific linguistic grammars, tokenize the input and randomly sample 15% of the words for physical-level modification.

| Strategy | Description |
|:---|:---|
| character_insertion | Systematically repeats the preceding character at arbitrary positions within selected words, simulating common "repetitive keystroke" errors. Entirely independent of specific lexical or syntactic rules, applicable to Latin, Cyrillic, or other alphabetic systems without language-specific customization |
| character_substitution | Exploits the vast Unicode standard to replace characters with visually identical (or highly similar) but uniquely encoded counterparts (e.g., Latin "a" with Cyrillic "a"). Uses authoritative cross-textual obfuscation dictionaries including Unicode Confusables, Arabic Shaping, and homoglyph corpora |
| character_deletion | Randomly removes characters from selected words, mimicking spelling omissions during rapid typing. A non-parametric attack requiring no external knowledge bases, introducing pure structural entropy to test model robustness against low-quality, noisy multilingual inputs |
| zero_width_insertion | Injects non-printing or zero-width Unicode control characters (Zero Width Space U+200B, Zero Width Non-Joiner U+200C, Zero Width Joiner U+200D, Word Joiner U+2060). These are integral to the core Unicode standard and supported by virtually all global text processing systems, creating a universal attack vector that is visually "invisible" |

**Structure-Level Strategies** — Modify the structural properties (e.g., length, fluency) of the text through LLM-assisted refinement operations.

| Strategy | Description |
|:---|:---|
| condensing | Condense/compress the text by removing redundancies while preserving core meaning |
| expanding | Expand/elaborate the text |
| polishing | Polish the text for fluency (Binary only) |

**General Strategies** — Default experimental setting with optional length restrictions.

| Strategy | Description |
|:---|:---|
| general | Default experimental setting (no length restriction) |
| general_64 | Texts truncated to max 64 tokens |
| general_128 | Texts truncated to max 128 tokens |
| general_256 | Texts truncated to max 256 tokens |
| general_512 | Texts truncated to max 512 tokens |

### Data Fields

**Binary Subset:**

| Field | Type | Description |
|:---|:---|:---|
| `human_written_text` | string | Original human-written text |
| `llm_generated_text` | string | Text generated by an LLM |
| `lang` | string | Language (arabic, chinese, english, french, german, portuguese, russian, spanish) |
| `model` | string | LLM used (deepseek-v3, gemini-2.5-flash, gpt-4o, qwen-max) |
| `split` | string | Data split (train / test) |
| `domain` | string | Text domain (e.g., News, Academic, etc.) |

**Ternary Subset:**

| Field | Type | Description |
|:---|:---|:---|
| `human_written_text` | string | Original human-written text |
| `llm_generated_text` | string | Text generated by an LLM |
| `llm_refined_text` | string | LLM-generated text further refined/rewritten |
| `lang` | string | Language |
| `model` | string | LLM used |
| `split` | string | Data split (train / test) |
| `domain` | string | Text domain |

### OOD Robustness Testing

A key design principle of DetectRL-X is evaluating **out-of-distribution (OOD) robustness** of detection models:

- The **train split is identical** across all strategy files — it contains the same human-written and LLM-generated text pairs
- The **test split differs** across strategies — each strategy file applies its specific rewriting transformation to the test set

This design allows researchers to:
1. Train a detector on standard human vs. LLM text pairs (shared train set)
2. Evaluate the detector's robustness against various rewriting strategies (strategy-specific test sets)
3. Compare performance across strategies fairly, since the train set is held constant

> **Space-saving tip**: Since the train split is duplicated across all strategy files, you can download only one file's train split and the test splits of the strategies you're interested in to save storage space.

### Open vs. Heldout

The dataset is partitioned along three dimensions: **8 languages × 4 LLMs × 6 domains = 192 cells**.

| Partition | Availability | Splits | Samples | Per Cell | Purpose |
|:---|:---:|:---|:---:|:---:|:---|
| `*_open.json` | ✅ Public | train (400) + test (250) | 124,800 | 650 | Training and open evaluation |
| `*_heldout.json` | 🔒 Shared task only | train (100) | 19,200 | 100 | Reserved for shared task evaluation |

The heldout set was created via stratified sampling (100 train samples per (lang, model, domain) cell) with a fixed random seed (SEED=42), ensuring that the same samples are held out across all strategy files for fair cross-strategy comparison.

## 📥 Dataset Access

```bash
# HuggingFace
https://huggingface.co/datasets/WUJUNCHAO/DetectRL-X
```

### Loading the Dataset

**Using Hugging Face `datasets`:**

```python
from datasets import load_dataset

# Load a specific strategy from Binary
dataset = load_dataset("WUJUNCHAO/DetectRL-X", data_files="Binary/binary_general_open.json")

# Load a specific strategy from Ternary
dataset = load_dataset("WUJUNCHAO/DetectRL-X", data_files="Ternary/trinary_general_open.json")

print(dataset["train"][0])
```

**Using `ijson` (for large files, streaming):**

```python
import ijson

with open("binary_general_open.json", "rb") as f:
    for item in ijson.items(f, "item"):
        print(item["human_written_text"][:100])
        break
```

### Example Sample

```json
{
  "human_written_text": "قمة اميركية سعودية في الرياض مع بدء عهد الملك سلمان...",
  "llm_generated_text": "زيارة أوباما للسعودية: إحياء للعلاقات الاستراتيجية...",
  "lang": "arabic",
  "model": "deepseek-v3",
  "split": "train",
  "domain": "News"
}
```

## 🤖 Released Models

### Detector

| Model | Description | Link |
|:---|:---|:---|
| DetectRL-X-XLM-RoBERTa-Detector-All | XLM-RoBERTa-based detector fine-tuned on DetectRL-X across all languages | 🤗 [WUJUNCHAO/DetectRL-X-XLM-RoBERTa-Detector-All](https://huggingface.co/WUJUNCHAO/DetectRL-X-XLM-RoBERTa-Detector-All) |

### Multilingual Paraphraser Models

Decoder-based paraphrasing models fine-tuned via DPO on Qwen-2.5-7B, one per language:

| Language | Model |
|:---|:---|
| Arabic | 🤗 [WUJUNCHAO/Qwen-Paraphraser-Arabic-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-Arabic-DPO) |
| Chinese | 🤗 [WUJUNCHAO/Qwen-Paraphraser-Chinese-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-Chinese-DPO) |
| English | 🤗 [WUJUNCHAO/Qwen-Paraphraser-English-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-English-DPO) |
| French | 🤗 [WUJUNCHAO/Qwen-Paraphraser-French-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-French-DPO) |
| German | 🤗 [WUJUNCHAO/Qwen-Paraphraser-German-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-German-DPO) |
| Portuguese | 🤗 [WUJUNCHAO/Qwen-Paraphraser-Portuguese-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-Portuguese-DPO) |
| Russian | 🤗 [WUJUNCHAO/Qwen-Paraphraser-Russian-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-Russian-DPO) |
| Spanish | 🤗 [WUJUNCHAO/Qwen-Paraphraser-Spanish-DPO](https://huggingface.co/WUJUNCHAO/Qwen-Paraphraser-Spanish-DPO) |

## 📧 Contact

For questions or suggestions, please contact us:
- nlp2ct.junchao@gmail.com

## 📄 License

This dataset is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Usage is strictly restricted to non-commercial academic research purposes.

## 🙏 Acknowledgments

Special thanks to all contributors, annotators, and translators who participated in dataset construction and validation. This project is supported by Alibaba Group, University of Macau, and Xiamen University.

## 📝 Citation

```bibtex
@inproceedings{wu-etal-2026-detectrl,
    title = "{D}etect{RL}-{X}: Towards Reliable Multilingual and Real-World {LLM}-Generated Text Detection",
    author = "Wu, Junchao  and
      Liu, Yefeng  and
      Zhu, Chenyu  and
      Zhang, Hao  and
      Wu, Zeyu  and
      Shi, Tianqi  and
      Du, Yichao  and
      Wang, Longyue  and
      Luo, Weihua  and
      Su, Jinsong  and
      Wong, Derek F.",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.1773/",
    doi = "10.18653/v1/2026.acl-long.1773",
    pages = "38247--38294",
}
```