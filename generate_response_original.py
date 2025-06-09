import pandas as pd
import os
import openai
from tqdm import tqdm

# Set your OpenAI API key
openai.api_key = ""  

# Define your directory
dir = "../Results/Safe_version/Gretel-safety-alignment/System_Risks"

# Load the dataframe
df = pd.read_csv(os.path.join(dir, "optimized_questions.csv"), encoding = 'ISO-8859-1')

# Function to get response from OpenAI
def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-4o",  
            messages = [{"role": "user", "content": prompt}],
            temperature = 0.8,
            top_p = 0.95,
            max_tokens = 512
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Create a new column for responses
responses = []

# Loop through the prompts using tqdm for progress bar

for prompt in tqdm(df['question'], desc = "Generating Responses"):
    response = get_response(prompt)
    responses.append(response)

# Add the responses to the dataframe
df['original_response'] = responses

# Save updated dataframe
df.to_csv(os.path.join(dir, "dataset_with_original_response.csv"), index = False)
