import logging
from langchain import PromptTemplate

template = """
The text below is that of a academic paper.
What is the research problem to be solved you found in the texts below?
Please be detailed and very concrete so that we can generate a concrete hypothesis from the problem.
-------------------------------------------------------------------
{paper}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["paper"]
)

class ProblemDiscoverer:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, paper):
        with open(paper, 'r') as f:
            text = f.read()
            prompt_text = prompt.format(paper=text)
            logging.info('Problem discovery prompt: %s', prompt_text)
        problem = self.llm(prompt_text)
        return problem