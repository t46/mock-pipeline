import numpy as np
from scipy import stats
from transformers import pipeline

# Initialize the LLM
llm = pipeline('text-generation')

# Define the scoring system for directness
def score_directness(response):
    if len(response.split()) == 1:
        return 10
    else:
        return 10 - min(len(response.split()) - 1, 9)

# Prepare the dataset
general_questions = ["What is 1 + 1?", "What is 2 * 2?", "What is 3 - 1?", "What is 4 / 2?"]
specific_questions = ["Provide the numerical answer to 1 + 1", "Provide the numerical answer to 2 * 2", "Provide the numerical answer to 3 - 1", "Provide the numerical answer to 4 / 2"]

# Run the experiment and evaluate the responses
general_scores = []
for question in general_questions:
    response = llm(question)[0]['generated_text']
    general_scores.append(score_directness(response))

specific_scores = []
for question in specific_questions:
    response = llm(question)[0]['generated_text']
    specific_scores.append(score_directness(response))

# Calculate the average directness score
average_general_score = np.mean(general_scores)
average_specific_score = np.mean(specific_scores)

# Compare the results
print(f"Average directness score for general questions: {average_general_score}")
print(f"Average directness score for specific questions: {average_specific_score}")

# Perform a t-test
t_stat, p_val = stats.ttest_ind(general_scores, specific_scores)
print(f"t-statistic: {t_stat}, p-value: {p_val}")

# Document the results
with open("experiment_report.txt", "w") as f:
    f.write(f"Average directness score for general questions: {average_general_score}\n")
    f.write(f"Average directness score for specific questions: {average_specific_score}\n")
    f.write(f"t-statistic: {t_stat}, p-value: {p_val}\n")

# If the results do not support the hypothesis, refine the hypothesis and repeat the experiment
if p_val > 0.05:
    print("The results do not support the hypothesis. Refining the hypothesis and repeating the experiment...")