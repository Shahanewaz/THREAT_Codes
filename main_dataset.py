import os
import pandas as pd
from tqdm import tqdm
from prompt_optimizer import optimize_prompt  

def optimize_dataset(input_path, output_path):
    
    # Load the input CSV
    df = pd.read_csv(input_path)
    # df = pd.read_csv(input_path).head(3)
    
    """
    if "question" not in df.columns:
        raise ValueError("Input dataset must contain a 'question' column.")
    """
    
    if "prompt" not in df.columns:
        raise ValueError("Input dataset must contain a 'prompt' column.")

    optimized_questions = []
    safe_gains = []

    # Loop through each prompt and apply optimization
    # for x_init in tqdm(df["question"], desc = "Optimizing Prompts"):
    for x_init in tqdm(df["prompt"], desc = "Optimizing Prompts"):
        try:
            x_best, R_best = optimize_prompt(x_init)
        except Exception as e:
            x_best = f"[ERROR] {str(e)}"
            R_best = None

        optimized_questions.append(x_best)
        safe_gains.append(R_best)

    # Save results to new columns
    df["optimized_question"] = optimized_questions
    df["safe_gain"] = safe_gains

    # Write the updated DataFrame to output
    df.to_csv(output_path, index = False)
    print(f"Optimization complete. Results saved to: {output_path}")

if __name__ == "__main__":
    dir1 = "../../../Results/Safe_version/Gretel-safety-alignment/System_Risks"

    os.makedirs(dir1, exist_ok = True)
    
    input_file = os.path.join(dir1, "sample_dataset.csv")
    output_file = os.path.join(dir1, "optimized_questions.csv")
    
    optimize_dataset(input_file, output_file)
