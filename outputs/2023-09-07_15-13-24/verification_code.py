import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.feature_extraction.text import CountVectorizer
from openai import GPT3

# Define scoring system for specificity and relevance
def specificity_score(prompt):
    vectorizer = CountVectorizer().fit_transform([prompt])
    vectors = vectorizer.toarray()
    return np.sum(vectors)

def relevance_score(prompt, response):
    prompt_words = prompt.split()
    response_words = response.split()
    return len(set(prompt_words) & set(response_words))

# Create a dataset of prompts
prompts = ["What is 1 + 1?", 
           "Calculate 1 + 1 and provide only the numerical answer", 
           "Who won the world series in 2020?", 
           "Provide the name of the team that won the world series in 2020", 
          ]

# Initialize GPT-3 model
model = GPT3()

# Generate responses and score specificity and relevance
specificity_scores = []
relevance_scores = []
responses = []
for prompt in prompts:
    response = model.generate(prompt)
    responses.append(response)
    specificity_scores.append(specificity_score(prompt))
    relevance_scores.append(relevance_score(prompt, response))

# Analyze the results
correlation, _ = pearsonr(specificity_scores, relevance_scores)
print(f'Correlation between specificity and relevance: {correlation}')

# Report the results
results = pd.DataFrame({
    'Prompt': prompts,
    'Response': responses,
    'Specificity Score': specificity_scores,
    'Relevance Score': relevance_scores
})

print(results)