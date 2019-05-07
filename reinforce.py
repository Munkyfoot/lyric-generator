from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path='textgenrnn_weights.hdf5',
                        vocab_path='textgenrnn_vocab.json',
                        config_path='textgenrnn_config.json')
textgen.train_from_file('data/lyrics.data_processed', num_epochs=5)
