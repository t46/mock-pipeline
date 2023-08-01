import subprocess
class VerificationExecutor:
    def __init__(self):
        pass
    def __call__(self):
        subprocess.run(["python", "scripts/verification.py"])
        return 'Hypothesis is False'