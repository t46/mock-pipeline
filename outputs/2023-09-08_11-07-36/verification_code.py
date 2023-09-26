import random
import numpy as np
from scipy.stats import chi2_contingency

# Step 1: Define the Dataset
dataset = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(1000)]

# Step 2: Define the Scoring System
def score_response(response):
    if isinstance(response, int):
        return 1
    else:
        return 0

# Step 3: Run the Trials
responses = []
for problem in dataset:
    X, Y = problem
    response1 = ask_LLM(f"What is {X} + {Y}?")  # replace ask_LLM with the actual function to ask the LLM
    response2 = ask_LLM(f"Calculate {X} + {Y} and provide the numerical answer only")
    responses.append((response1, response2))

# Step 4: Score the Responses
scores = []
for response1, response2 in responses:
    score1 = score_response(response1)
    score2 = score_response(response2)
    if score2 > score1:
        scores.append(1)  # success for the hypothesis
    else:
        scores.append(0)  # failure for the hypothesis

# Step 5: Analyze the Results
success_rate = np.mean(scores)
print(f"Success rate: {success_rate * 100}%")

# Perform a chi-square test
contingency_table = np.histogram(scores, bins=2)[0]
chi2, p_value, _, _ = chi2_contingency(contingency_table.reshape(-1, 1))
print(f"Chi-square test p-value: {p_value}")

# Step 6: Draw Conclusions
if p_value < 0.05 and success_rate > 0.5:
    print("The results support the hypothesis. Consider implementing the refined prompting strategy in the LLM.")
else:
    print("The results do not support the hypothesis. Consider alternative strategies for improving the directness of the LLM's responses.")