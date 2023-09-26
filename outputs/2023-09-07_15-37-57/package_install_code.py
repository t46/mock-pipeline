import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install packages
install('pandas')
install('scikit-learn')
install('scipy')
install('transformers')