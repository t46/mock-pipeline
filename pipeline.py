from modules import problem_discovery, hypothesis_generation, verification_execution, paper_writing
from langchain.llms import OpenAI
import argparse
import logging
import datetime
import warnings

warnings.simplefilter('ignore')

def main(args):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.9)  # TODO: define internally
    verification_result = 'False'

    # NOTE: for now, we assume that the problem is given as an input
    # paper = args.path_to_paper
    # problem_discoverer = problem_discovery.ProblemDiscoverer(llm)
    # problem = problem_discoverer(paper)
    # print(problem)
    # logging.info('Problem: %s', problem)

    # del problem_discoverer
    with open('input_data/problem.txt') as f:
        problem = f.read()
        print(problem)
        logging.info('Problem: %s', problem)

    cnt = 0

    while 'False' in verification_result:

        hypothesis_generator = hypothesis_generation.HypothesisGenerator(llm)
        if cnt == 0:
            hypothesis = hypothesis_generator(problem)
        else:
            hypothesis = hypothesis_generator(problem, hypothesis)
        print(hypothesis)
        logging.info('Hypothesis: %s', hypothesis)

        del hypothesis_generator

        verification_executor = verification_execution.VerificationExecutor(llm)
        verification_result = verification_executor(problem, hypothesis)
        logging.info('Verification Result: %s', verification_result)

        del verification_executor

        if 'True' in verification_result:
            print('Hypothesis is True')
            break

        cnt += 1

        # debugging
        if cnt == 1:
            break

    verification_plan = 'TODO: define internally'

    paper_writer = paper_writing.PaperWriter()
    latex_content = paper_writer(problem, hypothesis, verification_plan, verification_result, llm)  # TODO: intermediate_outputs
    print(latex_content)
    logging.info('LaTeX Content: %s', latex_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_paper", type=str, default='input_data/paper.tex', help="path_to_paper")
    args = parser.parse_args()
    main(args)