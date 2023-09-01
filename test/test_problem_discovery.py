import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import problem_discovery
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

    paper = args.path_to_paper
    problem_discoverer = problem_discovery.ProblemDiscoverer(llm)
    problem = problem_discoverer(paper)
    print(problem)
    logging.info('Problem: %s', problem)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_paper", type=str, default='input_data/problem.txt', help="path_to_paper")
    args = parser.parse_args()
    main(args)