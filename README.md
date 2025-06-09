This repository contains the codes for THREAT: Targeted Hypergaming via Reframing and Exploitation of Adversarial Tactics

# Folder Structure

```
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
│ ├── Gretel-safety-alignment
│ │ ├── Discrimination
│ │ └── Information_Hazards
│ │ └── System_Risks
│ └── HarmfulQADataset
```

# Code Outline

## Steps

1. Generate the original response (without applying the THREAT framework):

```python generate_response_original.py```

2. Apply the THREAT framework to get the optimized prompts for each original prompt:

```python main_dataset.py```

3. Generate responses for the optimized prompts:

```python generate_response_THREAT.py```

4. Compute refusal counts for original vs. THREAT-derived prompts:

```python compute_refusal.py```

5. Enumerate blue and red reference responses corresponding to each prompt:

```python blue_and_red.py```

6. Assign labels to each response:

```python blue_red_label.py```

# Main Result:

Refusal rate on original prompt vs THREAT-driven prompt for all datasets

| Dataset | Refusal Rate on Original Prompt | Refusal Rate on THREAT-derived Prompt |
|---|---|---|
| HarmfulQA | 794  / 1938 | 0 / 1938 |
| Discrimination | 302 / 815 | 2 / 815 |
| Information Hazards | 846 / 1390 | 15 / 1390 |
| System Risks | 674 / 1142 | 5 / 1142 |
