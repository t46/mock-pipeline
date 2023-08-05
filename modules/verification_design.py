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

template_for_hypothesis_refinement = """
Hypothesis: {hypothesis}
You will now test this hypothesis in the future. The hypothesis must be specific so that it can be tested. To this end, please formulate or model your hypothesis in concrete terms. 
You must also express all the expressions that come up in the hypothesis in text, physical entities, mathematical formulas, programs, or any appropriate expression depending on the verification method.
If you are using a mathematical process in the verification, the hypothesis should also be expressed in mathematical terms, and if you are proposing something, you will need to define its concrete substance.
Strictly following these instructions, output both the original hypothesis and a formulated hypothesis, a representation of the hypothesis, or a model of the hypothesis.
-------------------------------------------------------------------
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem", "hypothesis"]
)

def refine_hypothesis(hypothesis, llm):
    prompt_text = template_for_hypothesis_refinement.format(hypothesis=hypothesis)
    logging.info('Hypothesis refinement prompt: %s', prompt_text)
    refined_hypothesis = llm(prompt_text)
    return refined_hypothesis

def design_verification_plan(problem, hypothesis, llm):
    hypothesis = refine_hypothesis(hypothesis, llm)
    prompt_text = prompt.format(problem=problem, hypothesis=hypothesis)
    logging.info('Verification design prompt: %s', prompt_text)
    verification_plan = llm(prompt_text)
    return verification_plan