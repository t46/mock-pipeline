import logging
from langchain import PromptTemplate
import re
import subprocess

template = """

You are a helpful assistant which absolutely should fulfill all of the following.
Instructions that must be followed: Please follow strictly the following points.
- **DO NOT** include `your-api-key` in the code since it has already been specified!
- **DO NOT** output placeholder, make sure you write the implementation down to the contents of the function.

You are an excellent engineer.

Instruction: Given verification plan below, please output a python code to execute the verification plan. Note that you must obey the instructions above.
The verification plan is:
{verification_plan}

"""

template_for_refinement = """
The verification plan is this:
{verification_code}

Please regenerate the same python code except for the following modifications:
- **DO NOT** include `your-api-key` in the code since it has already been specified!
- **DO NOT** output placeholder, make sure you write the implementation down to the contents of the function.
- Please write a proper implementation where you **DO NOT** only end up with comments.
"""

template_for_install_dependencies = """
Output a executable python code that install the required package to run the code below:
{executable_verification_plan}
"""


prompt = PromptTemplate(
    template=template,
    input_variables=["verification_plan"]
)

prompt_install = PromptTemplate(
    template=template_for_install_dependencies,
    input_variables=["executable_verification_plan"]
)

prompt_refinement = PromptTemplate(
    template=template_for_refinement,
    input_variables=["verification_code"]
)

def extract_python_blocks(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    combined = '\n'.join(match.strip() for match in matches)
    return combined

def refine_verification_code(verification_code, llm):
    prompt_text = prompt_refinement.format(verification_code=verification_code)
    refined_verification_code = llm(prompt_text)
    return refined_verification_code

def install_dependencies(executable_verification_plan, llm):
    prompt_text = prompt_install.format(executable_verification_plan=executable_verification_plan)
    logging.info('Package install prompt: %s', prompt_text)
    code_to_install_packages = extract_python_blocks(llm(prompt_text))
    with open('scripts/package_install.py', 'w') as f:
        f.write(code_to_install_packages)
    subprocess.run(["python", "scripts/package_install.py"])

def instantiate_verification_plan(verification_plan, llm):
    prompt_text = prompt.format(verification_plan=verification_plan)
    logging.info('Verification instantiation prompt: %s', prompt_text)
    verification_code = llm(prompt_text)
    logging.info('Raw verification code: %s', verification_code)
    refined_verification_code = refine_verification_code(verification_code, llm)
    logging.info('Refined verification code: %s', refined_verification_code)
    executable_verification_plan = extract_python_blocks(refined_verification_code)
    with open('scripts/verification.py', 'w') as f:
        f.write(executable_verification_plan)
    install_dependencies(executable_verification_plan, llm)