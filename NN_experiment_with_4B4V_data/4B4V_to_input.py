import csv
import json
import re

train_f = open('4B4V_train_WB.csv', 'r')
test_f = open('4B4V_test_WB.csv', 'r')
dev_f = open('4B4V_test_WB.csv', 'r')
train_f_reader = csv.reader(train_f)
test_f_reader = csv.reader(test_f)
dev_f_reader = csv.reader(dev_f)

train_input = open('train_WB.txt', 'w', encoding='utf-8')
test_input = open('test_WB.txt', 'w', encoding='utf-8')
dev_input = open('dev_WB.txt', 'w', encoding='utf-8')

for row in train_f_reader:
    syllables = row[0].strip()
    meters = row[1].strip()
    syllables_list = re.findall(r'\S+', syllables)
    for syllable, meter in zip(syllables_list, meters):
        train_input.write(syllable + '\t' + meter + '\n')
    train_input.write('\n')

for row in test_f_reader:
    syllables = row[0].strip()
    meters = row[1].strip()
    syllables_list = re.findall(r'\S+', syllables)
    for syllable, meter in zip(syllables_list, meters):
        test_input.write(syllable + '\t' + meter + '\n')
    test_input.write('\n')

for row in dev_f_reader:
    syllables = row[0].strip()
    meters = row[1].strip()
    syllables_list = re.findall(r'\S+', syllables)
    for syllable, meter in zip(syllables_list, meters):
        dev_input.write(syllable + '\t' + meter + '\n')
    dev_input.write('\n')











