import os
import sys
import string

formatted_data = ""

with open(os.path.join(sys.path[0], 'data', 'lyrics.data_raw'), encoding='utf-8') as file:
    data = file.read()

    data = data.lower()
    data = data.translate(str.maketrans('', '', string.punctuation))
    data = data.replace('chorus', '')
    data = data.replace('lyrics by', '')
    data = data.replace('michael', '')
    data = data.replace('kenny', '')
    data = data.replace('benny', '')
    data = data.replace('sky', '')
    data = data.replace('lennon', '')
    data = data.replace('sorensen', '')
    data = data.replace('pezzano', '')
    data = data.replace('lewis', '')
    data = data.replace('guasco', '')
    data = data.replace('\n\n\n\n\n\n\n\n', '\n\n')
    data = data.replace('\n\n\n\n\n\n\n', '\n\n')
    data = data.replace('\n\n\n\n\n\n', '\n\n')
    data = data.replace('\n\n\n\n\n', '\n\n')
    data = data.replace('\n\n\n\n', '\n\n')
    data = data.replace('\n\n\n', '\n\n')
    data = data.replace('\n\n', '\n---\n')
    
    lines = data.split('\n')
    
    data = ""

    for i in range(len(lines)):
        stripped_line = lines[i].strip()
        if len(stripped_line) > 0:
            if stripped_line == '---':
                data += '\n'
            else:
                data += '{} '.format(stripped_line)

    lines = data.split('\n')

    for i in range(len(lines)):
        if len(lines[i].split(' ')) > 5:
            formatted_data += '{}\n'.format(lines[i])

with open(os.path.join(sys.path[0], 'data', 'lyrics.data_processed'), 'w', encoding='utf-8') as file:
    file.write(formatted_data)