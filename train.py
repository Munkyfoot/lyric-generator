from textgenrnn import textgenrnn
from datetime import datetime

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=10, max_gen_length=32, word_level=True,
                        max_length=16, new_model=True, rnn_bidirectional=True, rnn_size=128, rnn_layers=4, train_size=0.8, validation=True)
