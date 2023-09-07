import subprocess
from modules.verification_design import design_verification_plan
from modules.verification_instantiation import instantiate_verification_plan, extract_python_blocks


error_handling_prompt = """
When I ran the python code below, I got the error below. Please output improved code to avoid this error.
Please output the entire code without omission, including the parts I have already provided.

Python code:
{executable_verification_plan}

Error message:
{error_message}
"""


class VerificationExecutor:
    def __init__(self, llm):
        self.llm = llm
        self.outputs = {}

    def prepare_verification(self, problem, hypothesis):
        verification_data = {}

        verification_plan_data = design_verification_plan(problem, hypothesis, self.llm)
        verification_plan = verification_plan_data['verification_plan']
        verification_data.update(verification_plan_data)

        verification_code_data = instantiate_verification_plan(verification_plan, self.llm)
        verification_data.update(verification_code_data)

        self.outputs.update(verification_data)

        return verification_data

    def __call__(self, problem, hypothesis):
        verification_code = self.prepare_verification(problem, hypothesis)['verification_code']
        subprocess.run(["python", "scripts/verification.py"])
        # NOTE: This is commented out just for the sake of the demo.
        process = subprocess.Popen(["python", "scripts/verification.py"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        if process.returncode != 0:
            error_message = stderr.decode('utf-8')
            updated_verification_code = extract_python_blocks(self.llm(error_handling_prompt.format(executable_verification_plan=verification_code, error_message=error_message)))
            print('Updated verification code: ', updated_verification_code)

            self.outputs['verification_code_updated'] = updated_verification_code
            with open('scripts/verification.py', 'w') as f:
                f.write(updated_verification_code)
            subprocess.run(["python", "scripts/verification.py"])