import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split

# 1. Data Preparation
data = pd.read_csv('prompts.csv')
train, test = train_test_split(data, test_size=0.5, random_state=42)

# 2. Model Training
train_model(train['prompt'], 'traditional')
train_model(train['prompt'].apply(modify_prompt), 'specific')

# 3. Model Testing
responses_traditional = test_model(test['prompt'], 'traditional')
responses_specific = test_model(test['prompt'].apply(modify_prompt), 'specific')

# 4. Data Collection
word_counts_traditional = responses_traditional.apply(count_words)
word_counts_specific = responses_specific.apply(count_words)

# 5. Data Analysis
average_traditional = np.mean(word_counts_traditional)
average_specific = np.mean(word_counts_specific)

t_stat, p_value = stats.ttest_ind(word_counts_traditional, word_counts_specific)

# 6. Reporting
print(f'Average word count for traditional model: {average_traditional}')
print(f'Average word count for specific model: {average_specific}')
print(f'T-test results: t = {t_stat}, p = {p_value}')

if p_value < 0.05:
    print('The specific model generates more concise responses.')
else:
    print('The specific model does not generate more concise responses.')