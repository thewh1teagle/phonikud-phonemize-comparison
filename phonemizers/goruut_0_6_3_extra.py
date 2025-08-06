"""
uv pip install pygoruut       
"""
"""
uv pip install pygoruut       
"""
from pygoruut.pygoruut import Pygoruut

pygoruut063extra = None

def phonemize(sentence: str) -> str:
    global pygoruut063extra
    if pygoruut063extra is None:
        import urllib.request
        urllib.request.urlretrieve("https://huggingface.co/neurlang/goruut_extra_models/resolve/main/hebrew3.zip", filename="/tmp/hebrew3.zip")
        pygoruut063extra = Pygoruut(version='v0.6.3', models={"Hebrew3": "/tmp/hebrew3.zip"})

    return str(pygoruut063extra.phonemize(language="Hebrew3", sentence=sentence))

# Example usage:
if __name__ == "__main__":
    print(phonemize("בוקר טוב"))
