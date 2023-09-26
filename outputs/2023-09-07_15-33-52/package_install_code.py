import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install the required packages
install('numpy')
install('matplotlib')
install('scipy')
install('transformers')