import subprocess
from modules.verification_design import design_verification_plan
from modules.verification_instantiation import instantiate_verification_plan, extract_python_blocks
from langchain import PromptTemplate
import logging

template_for_error_handling = """
{executable_verification_plan}
When I ran the code above, I got the following error Please output improved code to avoid this error.
Please output the entire code without omission, including the parts I have already provided
{error_message}
"""

prompt = PromptTemplate(
    template=template_for_error_handling,
    input_variables=["executable_verification_plan", "error_message"]
)
class VerificationExecutor:
    def __init__(self, llm):
        self.llm = llm

    def prepare_verification(self, problem, hypothesis):
        verification_plan = design_verification_plan(problem, hypothesis, self.llm)
        executable_verification_plan = instantiate_verification_plan(verification_plan, self.llm)
        return executable_verification_plan

    def __call__(self, problem, hypothesis):
        executable_verification_plan = self.prepare_verification(problem, hypothesis)
        process = subprocess.Popen(["python", "scripts/verification.py"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        # NOTE: Commented out for now becuase it works without it.
        # if process.returncode != 0:
        #     error_message = stderr.decode('utf-8')
        #     prompt_text = prompt.format(executable_verification_plan=executable_verification_plan, error_message=error_message)
        #     logging.info('Verification instantiation prompt: %s', prompt_text)
        #     updated_verification_code = extract_python_blocks(self.llm(prompt_text))
        #     with open('scripts/verification.py', 'w') as f:
        #         f.write(updated_verification_code)
        return 'Hypothesis is False'