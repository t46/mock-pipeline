import csv
import random
import statsmodels.api as sm
import nltk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

# Step 1: Define Scope
# N/A

# Step 2: Prepare the Dataset
prompts = []
for i in range(100):
    prompt_specificity = random.random() # Random float from 0 to 1
    prompts.append(("Prompt "+str(i), prompt_specificity))

# Step 3: Implement the Language Model
def generate_response(prompt):
    text = nltk.word_tokenize(prompt)
    return random.choice(nltk.pos_tag(text))[0] # Return a random word from the prompt

# Step 4: Evaluate the Output
def evaluate_unrelated(response):
    return len(nltk.sent_tokenize(response)) # Count the number of sentences in a reply

# Step 5: Data Collection
data = []
for prompt, specificity in prompts:
    response = generate_response(prompt)
    unrelated = evaluate_unrelated(response)
    data.append((specificity, unrelated))

# Write to CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Step 6: Statistical Analysis
X = [[i[0]] for i in data]
Y = [[i[1]] for i in data]

# Splitting the data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, Y_train)

# Step 7: Hypothesis Testing
coeff_df = pd.DataFrame(model.coef_, columns=['Coefficient'])  
print(coeff_df)

# Step 8: Interpret Results
# N/A

# Step 9: Documentation and Reporting
# N/A