# Overview

This repository contains instructions on how to set up the code for the challenge which is part of our 
[2nd workshop on Multi-Modal Foundation Models](https://sites.google.com/view/2nd-mmfm-workshop/home?authuser=0) 
to appear as a part of 
the [CVPR 2024](https://cvpr.thecvf.com/) program. 
For other details on the challenge, we refer to the
[challenge website](https://sites.google.com/view/2nd-mmfm-workshop/challenge?authuser=0).

For detailed instructions on how to setup the codebase and all the environments, and setup the code for evaluation, please read through these separate instructions:

1. [Installation](docs/installation.md)
2. [Data Download](docs/download.md)
3. [Evaluation](docs/evaluation.md)
4. [Training](docs/training.md)

# Rules

### General Rules
- To be eligible for participation in our challenge, you must register by sending an email to the organizers (please see the contact email below).
- For all submission, the participants will be required to submit their code and the model weights with the instructions on how to reproduce the results. The winners of the competition will be required to open source their code under MIT or more permissive licence. 

### Challenge Phases
- The challenge will be running in two phases: 
  - Phase 1: The participants will submit their results on the test sets which is already present in `data/pre_processed` for all datasets.
  - Phase 2: An alien test set will be released after the phase 1 deadline. The participants will be required to submit their results on the alien test set. Again, with the code and the model weights. 
  - The model submitted for Phase 2 shall reproduce the results of Phase 1. This is stipulated in order to discourage people from overfitting on the test set. An immediate *disqualification* will be in place if the results of Phase 2 are not reproducible from the model submitted in Phase 1.
  - There is a 40% weightage for Phase 1 and 60% weightage for Phase 2.
  - Only participants that submitted results for Phase 1 before its deadline will receive access to Phase 2 evaluation data, and only participants that submitted Phase 2 results will be eligible for the competition.
  - Phase 2 is intended only for evaluating a model finalized in Phase 1, no model modification is allowed for Phase 2 (it should exactly reproduce Phase 1 evaluation).

### Metric
  The evaluation metric agreed upon by the organizers is: 

      Dataset Result = (performance of submitted model - performance of leading baseline) / (distance of leading baseline to 100%)
  the overall score will be computed as an average over the individual dataset results.

### Open Source Models
For eligibility to win the prize money, the participants are required to open source their code and the model weights. 
For participants who submit results with closed-source models, the organizers will not be 
able to consider them for the prize money. This is to ensure that the organizers can verify the results and the code.
All submitted results would be documented in a leaderboard, closed-source results will be marked.

# Important Dates
- Initial registration deadline: 
- Phase 1 deadline:
- Phase 2 deadline:
- Announcement of winners:



# Prize Money

The top 3 performers will be declared as the challenge winners and receive a money award. Details of the award will be disclosed soon! 

The three winners will also be invited for spotlight talks at the workshop. Details will 
be shared with the winners after the challenge conclusion and before the workshop date.

# Baselines
Here we provide three baselines for the challenge by training the LLAVA-1.5 model on three types of data, and we provide the results obtained from the 
resulting model on the test sets of the 10 datasets which contain 200 randomly sampled from the original `validation split` of the dataset. 
Due to the nature of the datasets, we evaluate the models with two metrics (and report the Accuracy %): 
- The [MMMU metric](https://arxiv.org/abs/2311.16502). Used for 6 datasetes: `iconqa_fill, funsd, iconqa_choose, wildreceipt, textbookqa, tabfact`
- Using Mixtral as a judge to evaluate the outputs of the models. Used for 4 datasets: `docvqa, inforgraphicsvqa, websrc`


### Model trained on the LLAVA dataset only:

- MMMU Evaluation 

| Iconqa-Fill | Funsd | Iconqa-Choose | Wildreceipt | Textbookqa | Tabfact | Average |
|-------------|-------|---------------|-------------|------------|---------|---------|
| 14.0        | 34.5  | 31.0          | 35.0        | 52.5       | 48.5    | 35.9    |

- Mixtral Evaluation

| DocVQA | InfographicsVQA | WebSRC | WTQ | Average |
|--------|-----------------|--------|-----|---------|
| 22.5   | 20.5            | 29.5   | 8.0 | 20.1    |



### Model trained on the train sets of the 10 datasets:

- MMMU Evaluation 

| Iconqa-Fill | Funsd | Iconqa-Choose | Wildreceipt | Textbookqa | Tabfact | Average |
|-------------|-------|---------------|-------------|------------|---------|---------|
| 36.0        | 81.0  | 53.0          | 87.0        | 61.0       | 59.5    | 62.9    |

- Mixtral Evaluation

| DocVQA | InfographicsVQA | WebSRC | WTQ  | Average |
|--------|-----------------|--------|------|---------|
| 38.0   | 30.0            | 36.5   | 22.5 | 31.8    |

### Model trained with LLAVA and the train sets of the 10 datasets:

- MMMU Evaluation 

| Iconqa-Fill | Funsd | Iconqa-Choose | Wildreceipt | Textbookqa | Tabfact | Average |
|-------------|-------|---------------|-------------|------------|---------|---------|
| 45.5        | 80.5  | 52.0          | 88.5        | 68.5       | 57.5    | 65.4    |

- Mixtral Evaluation

| DocVQA | InfographicsVQA | WebSRC | WTQ  | Average |
|--------|-----------------|--------|------|---------|
| 35.0   | 29.0            | 40.5   | 22.0 | 31.6    |

# Disclaimer
The organizers reserve the right to disqualify any participant who is found to be in violation of the rules of the challenge. 
The organizers also reserve the right to modify the rules of the challenge at any time.

# Contact
For any questions, please write an email to the organizers, a team member will get back to you as soon as possible:

[contactmmfm2024@gmail.com](contactmmfm2024@gmail.com).

