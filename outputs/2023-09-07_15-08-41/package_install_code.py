import sys

def install(package):
    if hasattr(sys, 'real_prefix'):
        # we are in a virtual env.
        !{sys.executable} -m pip install {package}
    else:
        !pip install --user {package}

# Install necessary packages
install('openai')
install('pandas')
install('scipy')