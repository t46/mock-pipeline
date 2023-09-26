import sys

def install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        !{sys.executable} -m pip install {package}

install('openai')
install('numpy')