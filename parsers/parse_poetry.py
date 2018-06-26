import csv
import re
import json


met_tags = []
syll_dict = {}
syll_f = open('./NN_experiment_with_4B4V_data/syllable_dictionary/syl_dict_complete.csv', 'r')
syll_dict_reader = csv.reader(syll_f)
for row in syll_dict_reader:
    syll_dict[row[0]] = row[1]
nninput = open('input_for_nn.txt', 'w', encoding='utf-8')
poems = []
poetry_f = open('./poetry_new.csv', 'r')
poetry_reader = csv.reader(poetry_f)
for row in poetry_reader:
    met_tags.append(row[1])
    poem = json.loads(row[0])
    lines = []
    for line in poem:
        line = line.strip()
        line = line.lower()
        line = re.sub('-', ' ', line)
        line = re.sub('[?]+', '? ', line)
        line = re.sub('[!]+', '! ', line)
        line = re.sub('[.]+', '. ', line)
        line = re.sub('[^a-z \'?!.]+', '', line)
        line = re.sub("\s\s+", " ", line)
        words = line.split(' ')
        words = list(filter(None, words))
        line_str = ''
        for word in words:
            if '?' in word:
                word = re.sub("\?", '-?', word)
                word_list = word.split('-')
                word_list = list(filter(None, word_list))
                if len(word_list) > 1:
                    syllables = syll_dict[word_list[0]]
                    syllables += '?'
                else:
                    syllables = '?'
            elif '!' in word:
                word = re.sub("\!", '-!', word)
                word_list = word.split('-')
                word_list = list(filter(None, word_list))
                if len(word_list) > 1:
                    syllables = syll_dict[word_list[0]]
                    syllables += '!'
                else:
                    syllables = '!'
            elif '.' in word:
                word = re.sub("\.", '-.', word)
                word_list = word.split('-')
                word_list = list(filter(None, word_list))
                if len(word_list) > 1:
                    syllables = syll_dict[word_list[0]]
                    syllables += '.'
                else:
                    syllables = '.'
            else:
                syllables = syll_dict[word]
            syllables = syllables.split('-')
            syllables = list(filter(None, syllables))
            tmp = []
            for syllable in syllables:
                if re.sub("\s\s+", " ", syllable) != ' ':
                    tmp.append(syllable)
            syllables = tmp
            if len(syllables) == 1:
                syllables[0] = '|' + syllables[0] + '|'
            elif len(syllables) == 2:
                syllables[0] = '|' + syllables[0]
                syllables[1] = syllables[1] + '|'
            else:
                syllables[0] = '|' + syllables[0]
                syllables[-1] = syllables[-1] + '|'
            for syllable in syllables:
                line_str += syllable + ' '
        line_str = line_str.rstrip()
        print(line_str)
        if line_str != '':
            nninput.write(line_str + '\n')
        lines.append(line_str)
    poems.append(lines)

processed_poetry_f = open('poetry_WB_processed.csv', 'w')
wr = csv.writer(processed_poetry_f)
for i, poem in enumerate(poems):
    poem_json = json.dumps(poem)
    met = met_tags[i]
    wr.writerow([poem_json, met])










