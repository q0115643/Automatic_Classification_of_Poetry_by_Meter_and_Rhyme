import csv
import re
import random

'''
split and reorder ../4B4V.csv data to make the input file for Bi-RNN+CRF model
'''
cnt = 0
file_length = 0
train_data = open('./tagger_theano/train.txt', 'w')
dev_data = open('./tagger_theano/dev.txt', 'w')
test_data = open('./tagger_theano/test.txt', 'w')
with open('../4B4V.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syllables = row[0]
        file_length += 1
print("file size: " + str(file_length))
test_size = file_length//10
print("test & dev size: " + str(test_size))
myFile.close()
file_idx = 0
with open('../4B4V.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        file_idx += 1
        syllables = row[0]
        origin = syllables
        syllables = re.sub('[\']+', '', syllables)
        syllables = re.sub('[^a-zA-Z ]+', ' ', syllables)
        syllables = re.sub("\s\s+", " ", syllables)
        syllables = syllables.strip()
        syllables = syllables.lower()
        meters = row[1]
        meters = meters.strip()
        syllables_list = re.findall(r'\S+', syllables)
        syllables_num = len(syllables_list)
        meters_num = len(meters)
        if syllables_num != meters_num:
            print(syllables)
            print(origin)
            print(meters)
            print('\n')
            cnt += 1
        # vertical align
        for syllable, meter in zip(syllables_list, meters):
            if meter == '^':
                b = random.randint(0, 1)
                tag_list = ['-', '+']
                meter = tag_list[b]
            if file_idx <= test_size:
                test_data.write(syllable + ' ' + meter + '\n')
            elif file_idx <= 2*test_size:
                dev_data.write(syllable + ' ' + meter + '\n')
            else:
                train_data.write(syllable + ' ' + meter + '\n')
        if file_idx <= test_size:
            test_data.write('\n')
        elif file_idx <= 2*test_size:
            dev_data.write('\n')
        else:
            train_data.write('\n')

print("lines with not-matching number of meters and syllables: " + str(cnt))
myFile.close()
test_data.close()
train_data.close()
dev_data.close()
