import sys

def install(package):
    if hasattr(sys, 'real_prefix'):
        # this is a virtual env, use pip
        !pip install {package}
    else:
        !pip install --user {package}

# Install the required packages
install('scikit-learn')
install('transformers')