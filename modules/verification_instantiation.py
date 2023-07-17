import logging
from langchain import PromptTemplate
import re

template = """
The verification plan is:
{verification_plan}

You are an excellent engineer.
Given verification plan above, please output a python code to execute the verification plan.
If it is difficult to output a single python code, you can output a list of python codes.
Even if it is difficult to output a perfect python code, please follow strictly the instruction and output a python code as much as possible.
Do not output a mere sample code. Instead, output a code which is used in real world, escpecially in research and development.
If you cannot specify a part of implelementation, use the ones which are commonly used in real world.
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["verification_plan"]
)

def extract_python_blocks(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    combined = '\n'.join(match.strip() for match in matches)
    return combined

class VerificationInstantiator:
    def __init__(self):
        pass
    def __call__(self, verification_plan, llm):
        prompt_text = prompt.format(verification_plan=verification_plan)
        logging.info('Verification instantiation prompt: %s', prompt_text)
        executable_verification_plan = extract_python_blocks(llm(prompt_text))
        with open('scripts/verification.py', 'w') as f:
            f.write(executable_verification_plan)
        return executable_verification_plan