import logging
from langchain import PromptTemplate

template = """
How can we solve the problem described below? Please provide multiple hypotheses in list format.

Problem:
{problem}
"""

hypothesis_selection_template = """
Please select the easiest-to-test hypothesis from among the hypotheses below.

Hypotheses:
{hypotheses}
"""

hypothesis_elaboration_template = """
Please make the hypothesis below more specific by providing a concrete example.

Hypothesis:
{hypothesis}
"""

preivious_hypothesis_template = """
The previous hypothesis listed below is incorrect. Please provide a more accurate hypothesis, supported by a detailed and concrete example.

Previous Hypothesis:
{previous_hypothesis}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem"]
)

class HypothesisGenerator:
    def __init__(self, llm):
        self.llm = llm
    
    def __call__(self, problem, previous_hypothesis=None):
        prompt_text = prompt.format(problem=problem)
        if previous_hypothesis is not None:
            prompt_text = preivious_hypothesis_template.format(previous_hypothesis=previous_hypothesis) + prompt_text
        logging.info('Hypothesis generation prompt: %s', prompt_text)
        hypothesis = self.llm(prompt_text)
        logging.info('Hypothesis: %s', hypothesis)
        hypothesis = self.llm(hypothesis_selection_template.format(hypotheses=hypothesis))
        logging.info('Hypothesis Selection: %s', hypothesis)
        hypothesis = self.llm(hypothesis_elaboration_template.format(problem=problem, hypothesis=hypothesis))
        logging.info('Hypothesis Elaboration: %s', hypothesis)

        return hypothesis