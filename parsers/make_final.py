import csv
import re
import json


met_tags = []
met_dict = {}
syll_f = open('output_dict.csv', 'r')
syll_dict_reader = csv.reader(syll_f)
for row in syll_dict_reader:
    met_dict[row[0]] = row[1]

final_csv = open('poetry_from_nn.csv', 'w', encoding='utf-8')
final_wr = csv.writer(final_csv)

poems = []
poetry_f = open('./poetry_WB_processed.csv', 'r')
poetry_reader = csv.reader(poetry_f)
cnt = 0
for row in poetry_reader:
    cnt += 1
    met_tags.append(row[1])
    poem = json.loads(row[0])
    lines = []
    for line in poem:
        if line != '':
            lines.append(met_dict[line])
    poems.append(lines)
print(cnt)
cnt = 0
for poem, metric in zip(poems, met_tags):
    poem_json = json.dumps(poem)
    final_wr.writerow([poem_json, metric])
    cnt +=1
print(cnt)






