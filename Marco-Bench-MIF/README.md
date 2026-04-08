<p align="center">
    <img src="../image/logo_1.png" width="250" style="margin-bottom: 0.2;"/>
<p>

# Marco-Bench-MIF: On Multilingual Instruction-Following Capability of Large Language

<div align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![ACL 2025](https://img.shields.io/badge/ACL-2025-blue)](https://www.2025.aclweb.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-yellow)](https://huggingface.co/datasets/AIDC-AI/Marco-Bench-MIF)

⭐ [_**Alibaba International Digital Commerce**_](https://aidc-ai.com) ⭐

:octocat: [**Github**](https://github.com/AIDC-AI/Marco-LLM)  🤗  [**Dataset**](https://huggingface.co/datasets/AIDC-AI/Marco-Bench-MIF) 📝  [**Paper**](https://aclanthology.org/2025.acl-long.1172)

</div>

## Introduction

Marco-Bench-MIF is the first deeply localized multilingual benchmark designed to evaluate instruction-following capabilities across 30 languages. Unlike existing benchmarks that rely primarily on machine translation, Marco-Bench-MIF implements fine-grained cultural adaptations to provide more accurate assessment. Our research demonstrates that machine-translated data underestimates model performance by 7-22% in multilingual environments.


## Key Features

- **Extensive Language Coverage**: 30 languages spanning 6 major language families, including high-resource (English, Chinese, German) and low-resource languages (Yoruba, Nepali)
- **Deep Cultural Localization**: Three-step process of lexical replacement, theme transformation, and pragmatic reconstruction to ensure cultural and linguistic appropriateness
- **Diverse Constraint Types**: 541 instruction-response pairs covering single/multiple constraints, expressive/content constraints, and various instruction types
- **Comparative Dataset**: Machine-translated and culturally-localized versions available for specific languages (Arabic, Chinese, Spanish, etc.) to enable comparative research

## Dataset Access

The dataset is available through our GitHub repository and Hugging Face:

```bash
# Github
git clone https://github.com/AIDC-AI/Marco-Bench-MIF.git

# Huggingface
https://huggingface.co/datasets/AIDC-AI/Marco-Bench-MIF
```


## Key Findings

Our benchmark evaluated 20+ LLM models and revealed:

1. Model scale strongly correlates with performance, with 70B+ models outperforming 8B models by 45-60%
2. A 25-35% performance gap exists between high-resource languages (German, Chinese) and low-resource languages (Yoruba, Nepali)
3. Significant differences between localized and machine-translated evaluations, especially for complex instructions

## Contact

For questions or suggestions, please submit a GitHub issue or contact us:
- Email: lyuchenyang.lcy@alibaba-inc.com
- Project homepage: https://github.com/AIDC-AI/Marco-Bench-MIF

## License

This dataset is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Acknowledgments

Special thanks to all annotators and translators who participated in dataset construction and validation. This project is supported by Alibaba International Digital Commerce Group.

## Citation
```bibtex
@inproceedings{zeng-etal-2025-marco,
  title     = "Marco-Bench-{MIF}: On Multilingual Instruction-Following Capability of Large Language",
  author    = "Zeng, Bo and Lyu, Chenyang and Liu, Sinuo and Zeng, Mingyan and Wu, Minghao and Ni, Xuanfan and Shi, Tianqi and Zhao, Yu and Liu, Yefeng and Zhu, Chenyu and Li, Ruizhe and Geng, Jiahui and Li, Qing and Tong, Yu and Wang, Longyue and Luo, Weihua and Zhang, Kaifu",
  editor    = "Che, Wanxiang and Nabende, Joyce and Shutova, Ekaterina and Pilehvar, Mohammad Taher",
  booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  month     = jul,
  year      = "2025",
  address   = "Vienna, Austria",
  publisher = "Association for Computational Linguistics",
  url       = "https://aclanthology.org/2025.acl-long.1172/",
  doi       = "10.18653/v1/2025.acl-long.1172",
  pages     = "24058--24072",
  ISBN      = "979-8-89176-251-0"
}
```