import random
import scipy.stats as stats

# Step 1: Data Collection
math_questions = [
    # Add your list of mathematical questions here
    # Each question should be a tuple with two elements:
    # The first element is the non-specific version of the question
    # The second element is the specific version of the question
    # For example: ("What is 1 + 1?", "Provide the numerical answer to 1 + 1")
]

# Step 2: Experiment Setup
random.shuffle(math_questions)
half = len(math_questions) // 2
non_specific_questions = [q[0] for q in math_questions[:half]]
specific_questions = [q[1] for q in math_questions[half:]]

# Step 3: Experiment Execution
# Assuming we have a function `ask_question_to_llm` that takes a question as input and returns the LLM's response
def ask_question_to_llm(question):
    # Implement the function to interact with the LLM here
    pass

non_specific_responses = [ask_question_to_llm(q) for q in non_specific_questions]
specific_responses = [ask_question_to_llm(q) for q in specific_questions]

# Step 4: Data Analysis
def is_numerical_response(response):
    return response.strip().isdigit()

non_specific_numerical_responses = sum(is_numerical_response(r) for r in non_specific_responses)
specific_numerical_responses = sum(is_numerical_response(r) for r in specific_responses)

P_N_given_S = specific_numerical_responses / len(specific_responses)
P_N_given_not_S = non_specific_numerical_responses / len(non_specific_responses)

# Step 5: Hypothesis Testing
contingency_table = [[specific_numerical_responses, len(specific_responses) - specific_numerical_responses],
                     [non_specific_numerical_responses, len(non_specific_responses) - non_specific_numerical_responses]]
chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)

# Step 6: Report Results
print(f"P(N|S) = {P_N_given_S}")
print(f"P(N|~S) = {P_N_given_not_S}")
print(f"p-value = {p_value}")

if P_N_given_S > P_N_given_not_S and p_value < 0.05:
    print("The specificity of a question prompt influences the format of the AI model's response.")
else:
    print("The data does not support the hypothesis.")

# Step 7: Review and Refine
# This step is subjective and depends on the results of the experiment and the specific circumstances.