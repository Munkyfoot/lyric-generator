from textgenrnn import textgenrnn
from datetime import datetime

try:
    textgen = textgenrnn(weights_path='textgenrnn_weights.hdf5',
                        vocab_path='textgenrnn_vocab.json',
                        config_path='textgenrnn_config.json')

    textgen.generate(interactive=True, top_n=5)
except KeyboardInterrupt:
    print("Interactive generation was interrupted.")
except:
    print("Generation failed. Have you run 'train.py' yet?")