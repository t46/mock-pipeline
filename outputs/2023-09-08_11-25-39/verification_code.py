import numpy as np
import scipy.stats as stats
from transformers import pipeline

# Initialize the language model
llm = pipeline('text-generation')

# Define the dataset
problems = ['1 + 1', '2 * 2', '3 - 1', '4 / 2', '5 ^ 2']
direct_prompts = [f'Provide the numerical result of {problem}' for problem in problems]
open_prompts = [f'What is {problem}?' for problem in problems]

# Generate responses
direct_responses = [llm(prompt)[0]['generated_text'] for prompt in direct_prompts]
open_responses = [llm(prompt)[0]['generated_text'] for prompt in open_prompts]

# Define a function to evaluate directness
def evaluate_directness(response):
    return len(response.split())

# Evaluate the directness of each response
directness_direct = [evaluate_directness(response) for response in direct_responses]
directness_open = [evaluate_directness(response) for response in open_responses]

# Compare the directness using a paired t-test
t_stat, p_val = stats.ttest_rel(directness_direct, directness_open)

# Draw conclusions
if p_val < 0.05:
    print('The responses to the direct prompts are significantly more direct than the responses to the open-ended prompts.')
else:
    print('There is no significant difference in directness between the responses to the direct prompts and the open-ended prompts.')

# Document the results
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_val}')
print('Directness of direct responses:', directness_direct)
print('Directness of open responses:', directness_open)