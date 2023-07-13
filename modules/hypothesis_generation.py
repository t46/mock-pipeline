import logging
from langchain import PromptTemplate

template = """
Background Information: Prompt engineering is a powerful technique to enhance ability of large language models.
How can we solve the problem below? Please be concice, simple, and very concrete.
-------------------------------------------------------------------
{problem}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem"]
)

class HypothesisGenerator:
    def __init__(self):
        pass
    def __call__(self, problem, llm):
        prompt_text = prompt.format(problem=problem)
        logging.info('Problem discovery prompt: %s', prompt_text)
        hypothesis = llm(prompt_text)
        return hypothesis