from modules import problem_discovery, hypothesis_generation, verification_design, verification_instantiation, verification_execution, paper_writing
from langchain.llms import OpenAI
import argparse
import logging
import datetime

def main(args):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f'logs/{now}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
    llm = OpenAI(model_name="gpt-4", temperature=0.9)  # TODO: define internally
    verification_result = 'False'

    paper = args.path_to_paper
    problem_discoverer = problem_discovery.ProblemDiscoverer()
    problem = problem_discoverer(paper, llm)
    print(problem)
    logging.info('Problem: %s', problem)

    cnt = 0

    while 'False' in verification_result:

        hypothesis_generator = hypothesis_generation.HypothesisGenerator()
        if cnt == 0:
            hypothesis = hypothesis_generator(problem, llm)
        else:
            hypothesis = hypothesis_generator(problem, llm, hypothesis)
        print(hypothesis)
        logging.info('Hypothesis: %s', hypothesis)

        verification_designer = verification_design.VerificationDesigner()
        verification_plan = verification_designer(problem, hypothesis, llm)
        print(verification_plan)
        logging.info('Verification Plan: %s', verification_plan)

        verification_instantiator = verification_instantiation.VerificationInstantiator()
        executable_verification_plan = verification_instantiator(verification_plan, llm)
        print(executable_verification_plan)
        logging.info('Executable Verification Plan: %s', executable_verification_plan)

        verification_executor = verification_execution.VerificationExecutor()
        verification_result = verification_executor()
        logging.info('Verification Result: %s', verification_result)

        if 'True' in verification_result:
            print('Hypothesis is True')
            break
        
        cnt += 1

        # debugging
        if cnt == 2:
            break

    paper_writer = paper_writing.PaperWriter()
    latex_content = paper_writer(problem, hypothesis, verification_plan, verification_result, llm)  # TODO: intermediate_outputs
    print(latex_content)
    logging.info('LaTeX Content: %s', latex_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_paper", type=str, default='input_data/paper.tex', help="path_to_paper")
    args = parser.parse_args()
    main(args)