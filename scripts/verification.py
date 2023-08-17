import time
import openai
from datetime import datetime

def verify_prompt_strategy():
    # Selecting the Language Model
    model = "text-davinci-002"

    # Data Preparation
    control_tasks = ["What is 123 + 456?", "Calculate 789 * 123", "What is the square root of 144?"]
    experimental_tasks = ["What is 321 + 654?", "Calculate 987 * 321", "What is the square root of 169?"]

    # Running the Control Condition
    control_results = []
    control_start_time = datetime.now()

    for task in control_tasks:
        response = openai.Completion.create(engine=model, prompt=task, max_tokens=60)
        control_results.append(response.choices[0].text.strip())
        
    control_end_time = datetime.now()
    T1 = (control_end_time - control_start_time).total_seconds()

    # Implementing the Prompt Strategy
    prompt_strategy = "Please provide the answer as a numerical figure only."

    # Running the Experimental Condition
    experimental_results = []
    experimental_start_time = datetime.now()

    for task in experimental_tasks:
        response = openai.Completion.create(engine=model, prompt=f"{task}\n{prompt_strategy}", max_tokens=60)
        experimental_results.append(response.choices[0].text.strip())
        
    experimental_end_time = datetime.now()
    T2 = (experimental_end_time - experimental_start_time).total_seconds()

    # Analysing the Results
    percentage_reduction = ((T1 - T2) / T1) * 100

    # Documenting the Results
    print(f"Control tasks results: {control_results}")
    print(f"Experimental tasks results: {experimental_results}")
    print(f"Percentage reduction in post-processing time: {percentage_reduction}%")

# Repeating the Experiment
# This function can be called multiple times with different sets of mathematical tasks
verify_prompt_strategy()