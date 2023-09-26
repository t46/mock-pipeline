import random
from sklearn.model_selection import train_test_split
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 1. Data Collection
Q = ["What is the capital of France?", "Who wrote the book '1984'?", "What is the tallest mountain in the world?"]
Q_prime = ["What is the capital of France in one word?", "Who wrote the book '1984' in one word?", "What is the tallest mountain in the world in one word?"]

# 2. Experiment Setup
Q_train, Q_test = train_test_split(Q, test_size=0.2, random_state=42)
Q_prime_train, Q_prime_test = train_test_split(Q_prime, test_size=0.2, random_state=42)

R = []
R_prime = []

# 2.2. Input each question from the training set of Q into the LLM and record the responses
for question in Q_train:
    inputs = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    R.append(response)

# 2.3. Similarly, input each question from the training set of Q' into the LLM and record the responses
for question in Q_prime_train:
    inputs = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    R_prime.append(response)

# 3. Data Analysis
R_lengths = [len(response.split()) for response in R]
R_prime_lengths = [len(response.split()) for response in R_prime]

# 3.2. Calculate the average length of the responses in R and R'
L = sum(R_lengths) / len(R_lengths)
L_prime = sum(R_prime_lengths) / len(R_prime_lengths)

# 3.3. Compare L and L'
print(f"Average length of responses in R: {L}")
print(f"Average length of responses in R_prime: {L_prime}")

# 4. Model Validation
R_test = []
R_prime_test = []

for question in Q_test:
    inputs = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    R_test.append(response)

for question in Q_prime_test:
    inputs = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    R_prime_test.append(response)

R_test_lengths = [len(response.split()) for response in R_test]
R_prime_test_lengths = [len(response.split()) for response in R_prime_test]

L_test = sum(R_test_lengths) / len(R_test_lengths)
L_prime_test = sum(R_prime_test_lengths) / len(R_prime_test_lengths)

print(f"Average length of responses in R_test: {L_test}")
print(f"Average length of responses in R_prime_test: {L_prime_test}")