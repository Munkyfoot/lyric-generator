from textgenrnn import textgenrnn
from datetime import datetime

try:
    textgen = textgenrnn(weights_path='textgenrnn_weights.hdf5',
                        vocab_path='textgenrnn_vocab.json',
                        config_path='textgenrnn_config.json')

    time_of_completion = datetime.now().isoformat(sep='_')

    textgen.generate_to_file(
        'generation/{}_T=1.0'.format(time_of_completion), n=10, temperature=[1.0])

    textgen.generate_to_file(
        'generation/{}_T=0.5'.format(time_of_completion), n=10, temperature=[0.5])

    textgen.generate_to_file(
        'generation/{}_T=0.2'.format(time_of_completion), n=10, temperature=[0.2])
except:
    print("Generation failed. Have you run 'train.py' yet?")