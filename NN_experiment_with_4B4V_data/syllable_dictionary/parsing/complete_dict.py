import csv
import json
import re

met_tags = []
dict_in_poem_f = open('syl_dict_in_poetry.csv', 'r')
dict_unk_f = open('syl_dict_unk.csv', 'r')
complete_dict_f = open('syl_dict_complete.csv', 'w')
wr = csv.writer(complete_dict_f)
dict_in_poem_reader = csv.reader(dict_in_poem_f)
dict_unk_reader = csv.reader(dict_unk_f)
for row in dict_in_poem_reader:
    wr.writerow(row)
for row in dict_unk_reader:
    wr.writerow(row)
dict_unk_f.close()
dict_in_poem_f.close()
complete_dict_f.close()

syl_dict = {}
with open('syl_dict_complete.csv', 'r') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict[row[0]] = row[1]

with open('poetry_new.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        met_tags.append(row[1])
        poem = json.loads(row[0])
        for line in poem:
            line = line.lower()
            line = re.sub('-', ' ', line)
            line = re.sub('[?!.]+', ' ', line)
            line = re.sub('[^a-z \']+', '', line)
            line = re.sub("\s\s+", " ", line)
            line = line.rstrip(' ')
            words = line.split(' ')
            for word in words:
                if word != '\n' and word != '':
                    if word not in syl_dict:
                        print(word)













