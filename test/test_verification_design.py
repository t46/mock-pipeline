import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import verification_design
from langchain.llms import OpenAI
import logging
import datetime

warnings.simplefilter('ignore')

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/test/verification_design/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/problem.txt') as f1:
        with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/hypothesis.txt') as f2:
            problem = f1.read()
            hypothesis = f2.read()
            verification_design.design_verification_plan(problem, hypothesis, llm)

if __name__ == "__main__":
    main()