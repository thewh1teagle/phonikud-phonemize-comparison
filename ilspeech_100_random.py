"""
mkdir data && cd data
wget https://huggingface.co/datasets/thewh1teagle/ILSpeech/resolve/main/speaker2/ilspeech_speaker2_v1.7z
7z x ilspeech_speaker2_v1.7z
"""

import json
import random

with open("ilspeech_speaker2_v1/transcript.json", "r") as f:
    transcript = json.load(f)
with open("ilspeech_speaker2_v1/metadata.csv", "r") as f:
    metadata = f.readlines()
    metadata = {k: v for k, v in (line.strip().split("|") for line in metadata)}

def get_ilspeech_100_random():
    """
    Returns a list of dictionaries containing the metadata and transcript for 100 random samples from the ILSpeech dataset.
    """
    seed = 0
    random.seed(seed)
    keys = list(transcript.keys())
    random.shuffle(keys)
    ilspeech_100_random = {} # k: v
    for i in range(100):
        key = keys[i]
        text = transcript[key]
        phonemes = metadata[key]
        ilspeech_100_random[text] = phonemes
    return ilspeech_100_random

if __name__ == "__main__":
    ilspeech_100_random = get_ilspeech_100_random()
    with open("ilspeech_seed0_ran_v8_sentences.json", "w") as f:
        json.dump(ilspeech_100_random, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(ilspeech_100_random)} samples to ilspeech_100_random.json")
