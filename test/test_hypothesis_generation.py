import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import hypothesis_generation
from langchain.llms import OpenAI
import argparse
import logging
import datetime

warnings.simplefilter('ignore')

def main(args):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/test/problem_discovery/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/problem.txt') as f:
        problem = f.read()
        hypothesis_generator = hypothesis_generation.HypothesisGenerator(llm)
        hypothesis = hypothesis_generator(problem)
    print(hypothesis)
    logging.info('Hypothesis: %s', hypothesis)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_paper", type=str, default='input_data/paper.tex', help="path_to_paper")
    args = parser.parse_args()
    main(args)