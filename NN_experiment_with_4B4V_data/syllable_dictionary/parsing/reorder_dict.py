import csv
import re

filename = "syllabification_dictionary.txt"
f_csv = open('syl_dict.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f_csv)
word_table = set()
cnt = 0
with open(filename) as f:
    for line in f:
        word_syl = line.split('\\')
        box1 = word_syl[0]
        box2 = word_syl[1]
        word_num = len(box1.split(' '))
        if word_num < 2:
            box1 = box1.lower()
            box2 = box2.lower()
            box1 = re.sub("\n", "", box1)
            box2 = re.sub("\n", "", box2)
            box2 = re.sub("--", "-", box2)
            box1 = re.sub('[^a-z\']+', '', box1)
            box2 = re.sub('[^a-z\-\']+', '', box2)
            if box1 not in word_table:
                word_table.add(box1)
                wr.writerow([box1, box2])
                cnt += 1
print("number of words: " + str(cnt))
f_csv.close()
