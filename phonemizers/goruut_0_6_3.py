"""
uv pip install pygoruut       
"""
"""
uv pip install pygoruut       
"""
from pygoruut.pygoruut import Pygoruut

pygoruut = None

def phonemize(sentence: str) -> str:
    global pygoruut
    if pygoruut is None:
        pygoruut = Pygoruut(version='v0.6.3')

    return str(pygoruut.phonemize(language="Hebrew3", sentence=sentence))

# Example usage:
if __name__ == "__main__":
    print(phonemize("בוקר טוב"))
