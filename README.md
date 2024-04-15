fork of https://github.com/dair-iitd/jeebench

# JEEBench(EMNLP 2023)

Repository for Course Project of CS-678 by Ali and Anjan. Paper chosen to replicate is: "Have LLMs Advanced Enough? A
Harder Problem Solving Benchmark For Large Language Models" accepted in EMNLP 2023 as a Main conference
paper. https://aclanthology.org/2023.emnlp-main.468/

![respresentative](https://github.com/dair-iitd/jeebench/assets/45387992/d0d14064-bce9-4b58-ac3f-87fef18fcff3)

## Dataset

To access the dataset, unzip the dataset.zip file. This contains the dataset, few-shot examples and responses collected
from GPT models along with extracted answers.
The dataset contains questions from Physics, Chemistry and Mathematics collected from JEE Advanced 2016 to 2023. The
breakdown with respect to subject type and response type is as follows:

<img src="https://github.com/dair-iitd/jeebench/assets/45387992/592af8bc-6a5f-457e-a8d8-806046e0463a" alt="drawing" width="500"/>

## Folder Directory Structure

```bash

D:.
├───data
│   └───responses
│       ├───GPT3.5_normal_responses
│       ├───GPT3_normal_responses
│       ├───GPT4_0613_normal_responses
│       ├───GPT4_CoT+OneShot_responses
│       ├───GPT4_CoT+SC_responses
│       │   └───marks_dump
│       ├───GPT4_CoT_responses
│       ├───GPT4_CoT_self_refine_responses
│       └───GPT4_normal_responses
├───responses
│   ├───GPT3.5_normal_responses
│   └───GPT4_0613_normal_responses
└───results
```

## How did we run the code

As it turns out, the code uses teh responses that the author already had with him to generate the results. This led to giving the same results every single time. We generated new answers to the question prompts and used them but were only able to use 114 questions since OpenAI rate limited us and the cost that incurred were significant.

We then edited the code to run only 114 questions on each model and ended up getting roughly close values.

## How to run the code?

### Set environment variable for OPENAI_API_KEY

For macOS/Linux

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
```

For Windows Powershell

```bash
$env:OPENAI_API_KEY="your_openai_api_key_here"
```

### General Command Structure

Here is the general form of the command to run the inference script:

```bash
python inference.py --model [model_name] --mode [mode] --max_questions [number] --num_procs [number]
```

--model: Specifies the model name.<br />
--mode: Sets the mode of operation ('normal' or 'CoT' for Chain of Thought).<br />
--max_questions: Limits the number of questions to process.<br />
--num_procs: Sets the number of processes for parallel execution.<br />

#### Running GPT-3.5 Turbo in Chain of Thought Mode:

```bash
python inference.py --model gpt-3.5-turbo --mode CoT --max_questions 1 --num_procs 2
```

#### Running GPT-3.5 Turbo in Normal Mode:

```bash
python inference.py --model gpt-3.5-turbo --mode normal --max_questions 10 --num_procs 4
```

#### Running GPT-4 Model in Normal Mode:

```bash
python inference.py --model gpt-4-0613 --mode normal --max_questions 10 --num_procs 4
```

### Evaluating Results

```bash
python compute_metrics.py
```

This script will compute the relevant metrics for your model's output. Ensure your results data is formatted correctly
as expected by compute_metrics.py.

## Results

Upon evaluating results, the results calculated seemed to exactly match the findings of the original authors showing
that OpenAI's GPT-4 would roughly rank around the top 20% in the JEE Advanced of 2023

![image](https://github.com/dair-iitd/jeebench/assets/45387992/3d79ba50-d4a3-4ba5-9a84-32b74ae5a887)

## Citation

If you use our dataset in your research, please cite it using the following

```latex
@inproceedings{arora-etal-2023-llms,
    title = "Have {LLM}s Advanced Enough? A Challenging Problem Solving Benchmark For Large Language Models",
    author = "Arora, Daman  and
      Singh, Himanshu  and
      {Mausam}",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.468",
    doi = "10.18653/v1/2023.emnlp-main.468",
    pages = "7527--7543",
    abstract = "The performance of large language models (LLMs) on existing reasoning benchmarks has significantly improved over the past years. In response, we present JEEBench, a considerably more challenging benchmark dataset for evaluating the problem solving abilities of LLMs. We curate 515 challenging pre-engineering mathematics, physics and chemistry problems from the highly competitive IIT JEE-Advanced exam. Long-horizon reasoning on top of deep in-domain knowledge is essential for solving problems in this benchmark. Our evaluation on various open-source and proprietary models reveals that the highest performance, even after using techniques like self-consistency, self-refinement and chain-of-thought prompting, is less than 40{\%}. The typical failure modes of GPT-4, the best model, are errors in algebraic manipulation, difficulty in grounding abstract concepts into mathematical equations accurately and failure in retrieving relevant domain-specific concepts. We also observe that by mere prompting, GPT-4 is unable to assess risk introduced by negative marking for incorrect answers. For this, we develop a post-hoc confidence-thresholding method over self-consistency, which enables effective response selection. We hope that our challenging benchmark will guide future re-search in problem-solving using LLMs.",
}
```

