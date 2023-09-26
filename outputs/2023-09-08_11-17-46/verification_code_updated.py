import random
import scipy.stats as stats

# Step 1: Data Collection
questions = [
    # Add your questions here
    # Example: 
    # {"original": "What is 1 + 1?", "modified": "Provide a one-word answer: What is 1 + 1?"}
]

# Step 2: Experiment Setup
random.shuffle(questions)
group_A = questions[:len(questions)//2]
group_B = questions[len(questions)//2:]

# Step 3: Execution
# Assuming we have a function `get_LLM_response(prompt)` that inputs a prompt into the LLM and returns the response
responses_A = [(q["original"], get_LLM_response(q["original"])) for q in group_A]
responses_B = [(q["modified"], get_LLM_response(q["modified"])) for q in group_B]

# Step 4: Data Analysis
# Assuming we have a function `is_direct_response(question, response)` that determines whether a response is direct
direct_responses_A = sum(is_direct_response(q, r) for q, r in responses_A)
direct_responses_B = sum(is_direct_response(q, r) for q, r in responses_B)

P1 = direct_responses_A / len(group_A) if group_A else None
P2 = direct_responses_B / len(group_B) if group_B else None

# Step 5: Hypothesis Testing
# Using a z-test for proportions
if P1 is not None and P2 is not None:
    z, p = stats.proportions_ztest([direct_responses_A, direct_responses_B], [len(group_A), len(group_B)], alternative='smaller')

    # Step 6: Reporting
    print(f"Proportion of direct responses in Group A: {P1}")
    print(f"Proportion of direct responses in Group B: {P2}")
    print(f"Z-statistic: {z}")
    print(f"P-value: {p}")

    if p < 0.05:
        print("Reject the null hypothesis. There is evidence to suggest that modifying the prompt structure results in a higher proportion of direct responses.")
    else:
        print("Do not reject the null hypothesis. Modifying the prompt structure does not significantly affect the proportion of direct responses.")
else:
    print("Not enough data to perform the z-test.")