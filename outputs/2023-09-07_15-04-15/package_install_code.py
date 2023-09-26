import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install packages
install('numpy')
install('scipy')
install('sklearn')
install('openai')