from textgenrnn import textgenrnn
from datetime import datetime

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=15, max_gen_length=100, word_level=False,
                        max_length=50, new_model=True, rnn_bidirectional=True, rnn_size=128, rnn_layers=3, train_size=0.8, validation=True)
