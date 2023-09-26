

hypothesis_candidates_template = """
How can we solve the problem described below? Please provide multiple hypotheses in list format.

Problem:
{problem}
"""

hypothesis_selection_template = """
Please select the easiest-to-test hypothesis from among the hypotheses below.

Hypotheses:
{hypotheses}
"""


class HypothesisGenerator:
    def __init__(self, llm):
        self.llm = llm
        self.outputs = {}
    
    def __call__(self, problem):
        hypothesis_candidates = self.llm(hypothesis_candidates_template.format(problem=problem))
        print(hypothesis_candidates)

        selected_hypothesis = self.llm(hypothesis_selection_template.format(hypotheses=hypothesis_candidates))
        print(selected_hypothesis)

        hypothesis_data = {
            'hypothesis_candidates': hypothesis_candidates,
            'hypothesis': selected_hypothesis,
        }

        self.outputs.update(hypothesis_data)

        return hypothesis_data