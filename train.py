from textgenrnn import textgenrnn
from datetime import datetime

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=10, max_gen_length=150, word_level=True,
                        max_length=5, new_model=True, rnn_size=128, rnn_layers=3, train_size=0.8, validation=True)
