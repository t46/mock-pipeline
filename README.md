# mock-pipeline
## Repository Structure
```
.
├── README.md
├── input_data ...................................... Any data to be entered into the module should be placed here.
│   └── problem.txt ................................. A sample research problem read by the hypothesis_generation module.
├── modules ......................................... The modules that make up the pipeline.
│   ├── __init__.py
│   ├── hypothesis_generation.py .................... A module that generates a hypothesis given a problem.
│   ├── verification_design.py ...................... A module that designs a verification plan given problem and hypothesis.
│   ├── verification_execution.py ................... A module that executes a insntantiated verification plan.
│   └── verification_instantiation.py ............... A module that instantiates a verification plan given a design.
├── pipeline.py ..................................... The main pipeline script.
├── scripts ......................................... Scripts that are generated by the modules.
│   ├── package_install.py .......................... A script by verification_instantiation that installs required packages.
│   └── verification.py ............................. A script by verification_instantiation that executes the verification.
└── outputs ......................................... Generated outputs.
    ├── evaluation.csv .............................. The results of evaluation for each run.
    ├── 2023-09-07_15-04-15 ......................... Outputs saved at 2023-09-07_15-04-15
    │   ├── hypothesis_candidates.txt ............... Hypothesis candidates generated by "Hypothesis Candidate Generation".
    │   ├── hypothesis.txt .......................... Hypothesis generated (selected) by "Hypothesis Selection".
    │   ├── representation_of_hypothesis.txt ........ Reformulated hypothesis generated by "Hypothesis Reformulation".
    │   ├── verification_plan.txt ................... Verification plan generated by "Verification Plan Design".
    │   ├── raw_verification_code_in_text.txt ....... Verification code generated by "Verification Code Generation".
    │   ├── refined_verification_code_in_text.txt ... Verification code re-generated to follow instruction by "Instruction Following".
    │   ├── verification_code.py .................... Verification code extracted from refined_verification_code_in_text.txt. and saved as Python script.
    │   ├── verification_code_updated.py ............ Verification code updated based on error messages.
    │   └── package_install_code.py ................. Package installation code generated by "Package Install Code Generation".
    ├── 2023-09-07_15-04-16 ......................... Outputs saved at 2023-09-07_15-04-16
    │   ├── hypothesis_candidates.txt ............... Hypothesis candidates generated by "Hypothesis Candidate Generation".
```

## Quick Start
### Create a Virtual Environment
```shell
conda create -n autores
conda activate autores
conda install -c conda-forge langchain
```
### Set Environment Variables
```shell
export OPENAI_API_KEY="your-api-key"
```

### Run Pipeline
```shell
python pipeline.py
```

### Run Pipeline 50 Times
```shell
```shell
./run_pipeline.sh
```

## Evaluation
The author's subjective evaluation results are recorded in `outputs/evaluation.csv` . If the criteria listed in the columns are satisfied, 1 is recorded, and if not, 0 is recorded. Below is a brief description of each column. Please refer to the Appendix of the paper for a description of how the evaluation was conducted.

- `hypothesis_is_appropriate`: If the hypothesis is judged to be appropriate for the problem, 1 is recorded.
- `hypothesis_is_feasible`: If the hypothesis is judged to be feasible given the resouce GPT-4 can use, 1 is recorded.
- `verification_code_or_code_updated_is_appropriate`: If the `verification_code.py` or the `verification_code_updated.py` is judged to be appropriate, 1 is recorded.
- `verification_code_is_executable`: If `verification_code.py` is executable, 1 is recorded.
- `no_plaece_holder`: If there is no place holder, ellipsis, or items that have only comments left without any implementation in `verification_code.py`, 1 is recorded.
- `package_install_is_executable`: If `package_install_code.py` is executable, 1 is recorded.
- `verification_code_updated_is_executable`: If `verification_code_updated.py` is executable, 1 is recorded.
- `verification_code_updated_contains_api_error`: If `verification_code_updated.py` contains an error related to API use, 1 is recorded.
- `api_error_only`: If `verification_code_updated.py` contains only an error related to API use, 1 is recorded.
- `appropriate & executable`: If either `verification_code.py` or `verification_code_updated.py` is both appropriate and executable, 1 is recorded.
- `appropriate & executable & package`: If either `verification_code.py` or `verification_code_updated.py` is both appropriate and executable, and `package_install_code.py` is executable, 1 is recorded.
- `appropriate & api_only`: If either `verification_code.py` or `verification_code_updated.py` is both appropriate and executable, and `verification_code_updated.py` contains only an error related to API use, 1 is recorded.
- `total_evaluation`: If `hypthesis_is_appropriate`, `hyoithesis_is_feasible`, and `appropriate & executable & package` are 1, 1, 1 is recorded, 1 is recorded.