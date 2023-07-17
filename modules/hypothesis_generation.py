import logging
from langchain import PromptTemplate

template = """
Background Information: Prompt engineering is a powerful technique to enhance ability of large language models. Probmpt engineering is a technique to generate a prompt to a large language model so that the language model can output a desired text.
The technique is very useful because it does not require training to improve outputs in zero-shot way.
How can we solve the problem below? Please output a detailed and very concrete hypothesis.
Note that hypothesis is a statement that can be tested and answered in yes or no style.
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
        logging.info('Hypothesis generation prompt: %s', prompt_text)
        hypothesis = llm(prompt_text)
        return hypothesis