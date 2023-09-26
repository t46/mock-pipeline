import sys

def install(package):
    if hasattr(sys, 'real_prefix'):
        # this is a virtual env, use it
        !{sys.executable} -m pip install {package}
    else:
        import pip
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

# Install the necessary packages
install('nltk')
install('scipy')
install('openai')