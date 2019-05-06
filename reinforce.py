from textgenrnn import textgenrnn
from datetime import datetime

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=25)
