import logging
from langchain import PromptTemplate

template = """
Given the information below, output title, abstract, and introduction of research paper in latex file format.
-------------------------------------------------------------------
Research Problem: {problem}
Research Hypothesis: {hypothesis}
Verification Plan: {verification_plan}
Verification Result: {verification_result}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem", "hypothesis", "verification_plan", "verification_result"]
)


class PaperWriter:
    def __init__(self):
        pass
    def __call__(self, problem, hypothesis, verification_plan, verification_result, llm):
        prompt_text = prompt.format(problem=problem, hypothesis=hypothesis, verification_plan=verification_plan, verification_result=verification_result)
        logging.info('Paper writing prompt: %s', prompt_text)
        latex_content = llm(prompt_text)
        with open('latex/main.tex', 'w') as f:
            f.write(latex_content)
        return latex_content