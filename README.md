This repository contains the codes for THREAT: Targeted Hypergaming via Reframing and Exploitation of Adversarial Tactics

## Folder Structure

├── Code
│ ├── attack_framework.py
│ └── blue_and_red.py
│ └── blue_red_label.py
│ └── compute_refusal.py
│ └── generate_response_THREAT.py
│ └── generate_response_original.py
│ └── llm_generation.py
│ └── main_dataset.py
│ └── prompt_optimizer.py
│ └── single_step_attack.py
│ └── utils.py
├── Result
│ ├── App.js
│ └── utils
│ └── helpers.js

The main code is main_dataset.py. The required command is: ```python main_dataset.py```

Main Result:

Refusal rate on original prompt vs THREAT-driven prompt for all datasets

| Dataset | Refusal Rate on Original Prompt | Refusal Rate on THREAT-derived Prompt |
|---|---|---|
| HarmfulQA | 794  / 1938 | 0 / 1938 |
| Discrimination | 302 / 815 | 2 / 815 |
| Information Hazards | 846 / 1390 | 15 / 1390 |
| System Risks | 674 / 1142 | 5 / 1142 |
