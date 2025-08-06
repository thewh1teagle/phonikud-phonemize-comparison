"""
uv pip install pygoruut       
"""
"""
uv pip install pygoruut       
"""
from pygoruut.pygoruut import Pygoruut

pygoruut063 = None

def phonemize(sentence: str) -> str:
    global pygoruut063
    if pygoruut063 is None:
        pygoruut063 = Pygoruut(version='v0.6.3')

    return str(pygoruut063.phonemize(language="Hebrew3", sentence=sentence))

# Example usage:
if __name__ == "__main__":
    print(phonemize("בוקר טוב"))
