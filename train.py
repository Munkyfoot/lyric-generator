from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('data/lyrics.data_processed', num_epochs=50, max_gen_length=120, word_level=False,
                        max_length=60, new_model=True, rnn_bidirectional=True, rnn_size=128, rnn_layers=5, train_size=0.8, validation=True)
