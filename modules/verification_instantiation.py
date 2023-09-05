import logging
from langchain import PromptTemplate
import re
import subprocess

template = """
You are a helpful assistant who should strictly adhere to the following guidelines:
- **DO NOT** include `api-key` in the code, as it has already been specified.
- **DO NOT** output placeholders, end up with comments, or use just a sequence of dots without fully implementing the contents of the code. Ensure that you fully implement the contents.

You are an excellent engineer. In accordance with the verification plan provided below, please output Python code to execute said plan. Note that you must comply with the instructions above.

Verification plan:
{verification_plan}

"""

template_for_refinement = """
Please regenerate the same Python code below except for the following modifications:
- **DO NOT** include `api-key` in the code, as it has already been specified.
- **DO NOT** output placeholders, end up with comments, or use just a sequence of dots without fully implementing the contents of the code. Ensure that you fully implement the contents.

Python code:
{verification_code}
"""

template_for_install_dependencies = """
Output an executable Python code that installs the required package to run the code below. 
Make sure that the installation code is executable and does not cause any errors when run as a Python script, rather than as a Jupyter Notebook or from the command line.

Python code:
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
    return executable_verification_plan