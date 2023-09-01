import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import hypothesis_generation
from langchain.llms import OpenAI
import argparse
import logging
import datetime

warnings.simplefilter('ignore')

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/test/hypothesis_generation/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/problem_2.txt') as f:
        problem = f.read()
        hypothesis_generator = hypothesis_generation.HypothesisGenerator(llm)
        hypothesis = hypothesis_generator(problem)
    print(hypothesis)
    logging.info('Hypothesis: %s', hypothesis)

if __name__ == "__main__":
    main()