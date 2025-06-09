import pandas as pd
import os

# Load the CSV file
dir1 = "../HarmfulQADataset"
df = pd.read_csv(os.path.join(dir1, "harmfulqa.csv"))

dir2 = "../Results/HarmfulQADataset"
df2 = pd.read_csv(os.path.join(dir2, "responses_with_refusal_flag.csv"))

# Clean 'conversation_type' values and drop rows with missing text
df['conversation_type'] = df['conversation_type'].str.replace('_conversations', '', regex = False)
df = df.dropna(subset = ['value'])

# Filter GPT responses excluding "you're welcome"
gpt_df = df[
    (df['from'] == 'gpt') &
    (~df['value'].str.lower().str.contains("you're welcome"))
]

# Separate by conversation type

blue_grouped = gpt_df[gpt_df['conversation_type'] == 'blue'].groupby('id')['value'].apply(list)
red_grouped = gpt_df[gpt_df['conversation_type'] == 'red'].groupby('id')['value'].apply(list)

df2['blue_gpt_responses'] = df2['id'].map(blue_grouped)
df2['red_gpt_responses'] = df2['id'].map(red_grouped)

# Replace NaN with empty list
df2['blue_gpt_responses'] = df2['blue_gpt_responses'].apply(lambda x: x if isinstance(x, list) else [])
df2['red_gpt_responses'] = df2['red_gpt_responses'].apply(lambda x: x if isinstance(x, list) else [])

df2.to_csv(os.path.join(dir2, "responses_with_blue_and_red_responses.csv"), index = False)
