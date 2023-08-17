import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('openai')