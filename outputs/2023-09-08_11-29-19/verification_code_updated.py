import numpy as np
import scipy.stats as stats

# Data Collection
general_prompts = ["Tell me about the weather", "What's the time?", "How many people live in New York?"]
specific_prompts = ["What's the temperature in Celsius?", "What's the current time in GMT?", "What's the population of New York in 2021?"]

# Mock function: replace this with your actual function
def get_LLM_response(prompt):
    return "This is a mock response"

# Experiment Execution
general_responses = []
specific_responses = []

for prompt in general_prompts:
    response = get_LLM_response(prompt)
    general_responses.append(response)

for prompt in specific_prompts:
    response = get_LLM_response(prompt)
    specific_responses.append(response)

# Data Analysis
def categorize_responses(responses):
    numerical_responses = 0
    for response in responses:
        if response.isdigit():
            numerical_responses += 1
    return numerical_responses

N_G = categorize_responses(general_responses)
N_S = categorize_responses(specific_responses)

# Statistical Testing
# Create a contingency table
contingency_table = np.array([[N_G, len(general_prompts) - N_G], [N_S, len(specific_prompts) - N_S]])

# Perform chi-square test
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# Result Interpretation
if p < 0.05:
    print("Reject the null hypothesis. The specificity of prompts influences the type of response from the LLM.")
else:
    print("Do not reject the null hypothesis. The specificity of prompts does not significantly influence the type of response from the LLM.")