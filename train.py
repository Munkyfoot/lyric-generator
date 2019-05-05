from textgenrnn import textgenrnn
from datetime import datetime

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=15, max_gen_length=50, word_level=True,
                        max_length=20, new_model=True, rnn_bidirectional=True, rnn_size=128, rnn_layers=7, train_size=0.8, validation=True)
