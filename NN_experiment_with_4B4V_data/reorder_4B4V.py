import csv
import re
import random

'''
split and reorder ../4B4V.csv data to make the input file for Bi-RNN+CRF model
'''
cnt = 0
file_length = 0
train_f = open('4B4V_train.csv', 'w')
wr_train = csv.writer(train_f)
dev_f = open('4B4V_dev.csv', 'w')
wr_dev = csv.writer(dev_f)
test_f = open('4B4V_test.csv', 'w')
wr_test = csv.writer(test_f)

file_syl = open('../4B4V_syl.csv', newline='')
syl_reader = csv.reader(file_syl)
for row in syl_reader:
    syllables = row[0]
    file_length += 1
print("file size: " + str(file_length))
test_size = file_length//10
print("test & dev size: " + str(test_size))

file_idx = 0
file_syl = open('../4B4V_syl.csv', newline='')
file_word = open('../4B4V_wordbase.csv', newline='')
syl_reader = csv.reader(file_syl)
word_reader = csv.reader(file_word)

file_WB = open('../4B4V_WB.csv', 'w')
WB_writer = csv.writer(file_WB)

for row_syl, row_word in zip(syl_reader, word_reader):
    file_idx += 1
    syllables = row_syl[0]
    syllables = re.sub('[-]+', ' ', syllables)
    syllables = re.sub('[^a-zA-Z \'?!.]+', ' ', syllables)
    syllables = re.sub("\s\s+", " ", syllables)
    syllables = syllables.strip()
    syllables = syllables.lower()
    words = row_word[0]
    words = re.sub('[-]+', ' ', words)
    words = re.sub('[^a-zA-Z \'?!.]+', ' ', words)
    words = re.sub("\s\s+", " ", words)
    words = words.strip()
    words = words.lower()
    meters = row_syl[1]
    meters = meters.strip()
    met_str = ''
    for meter in meters:
        if meter == '^':
            b = random.randint(0, 1)
            tag_list = ['-', '+']
            meter = tag_list[b]
        met_str += meter
    meters = met_str
    syllables_list = re.findall(r'\S+', syllables)
    words_list = re.findall(r'\S+', words)
    i_word = 0
    syllables_WB = ''
    syllabs = ''
    for i_syl, syllable in enumerate(syllables_list):
        if syllable == words_list[i_word]:
            syllables_WB += '|' + syllable + '|'
            i_word += 1
        elif syllabs + syllable == words_list[i_word]:
            syllables_WB += syllable + '|'
            syllabs = ''
            i_word += 1
        else:
            if words_list[i_word][:len(syllable)] == syllable:
                syllables_WB += '|' + syllable
                syllabs = syllable
            else:
                syllables_WB += syllable
                syllabs += syllable
        syllables_WB += ' '
    syllables_WB = syllables_WB.rstrip()
    WB_writer.writerow([syllables_WB, meters])
file_WB.close()
file_idx = 0
with open('../4B4V_syl.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        file_idx += 1
        syllables = row[0]
        syllables = re.sub('[-]+', ' ', syllables)
        syllables = re.sub('[^a-zA-Z \'?!.]+', ' ', syllables)
        syllables = re.sub("\s\s+", " ", syllables)
        syllables = syllables.strip()
        meters = row[1]
        meters = meters.strip()
        syllables_list = re.findall(r'\S+', syllables)
        syllables_num = len(syllables_list)
        # vertical align
        syl_str = ''
        dd = 0
        for syllable in syllables_list:
            if dd == 0:
                syl_str += syllable
                dd = 1
            else:
                syl_str += ' ' + syllable
        if file_idx <= test_size:
            wr_test.writerow([syl_str, meters])
        elif file_idx <= 2*test_size:
            wr_dev.writerow([syl_str, meters])
        else:
            wr_train.writerow([syl_str, meters])

train_f_WB = open('4B4V_train_WB.csv', 'w')
wr_train_WB = csv.writer(train_f_WB)
dev_f_WB = open('4B4V_dev_WB.csv', 'w')
wr_dev_WB = csv.writer(dev_f_WB)
test_f_WB = open('4B4V_test_WB.csv', 'w')
wr_test_WB = csv.writer(test_f_WB)
file_idx = 0
with open('../4B4V_WB.csv', newline='') as myFile1:
    reader = csv.reader(myFile1)
    for row in reader:
        file_idx += 1
        syllables = row[0]
        syllables = syllables.strip()
        meters = row[1]
        meters = meters.strip()
        # vertical align
        if file_idx <= test_size:
            wr_test_WB.writerow([syllables, meters])
        elif file_idx <= 2*test_size:
            wr_dev_WB.writerow([syllables, meters])
        else:
            wr_train_WB.writerow([syllables, meters])
