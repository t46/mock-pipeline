from modules import problem_discovery, hypothesis_generation, verification_design, verification_instantiation, verification_execution, paper_writing
from langchain.llms import OpenAI
import argparse
import logging

def main(args):
    logging.basicConfig(
        filename='logs/output.log',  # ログを保存するファイル名
        level=logging.INFO,  # ログのレベル (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(levelname)s - %(message)s'  # ログのフォーマット
)
    llm = OpenAI(model_name="text-davinci-003", temperature=0.9)  # TODO: define internally

    paper = args.path_to_paper
    problem_discoverer = problem_discovery.ProblemDiscoverer()
    problem = problem_discoverer(paper, llm)
    print(problem)
    logging.info('Problem: %s', problem)

    hypothesis_generator = hypothesis_generation.HypothesisGenerator()
    hypothesis = hypothesis_generator(problem, llm)
    print(hypothesis)
    logging.info('Hypothesis: %s', hypothesis)

    verification_designer = verification_design.VerificationDesigner()
    verification_plan = verification_designer(problem, hypothesis, llm)
    print(verification_plan)
    logging.info('Verification Plan: %s', verification_plan)

    # verification_instantiator = verification_instantiation.VerificationInstantiator()
    # executable_verification_plan = verification_instantiator(verification_plan)

    # verification_executor = verification_execution.VerificationExecutor()
    # verification_result = verification_executor(executable_verification_plan)
    verification_result = "Hypothesis is True"
    logging.info('Verification Result: %s', verification_result)

    paper_writer = paper_writing.PaperWriter()
    latex_content = paper_writer(problem, hypothesis, verification_plan, verification_result, llm)  # TODO: intermediate_outputs
    print(latex_content)
    logging.info('LaTeX Content: %s', latex_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_paper", type=str, default='input_data/paper.tex', help="path_to_paper")
    args = parser.parse_args()
    main(args)