import random
from sklearn.model_selection import train_test_split
from transformers import pipeline

# Prepare a dataset of mathematical problems
problems = [(f"What is {i} + {j}?", f"Provide the numerical answer to {i} + {j}", i+j) for i in range(50) for j in range(20)]

# Check if the dataset is large enough
assert len(problems) >= 1000

# Divide the dataset into two equal parts
set_A, set_B = train_test_split(problems, test_size=0.5, random_state=42)

# Initialize the language model
llm = pipeline('text-generation')

# Initialize counters for correct responses
correct_responses_A = 0
correct_responses_B = 0

# Iterate over set_A and set_B and generate responses
for problem, _, answer in set_A:
    output = llm(problem)[0]['generated_text']
    if str(answer) in output:
        correct_responses_A += 1

for _, problem, answer in set_B:
    output = llm(problem)[0]['generated_text']
    if str(answer) in output:
        correct_responses_B += 1

# Calculate the percentage of correct responses
percentage_A = correct_responses_A / len(set_A) * 100
percentage_B = correct_responses_B / len(set_B) * 100

# Print the results
print(f"Percentage of correct responses for Set A (original prompts): {percentage_A}%")
print(f"Percentage of correct responses for Set B (modified prompts): {percentage_B}%")

# Compare the results
if percentage_B > percentage_A:
    print("The modified prompts resulted in a higher percentage of correct responses, supporting the hypothesis.")
else:
    print("The modified prompts did not improve the accuracy, not supporting the hypothesis.")