import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install packages
install('pandas')
install('numpy')
install('scipy')
install('matplotlib')
install('seaborn')
install('sklearn')