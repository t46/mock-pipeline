import openai
import numpy as np
from scipy import stats

# 1. Data Collection
questions = ["What is the capital of France?", "Who wrote 'To Kill a Mockingbird'?", "What is the square root of 16?"]
modified_questions = ["Give a direct answer: " + q for q in questions]

# 2. Model Testing
def get_response(prompt):
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60)
    return response.choices[0].text.strip()

original_responses = [get_response(q) for q in questions]
modified_responses = [get_response(q) for q in modified_questions]

# 3. Data Analysis
def response_analysis(original_responses, modified_responses):
    original_lengths = [len(r.split()) for r in original_responses]
    modified_lengths = [len(r.split()) for r in modified_responses]
    
    original_directness = [1 if r.split()[0] in q else 0 for r, q in zip(original_responses, questions)]
    modified_directness = [1 if r.split()[0] in q else 0 for r, q in zip(modified_responses, modified_questions)]
    
    return original_lengths, modified_lengths, original_directness, modified_directness

original_lengths, modified_lengths, original_directness, modified_directness = response_analysis(original_responses, modified_responses)

# 4. Statistical Analysis
length_ttest = stats.ttest_rel(original_lengths, modified_lengths)
directness_ttest = stats.ttest_rel(original_directness, modified_directness)

# 5. Conclusion
if length_ttest.pvalue < 0.05 and directness_ttest.pvalue < 0.05:
    print("The hypothesis is verified.")
else:
    print("The hypothesis is not verified.")