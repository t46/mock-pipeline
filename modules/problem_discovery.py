import logging
from langchain import PromptTemplate

template = """
What is the problem to be solved you found in the latex texts below?
-------------------------------------------------------------------
{paper}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["paper"]
)

class ProblemDiscoverer:
    def __init__(self):
        pass
    def __call__(self, paper, llm):
        with open(paper, 'r') as f:
            text = f.read()
            prompt_text = prompt.format(paper=text)
            logging.info('Problem discovery prompt: %s', prompt_text)
        problem = llm(prompt_text)
        return problem