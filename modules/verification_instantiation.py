import re
import subprocess

prompt_verification_code_generation = """
You are a helpful assistant who should strictly adhere to the following guidelines:
- **DO NOT** include `api-key` in the code, as it has already been specified.
- **DO NOT** output placeholders, end up with comments, or use just a sequence of dots without fully implementing the contents of the code. Ensure that you fully implement the contents.

You are an excellent engineer. In accordance with the verification plan provided below, please output Python code to execute said plan. Note that you must comply with the instructions above.

Verification plan:
{verification_plan}

"""

prompt_instruction_following = """
Please regenerate the same Python code below except for the following modifications:
- **DO NOT** include `api-key` in the code, as it has already been specified.
- **DO NOT** output placeholders, end up with comments, or use just a sequence of dots without fully implementing the contents of the code. Ensure that you fully implement the contents.

Python code:
{verification_code}
"""

prompt_package_install = """
Output an executable Python code that installs the required package to run the code below. 
Make sure that the installation code is executable and does not cause any errors when run as a Python script, rather than as a Jupyter Notebook or from the command line.
Be sure to import all necessary libraries, including standard libraries, into the generated code.
Output only the code to install the package, not the code to run the package.

Python code:
{executable_verification_plan}
"""



def extract_python_blocks(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    combined = '\n'.join(match.strip() for match in matches)
    return combined

def refine_verification_code(verification_code, llm):
    refined_verification_code = llm(prompt_instruction_following.format(verification_code=verification_code))
    return refined_verification_code

def install_dependencies(executable_verification_plan, llm):
    code_to_install_packages = extract_python_blocks(llm(prompt_package_install.format(executable_verification_plan=executable_verification_plan)))
    print('Code to install packages: ', code_to_install_packages)

    with open('scripts/package_install.py', 'w') as f:
        f.write(code_to_install_packages)
    subprocess.run(["python", "scripts/package_install.py"])

    return code_to_install_packages

def instantiate_verification_plan(verification_plan, llm):
    raw_verification_code_in_text = llm(prompt_verification_code_generation.format(verification_plan=verification_plan))
    print('Raw verification code: ', raw_verification_code_in_text)

    refined_verification_code_in_text = refine_verification_code(raw_verification_code_in_text, llm)
    print('Refined verification code: ', refined_verification_code_in_text)

    verification_code = extract_python_blocks(refined_verification_code_in_text)
    with open('scripts/verification.py', 'w') as f:
        f.write(verification_code)
    package_install_code = install_dependencies(verification_code, llm)
    verification_code_data = {
        'raw_verification_code_in_text': raw_verification_code_in_text,
        'refined_verification_code_in_text': refined_verification_code_in_text,
        'verification_code': verification_code,
        'package_install_code': package_install_code
    }
    return verification_code_data