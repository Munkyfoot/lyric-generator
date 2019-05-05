# Lyrics Generator

## About
This project uses the textgenrnn package to generate lyrics.

## Requirements
- Python >= 3.5
- - textgenrnn

Install python version 3.5 or later and then run 'pip install textgenrnn'

## How to Use
1. Replace the lyrics in 'lyrics.data_raw' with your desired lyrics following the same format.
2. Run 'python cleanup_data.py' to format the data so it's easier for the neural network to understand.
3. Run 'python train.py' to train the model.
4. Run 'python generate.py' to generate sample outputs and save them to files.
5. Run 'python interactive.py' to generate a sample word by word with your input.

All sample lyrics are property of Sol Seed Music, LLC
