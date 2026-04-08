# IFEval: Multilingual Instruction Following Evaluation

This repository extends the original [IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) with enhanced multilingual support for instruction following evaluation of large language models. This work is part of the [Marco-Bench-MIF](https://arxiv.org/abs/2507.11882) project presented at ACL 2025.

## Features

- **Enhanced Multilingual Support**: Improved support for 30+ languages including Chinese, Arabic, Russian, Japanese, Korean, and more
- **Multi-language Punctuation Support**: Extended punctuation checking for various writing systems
- **Improved Language Detection**: Better handling of mixed-language responses
- **Comprehensive Quote Support**: Support for different quotation mark styles across languages

## Dependencies

Please make sure that all required python packages are installed via:

```bash
pip3 install -r requirements.txt
```

## Quick Start

### 1. Basic Usage

```bash
# Run evaluation on a single file
python3 -m instruction_following_eval.evaluation_main \
  --input_data=./data/your_data.jsonl \
  --input_response_data=./data/your_data.jsonl \
  --output_dir=./output/
```

### 2. Data Format

Your input data should be in JSONL format with the following structure:

```json
{
  "key": 1051,
  "prompt": "Write a message to your friend in lowercase letters and ask him to go vote.",
  "instruction_id_list": ["change_case:english_lowercase", "language:response_language"],
  "kwargs": [{}, {"language": "en"}],
  "response": "hello there! i hope you're doing well. i wanted to ask if you could please go vote in the upcoming election. your vote really matters and can make a difference in our community."
}
```

**Note**: The multilingual evaluation datasets are available separately. Please refer to the [Marco-Bench-MIF data repository](https://github.com/your-username/marco-bench-mif-data) for the complete datasets used in our ACL 2025 paper.

### 3. Batch Processing

```bash
# Process all language files in the data directory
bash run.sh
```

## Supported Languages

This enhanced version supports evaluation in 30+ languages:

- **CJK Languages**: Chinese (Simplified/Traditional), Japanese, Korean
- **Indo-European**: English, Spanish, French, German, Italian, Portuguese, Russian, Polish, Czech, etc.
- **Semitic**: Arabic, Hebrew
- **Other Scripts**: Thai, Bengali, Hindi, Tamil, Telugu, Kannada, Malayalam, etc.

## Key Improvements

### 1. Multilingual Punctuation Support
- Extended comma checking for Chinese (，), Arabic (،), and other languages
- Comprehensive quote support for various writing systems
- Language-specific punctuation rules

### 2. Enhanced Language Detection
- Better handling of mixed-language responses
- Improved accuracy for short text detection
- Support for code-mixed content

### 3. Improved Word Counting
- Character-based counting for CJK languages
- Word-based counting for Latin scripts
- Proper handling of mixed-language text

## Examples

### Arabic Example
```json
{
  "key": 1001,
  "prompt": "اكتب رسالة إلى صديقك بأحرف صغيرة واطلب منه الذهاب والتصويت.",
  "instruction_id_list": ["change_case:english_lowercase", "language:response_language"],
  "kwargs": [{}, {"language": "en"}],
  "response": "hello there! i hope you're doing well..."
}
```

### Chinese Example
```json
{
  "key": 2001,
  "prompt": "请用中文写一篇关于人工智能的文章，不超过800字。",
  "instruction_id_list": ["length_constraints:number_words", "language:response_language"],
  "kwargs": [{"relation": "less than", "num_words": 800}, {"language": "zh-cn"}],
  "response": "人工智能是计算机科学的一个重要分支..."
}
```

## Output

The evaluation generates:
- `results.jsonl`: Detailed evaluation results for each sample
- `summary.json`: Overall statistics and accuracy scores

## Reference

If you use this work, please consider citing both the original IFEval paper and this enhanced version:

**Original IFEval:**
```
@article{zhou2023instruction,
  title={Instruction-Following Evaluation for Large Language Models},
  author={Zhou, Jeffrey and Lu, Tianjian and Mishra, Swaroop and Brahma, Siddhartha and Basu, Sujoy and Luan, Yi and Zhou, Denny and Hou, Le},
  journal={arXiv preprint arXiv:2311.07911},
  year={2023}
}
```

**This Enhanced Version:**
```
@article{zeng2025marco,
  title={Marco-Bench-MIF: On multilingual instruction-following capability of large language models},
  author={Zeng, Bo and Lyu, Chenyang and Liu, Sinuo and Zeng, Mingyan and Wu, Minghao and Ni, Xuanfan and Shi, Tianqi and Zhao, Yu and Liu, Yefeng and Zhu, Chenyu and others},
  journal={arXiv preprint arXiv:2507.11882},
  year={2025}
}
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original IFEval implementation by Google Research
- Enhanced multilingual support and improvements based on the Marco-Bench-MIF work (ACL 2025)
- This repository is part of the Marco-Bench-MIF project for evaluating multilingual instruction-following capabilities