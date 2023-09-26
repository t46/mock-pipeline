import sys

def install(package):
    if hasattr(sys, 'real_prefix'):
        # this is a virtual env, use it
        !{sys.executable} -m pip install {package}
    else:
        import IPython
        IPython.get_ipython().system('!{sys.executable} -m pip install {package}')

# Install the openai package
install('openai')