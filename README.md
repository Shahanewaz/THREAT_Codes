This repository contains the codes for THREAT: Targeted Hypergaming via Reframing and Exploitation of Adversarial Tactics

<p align="center">
  <img src="Figures/THREAT_framework_example.png" alt="An example of THREAT framework" width="65%">
</p>

*Figure 1. A harmful prompt from the HarmfulQA dataset can be reframed to evade safety filters while preserving adversarial intent, leading to an unintended model response.*

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

<p align="center">
  <code>python generate_response_original.py</code>
</p>

2. Apply the THREAT framework to get the optimized prompts for each original prompt:

<p align="center">
  <code>python python main_dataset.py</code>
</p>

3. Generate responses for the optimized prompts:

<p align="center">
  <code>python generate_response_THREAT.py</code>
</p>

4. Compute refusal counts for original vs. THREAT-derived prompts:

<p align="center">
  <code>python compute_refusal.py</code>
</p>

5. Enumerate blue and red reference responses corresponding to each prompt:

<p align="center">
  <code>python blue_and_red.py</code>
</p>

6. Assign labels to each response:

<p align="center">
  <code>python blue_red_label.py</code>
</p>

# Main Result:

# Comparison of Refusal Rates: Baseline vs. THREAT-Optimized Prompts
<div align="center">

| Dataset | Refusal Rate on Original Prompt | Refusal Rate on THREAT-derived Prompt |
|---|---|---|
| HarmfulQA | 794  / 1938 | 0 / 1938 |
| Discrimination | 302 / 815 | 2 / 815 |
| Information Hazards | 846 / 1390 | 15 / 1390 |
| System Risks | 674 / 1142 | 5 / 1142 |

</div>

The corresponding bar plot is shown below:

<div align="center">
  
![Refusal Bar Plot](Figures/refusal_rate.PNG)

</div>

*Figure 2. Refusal rates (original vs.\ THREAT) on four different safety‐benchmark datasets: (i) discrimination, (ii) information hazards, (iii) safety risks and (iv) harmfulQA. Each bar indicates the percentage (and absolute count) of prompts that GPT-4o refused to answer under each prompting strategy.*

# Comparative Score Distribution: Red and Blue Label
<div align="center">
  
![Average Red and Blue Score](Figures/red_blue_score.PNG)

</div>

*Figure 3. Average similarity scores for generated responses on the Discrimination dataset, grouped by predicted label. The left panel shows the mean blue score for examples labeled “Blue" versus “Red," and the right panel shows the mean red score for the same two groups.*

The Jensen–Shannon divergence (JSD) between red-score and blue-score distributions for each dataset, quantifying the degree of separation between unsafe and safe alignment scores is given below:

<div align="center">
  
| Dataset | JSD |
|---|---|
| HarmfulQA | 0.692 |
| Discrimination | 0.603 |
| Information Hazards | 0.572 |
| System Risks | 0.653 |

</div>

# Refusal Count as a Function of Red–Blue Score Difference

<p align="center">
  <img src="Figures/refusal_by_diff_bins_HarmfulQADataset.png" alt="HarmfulQA" width="45%" />
  <img src="Figures/refusal_by_diff_bins_Gretel-safety-alignment_System_Risks.png" alt="System Risks" width="45%" />
</p>

*Figure 4: Refusal counts for the original prompts, categorized by intervals of the difference between red‐ and blue‐scores; the values displayed above each bar indicate the corresponding refusal counts for our THREAT‐derived prompts.*

# Distribution of Safety Reward Gain by Label

<div align="center">
  
![Box Plot by Label](Figures/safe_gain_by_label_HarmfulQADataset.png)

</div>

*Figure 5: Boxplots of overall reward safety gains classified by predicted label on the HarmfulQA dataset. Notably, "Blue" predictions exhibit a higher median overall reward safety gain, whereas "Red" predictions display a lower median.*

# Distribution of Red and Blue Predictions by Judge Response Score

<div align="center">
  
![Box Plot by Label](Figures/red_blue_percentage_Gretel-safety-alignment_System_Risks.png)

</div>

*Figure 6: Distribution of Red and Blue Predictions by Judge Response Score in the System Risks Dataset. As the judge-assigned score increases, the proportion of Red predictions decreases, with low scores corresponding predominantly to Red responses and higher scores yielding a more balanced distribution between Red and Blue classifications.*
