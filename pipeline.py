from modules import problem_discovery, hypothesis_generation, verification_execution, paper_writing
from langchain.llms import OpenAI
import argparse
import logging
import datetime
import warnings

warnings.simplefilter('ignore')

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.0)

    with open('input_data/problem_2.txt') as f:
        problem = f.read()
        print(problem)
        logging.info('Problem: %s', problem)


    hypothesis_generator = hypothesis_generation.HypothesisGenerator(llm)
    hypothesis = hypothesis_generator(problem)
    print(hypothesis)
    logging.info('Hypothesis: %s', hypothesis)

    del hypothesis_generator

    verification_executor = verification_execution.VerificationExecutor(llm)
    verification_result = verification_executor(problem, hypothesis)
    logging.info('Verification Result: %s', verification_result)

    del verification_executor

    verification_plan = 'TODO: define internally'

    paper_writer = paper_writing.PaperWriter()
    latex_content = paper_writer(problem, hypothesis, verification_plan, verification_result, llm)  # TODO: intermediate_outputs
    print(latex_content)
    logging.info('LaTeX Content: %s', latex_content)

if __name__ == "__main__":
    main()