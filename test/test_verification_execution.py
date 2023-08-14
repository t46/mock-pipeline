import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import verification_execution
from langchain.llms import OpenAI
import argparse
import logging
import datetime

warnings.simplefilter('ignore')

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/test/problem_discovery/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/hypothesis.txt') as f:
        problem = f.read()
        verification_executor = verification_execution.VerificationExecutor(llm)
        verification_executor(problem, llm)

if __name__ == "__main__":
    main()