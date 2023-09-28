import numpy as np
from scipy import stats
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the Scoring Function
def scoring_function(response, prompt):
    vectorizer = TfidfVectorizer().fit_transform([response, prompt])
    cosine = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
    return cosine[0][0]

# Define the Response Generation Function
def generate_response(prompt):
    # For now, simply return the prompt as the response
    # Replace this with your own logic for generating a response
    return prompt

# Prepare the Dataset
prompts = ["What is 1 + 1?", "Calculate 1 + 1 and provide only the numerical answer."] 
correct_responses = ["2", "2"] 

# Generate responses
responses = [generate_response(prompt) for prompt in prompts]

# Score the Responses
scores = [scoring_function(response, prompt) for response, prompt in zip(responses, prompts)]

# Test the responses
successful_tests = 0
for i in range(0, len(prompts), 2):
    if scores[i+1] > scores[i]:
        successful_tests += 1

# Analyze the Results
percentage_successful = (successful_tests / (len(prompts) / 2)) * 100
print(f"Percentage of successful test cases: {percentage_successful}%")

# Perform a paired t-test
t_statistic, p_value = stats.ttest_rel(scores[::2], scores[1::2])
print(f"Paired t-test p-value: {p_value}")

# Draw Conclusions
if percentage_successful > 50 and p_value < 0.05:
    print("The specificity and clarity of prompts given to a Language Model significantly influence the relevance of its generated responses.")
else:
    print("The evidence does not support the hypothesis.")