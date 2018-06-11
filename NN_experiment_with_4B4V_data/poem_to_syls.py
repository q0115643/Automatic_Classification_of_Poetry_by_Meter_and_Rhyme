import csv
import re
import json
import pyphen
dic = pyphen.Pyphen(lang='fr', left=1, right=1)
met_tags = []
unk_count = 0
known_count = 0
syl_dict = {}
unk_words = set()
known_words = set()

syl_dict_new = open('syl_dict_new.csv', 'w')
wr = csv.writer(syl_dict_new)
words_in_pyphen = []

with open('syl_dict.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict[row[0]] = row[1]

with open('poetry.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        met_tags.append(row[1])
        poem = json.loads(row[0])
        for line in poem:
            line = line.lower()
            line = re.sub('-', ' ', line)
            line = re.sub('[^a-z ]+', '', line)
            line = re.sub("\s\s+", " ", line)
            words = line.split(' ')
            for word in words:
                if word not in syl_dict:
                    if word not in unk_words:
                        unk_count += 1
                        unk_words.add(word)
                        words_in_pyphen.append(dic.inserted(word))
                else:
                    if word not in known_words:
                        known_words.add(word)
                        known_count += 1
                        wr.writerow([word, syl_dict[word]])

print(known_count)
print(unk_count)
syl_dict_new.close()
with open('unk_words.txt', 'w') as myFile:
    for word in unk_words:
        myFile.write(word + '\n')
