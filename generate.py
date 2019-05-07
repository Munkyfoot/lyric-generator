import os
import sys
from textgenrnn import textgenrnn

try:
    textgen = textgenrnn(weights_path='textgenrnn_weights.hdf5',
                        vocab_path='textgenrnn_vocab.json',
                        config_path='textgenrnn_config.json')

    textgen.generate_to_file(
        os.path.join(sys.path[0], 'generation', 'T100'), n=10, temperature=[1.0])

    textgen.generate_to_file(
        os.path.join(sys.path[0], 'generation', 'T50'), n=10, temperature=[0.5])

    textgen.generate_to_file(
        os.path.join(sys.path[0], 'generation', 'T20'), n=10, temperature=[0.2])
except Exception as e:
    print("Generation failed with exception {}".format(e))