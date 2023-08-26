import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install the packages
install('csv')
install('random')
install('statsmodels')
install('nltk')
install('sklearn')
install('pandas')