import logging
from langchain import PromptTemplate

template = """
The problem to besolved is:
{problem}

The hypothesis to solve the problem is:
{hypothesis}

Given above, how can we verify the hypothesis? Please give us the detailed verification plan in strucured sentences. 
Please be detailed and very concrete so that the procedure should be executable by a large language model and computer. Write down the step-by-step procedure.
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem", "hypothesis"]
)

class VerificationDesigner:
    def __init__(self):
        pass
    def __call__(self, problem, hypothesis, llm):
        prompt_text = prompt.format(problem=problem, hypothesis=hypothesis)
        logging.info('Verification design prompt: %s', prompt_text)
        verification_plan = llm(prompt_text)
        return verification_plan