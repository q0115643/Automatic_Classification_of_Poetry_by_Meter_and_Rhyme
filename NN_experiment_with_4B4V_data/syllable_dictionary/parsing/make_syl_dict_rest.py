import csv
import re


syl_dict = {}
syl_dict_new = {}
syl_dict_rest = {}

with open('syl_dict.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict[row[0]] = row[1]

with open('syl_dict_in_poetry.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        syl_dict_new[row[0]] = row[1]

for key, value in syl_dict.items():
    if key not in syl_dict_new:
        syl_dict_rest[key] = value
cnt = 0
syl_dict_rest_file = open('syl_dict_not_in_poetry.csv', 'w')
wr = csv.writer(syl_dict_rest_file)
for key, value in syl_dict_rest.items():
    wr.writerow([key, value])
    cnt += 1
syl_dict_rest_file.close()
print(cnt)
