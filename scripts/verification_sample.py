import openai
import json


def generate_prompt(question):
    prompt = f"{question}\n"
    return prompt

def check_correctness(answer, response):
    return (answer == response.choices[0].text.strip())

def verification_criterion(correct_answer_original, correct_answer_proposition):
    return bool(correct_answer_original < correct_answer_proposition)

with open('input_data/sample_data.jsonl', 'r') as file:
    correct_answer_original = 0
    correct_answer_proposition = 0
    total = 0
    data = json.loads(file.__next__())
    question = data["question"]
    answer = data["answer"]

    response_original = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Q: {question}\n"
        )
    response_proposition = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Q: {question}\n Constraint: Extract only the direct answer from the response without any additional words."
        )

    correct_answer_original += check_correctness(answer, response_original)
    correct_answer_proposition += check_correctness(answer, response_proposition)

print(f"Hypothesis is {verification_criterion(correct_answer_original, correct_answer_proposition)}")


        


