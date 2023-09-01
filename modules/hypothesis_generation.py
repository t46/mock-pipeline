import logging
from langchain import PromptTemplate

template = """
How can we solve the problem below? Please output multiple hypotheses in list format.
-------------------------------------------------------------------
{problem}
"""

hypothesis_selection_template = """
Select the hypothesis that is easiest to test from among these hypotheses.
-------------------------------------------------------------------
{hypotheses}
"""

hypothesis_elaboration_template = """
Please make the hypothesis below more specific and concrete with an example.

Note:
- Output a concrete example of your proposal.
-------------------------------------------------------------------
{hypothesis}
"""

preivious_hypothesis_template = """
Previous Hypothesis: {previous_hypothesis}
The previous hypothesis is not true. Please output a detailed and very concrete better hypothesis.
-------------------------------------------------------------------
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