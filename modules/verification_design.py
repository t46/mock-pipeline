import logging
from langchain import PromptTemplate

template = """
Given the below problem and hypothesis to solve the problem, how can we verify the hypothesis? Please give us the detailed verification plan in strucured sentences. 
Please be detailed and very concrete so that the procedure should be executable by a large language model and computer. Write down the step-by-step procedure.
However, the verification plan should be as detailed as possible. If necessary, a single task can be broken down into multiple subtasks and listed hierarchically as a whole.
Also, the verification plan must be feasible. Therefore, you can use what you already have and do not need to create anything new. Make your validation plan as realistic as possible.

Problem:
{problem}

Hypothesis:
{hypothesis}
"""

template_for_hypothesis_formulation = """
You will test the hypothesis below. The hypothesis must be specific so that it can be tested. To this end, please formulate or model your hypothesis in concrete terms. 
You must also express all the expressions that come up in the hypothesis in text, physical entities, mathematical formulas, programs, or any appropriate expression depending on the verification method.
If you are using a mathematical process in the verification, the hypothesis should also be expressed in mathematical terms, and if you are proposing something, you will need to define its concrete substance.
Strictly following these instructions, output both the original hypothesis and a formulated hypothesis, a representation of the hypothesis, or a model of the hypothesis.

Hypothesis:
{hypothesis}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["problem", "hypothesis"]
)

def refine_hypothesis(hypothesis, llm):
    prompt_text = template_for_hypothesis_formulation.format(hypothesis=hypothesis)
    logging.info('Hypothesis refinement prompt: %s', prompt_text)
    refined_hypothesis = llm(prompt_text)
    return refined_hypothesis

def design_verification_plan(problem, hypothesis, llm):
    hypothesis = refine_hypothesis(hypothesis, llm)
    logging.info('Refined hypothesis: %s', hypothesis)
    print('Refined hypothesis: ', hypothesis)

    prompt_text = prompt.format(problem=problem, hypothesis=hypothesis)
    logging.info('Verification design prompt: %s', prompt_text)

    verification_plan = llm(prompt_text)
    logging.info('Verification plan: %s', verification_plan)
    print('Verification plan: ', verification_plan)
    return verification_plan