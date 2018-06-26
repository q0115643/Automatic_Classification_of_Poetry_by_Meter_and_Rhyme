import csv
import re
import json
met_tags = []
unk_count = 0
known_count = 0
syl_dict = {}
unk_words = set()
known_words = set()

syl_dict_new = open('syl_dict_in_poetry.csv', 'w')
wr = csv.writer(syl_dict_new)
words_in_pyphen = []

with open('syl_dict.csv') as myFile:
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
            words = line.split(' ')
            for word in words:
                if word not in syl_dict:
                    if word not in unk_words:
                        unk_count += 1
                        unk_words.add(word)
                else:
                    if word not in known_words:
                        known_words.add(word)
                        known_count += 1
                        wr.writerow([word, syl_dict[word]])

print(known_count)  # 34324
print(unk_count)    # 25729
syl_dict_new.close()
with open('unk_words.txt', 'w') as myFile:
    for word in unk_words:
        myFile.write(word + '\n')
