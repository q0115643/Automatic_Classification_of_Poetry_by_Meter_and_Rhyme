import csv
import re


'''
reorder ../4B4V.csv data to make the input file for Bi-RNN+CRF model
'''
cnt = 0
input_data = open('input.txt', 'w')
with open('../4B4V.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
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
            if meter == '+':
                meter = 's'
            else:
                meter = 'u'
            input_data.write(syllable + ' ' + 'I-' + meter + '\n')
        input_data.write('\n')

print("lines with not-matching number of meters and syllables: " + str(cnt))
input_data.close()
myFile.close()
