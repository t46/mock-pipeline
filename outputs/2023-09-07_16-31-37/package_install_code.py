import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install the necessary packages
install('numpy')
install('scipy')
install('transformers')