
verification_plan_design_prompt = """
Given the problem and accompanying hypothesis below, how can we verify the hypothesis? Please provide a detailed verification plan composed of structured sentences. 
Ensure that the plan is sufficiently detailed and concrete so that it can be executed by a large language model and computer. 
Outline the procedure in a step-by-step manner. If necessary, break down a single task into multiple sub-tasks and list them hierarchically. 
The verification plan should be realistic and feasible, making use of existing resources rather than requiring the creation of new ones.

Problem:
{problem}

Hypothesis:
{hypothesis}
"""

hypothesis_formulation_prompt = """
To test the hypothesis below, ensure that it is specific enough to be testable. Formulate or model your hypothesis in concrete terms. Clearly express all elements of the hypothesis using text, physical entities, mathematical formulas, computer programs, or any other suitable forms, depending on the verification method you're using. 
If your verification involves a mathematical process, also articulate the hypothesis in mathematical terms. If you're proposing something new, define it in concrete terms. 
Once you've followed these guidelines, present both the original hypothesis and your refined version, whether that is a formulated hypothesis, a representation, or a model.

Hypothesis:
{hypothesis}
"""


def refine_hypothesis(hypothesis, llm):
    refined_hypothesis = llm(hypothesis_formulation_prompt.format(hypothesis=hypothesis))
    return refined_hypothesis

def design_verification_plan(problem, hypothesis, llm):
    representation_of_hypothesis = refine_hypothesis(hypothesis, llm)
    print('Representation of hypothesis: ', representation_of_hypothesis)

    verification_plan = llm(verification_plan_design_prompt.format(problem=problem, hypothesis=representation_of_hypothesis))
    print('Verification plan: ', verification_plan)

    verification_plan_data = {
        'representation_of_hypothesis': representation_of_hypothesis,
        'verification_plan': verification_plan
    }
    
    return verification_plan_data