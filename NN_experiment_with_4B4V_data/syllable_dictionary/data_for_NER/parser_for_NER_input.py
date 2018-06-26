import csv
import re
import json
import random
'''
unk_f = open('unk_words.txt', 'r', encoding='utf-8')
test_set = open('test.txt', 'w', encoding='utf-8')
for word in unk_f.read().splitlines():
    for c in word:
        test_set.write(c+'\n')
    test_set.write('\n')
unk_f.close()
test_set.close()
'''
syl_dict_in = []
syl_dict_out = []

with open('syl_dict_in_poetry.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict_in.append((row[0], row[1]))

with open('syl_dict_not_in_poetry.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict_out.append((row[0], row[1]))
random.shuffle(syl_dict_out)
train_data = []
dev_data = []
test_data = []
for item in syl_dict_in:
    train_data.append(item)
for i, item in enumerate(syl_dict_out):
    if i < 3000:
        dev_data.append(item)
    elif i < 6000:
        test_data.append(item)
    else:
        train_data.append(item)
train_f = open('train.txt', 'w', encoding='utf-8')
for (word, syllables) in train_data:
    revise = 0
    for i, c in enumerate(word):
        train_f.write(c + '\t')
        if i == 0:
            train_f.write('b')
        elif syllables[i+revise-1] == '-':
            train_f.write('b')
        else:
            train_f.write('i')
        if len(syllables) > i+revise+1:
            if syllables[i+revise+1] == '-':
                revise += 1
        train_f.write('\n')
    train_f.write('\n')
train_f.close()
dev_f = open('dev.txt', 'w', encoding='utf-8')
for (word, syllables) in dev_data:
    revise = 0
    for i, c in enumerate(word):
        dev_f.write(c + '\t')
        if i == 0:
            dev_f.write('b')
        elif syllables[i+revise-1] == '-':
            dev_f.write('b')
        else:
            dev_f.write('i')
        if len(syllables) > i+revise+1:
            if syllables[i+revise+1] == '-':
                revise += 1
        dev_f.write('\n')
    dev_f.write('\n')
dev_f.close()
test_f = open('test.txt', 'w', encoding='utf-8')
for (word, syllables) in test_data:
    revise = 0
    for i, c in enumerate(word):
        test_f.write(c + '\t')
        if i == 0:
            test_f.write('b')
        elif syllables[i+revise-1] == '-':
            test_f.write('b')
        else:
            test_f.write('i')
        if len(syllables) > i+revise+1:
            if syllables[i+revise+1] == '-':
                revise += 1
        test_f.write('\n')
    test_f.write('\n')
test_f.close()
