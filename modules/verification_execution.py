import subprocess
from modules.verification_design import design_verification_plan
from modules.verification_instantiation import instantiate_verification_plan
class VerificationExecutor:
    def __init__(self, llm):
        self.llm = llm

    def prepare_verification(self, problem, hypothesis):
        verification_plan = design_verification_plan(problem, hypothesis, self.llm)
        instantiate_verification_plan(verification_plan, self.llm)

    def __call__(self, problem, hypothesis):
        self.prepare_verification(problem, hypothesis)
        subprocess.run(["python", "scripts/verification.py"])
        return 'Hypothesis is False'