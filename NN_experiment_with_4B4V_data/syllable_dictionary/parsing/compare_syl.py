import csv
import re
import json

lines_ff = open('lines.txt', 'w', encoding='utf-8')
lines_f = open('lines_litlab.txt', 'w', encoding='utf-8')
with open('syllabes_file.txt', 'r', encoding='utf-8') as myFile:
    for line in myFile:
        line = re.sub('^\([^)]*\)', '', line)
        line = re.sub('\.', '|', line)
        line = re.sub('\*', '|', line)
        line = line.lower()
        line = re.sub('[^a-z\|\']+', '', line)
        line = re.sub("\s\s+", " ", line)
        line = re.sub("\|\|+", "|", line)
        line = re.sub("\n", '', line)
        if line != 'n' and line != 'm' and line != '':
            lines_f.write(line + '\n')
lines_f.close()

with open('poetry.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        poem = json.loads(row[0])
        for line in poem:
            line = line.lower()
            line = re.sub('[^a-z\' ]+', ' ', line)
            line = re.sub("\s\s+", " ", line)
            line = re.sub("\n", '', line)
            if line != '':
                lines_ff.write(line + '\n')
lines_ff.close()
