import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def is_direct_response(response, answer):
    return response.strip().lower() == answer.strip().lower()

questions = ["What is 1 + 1?", "What is the capital of France?", "Who wrote 'To Kill a Mockingbird'?", "What is the chemical symbol for gold?"]
answers = ["2", "Paris", "Harper Lee", "Au"]

general_questions = questions
specific_questions = ["Provide the numerical answer for 1 + 1", "Name the capital city of France", "Name the author of 'To Kill a Mockingbird'", "Provide the chemical symbol for gold"]

def ask_llm(question):
    return "Placeholder response"

general_responses = [ask_llm(q) for q in general_questions]
specific_responses = [ask_llm(q) for q in specific_questions]

general_directness = [is_direct_response(r, a) for r, a in zip(general_responses, answers)]
specific_directness = [is_direct_response(r, a) for r, a in zip(specific_responses, answers)]

general_direct_proportion = np.mean(general_directness)
specific_direct_proportion = np.mean(specific_directness)

contingency_table = pd.crosstab(index=[general_directness, specific_directness], columns=["counts"])
chi2, p, dof, expected = chi2_contingency(contingency_table)

if p < 0.05:
    print("The specific prompt format is more likely to result in a direct response.")
else:
    print("The specific prompt format does not significantly affect the directness of responses.")