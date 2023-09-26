import numpy as np
from scipy import stats
from sklearn.metrics import precision_score

# Data Collection
questions = get_questions()

# Experiment Design
np.random.shuffle(questions)
mid = len(questions) // 2
traditional_questions = questions[:mid]
modified_questions = ["Provide the numerical answer to " + q for q in questions[mid:]]

# Run the Experiment
traditional_responses = [ask_question(q) for q in traditional_questions]
modified_responses = [ask_question(q) for q in modified_questions]

# Data Analysis
traditional_precisions = [precision_score(is_relevant(r), r) for r in traditional_responses]
modified_precisions = [precision_score(is_relevant(r), r) for r in modified_responses]

# Statistical Testing
t_stat, p_value = stats.ttest_ind(traditional_precisions, modified_precisions)

# Interpretation and Conclusion
if p_value < 0.05:
    print("Modifying the prompt to explicitly request a concise answer can increase the precision of the responses from the LLM.")
else:
    print("Modifying the prompt does not significantly affect the precision of the responses from the LLM.")