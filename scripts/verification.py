import openai
import pandas as pd

# Set the model and temperature
model = 'gpt-4'
temperature = 0.0

# Define the inputs
inputs = ['What is the capital of France?', 'Tell me a joke.', 'Write a short story about a brave knight.', 'What is your opinion on climate change?', 'Translate "Hello" to Spanish.']

# Define a function to run the test
def run_test(inputs):
    outputs = []
    for i in inputs:
        response = openai.ChatCompletion.create(model=model, messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": i}], temperature=temperature)
        outputs.append(response['choices'][0]['message']['content'])
    return outputs

# Run the initial test
initial_outputs = run_test(inputs)

# Define the number of test rounds
test_rounds = 10
all_outputs = []

# Run the test for the specified number of rounds
for i in range(test_rounds):
    outputs = run_test(inputs)
    all_outputs.append(outputs)

# Create a DataFrame with the outputs
df = pd.DataFrame(all_outputs, columns=inputs)

# Calculate the consistency of the outputs
consistency = df.nunique() == 1
consistency_percentage = (consistency.sum() / len(consistency)) * 100

# Print the conclusion based on the consistency of the outputs
if consistency_percentage == 100:
    print('The model produces deterministic and consistent outputs.')
else:
    print('The model does not produce consistent outputs. Further investigation is needed.')