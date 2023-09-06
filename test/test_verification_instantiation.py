import sys
sys.path.append('/Users/shiro/autoresearch/mock-pipeline')
import warnings
from modules import verification_instantiation
from langchain.llms import OpenAI
import logging
import datetime

warnings.simplefilter('ignore')

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/test/verification_instantiation/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('/Users/shiro/autoresearch/mock-pipeline/test/sample-data/verification_plan.txt') as f:
        verification_plan = f.read()
        verification_instantiation.instantiate_verification_plan(verification_plan, llm)

if __name__ == "__main__":
    main()