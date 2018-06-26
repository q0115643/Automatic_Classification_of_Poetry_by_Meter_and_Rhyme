import re
import csv

processed = open('output_dict.csv', 'w', encoding='utf-8')
wr = csv.writer(processed)

meters_list = []
out_f = open('output.txt', 'r', encoding='utf-8')
for line in out_f.read().splitlines():
    line = re.sub('[^\-+]', '', line)
    print(line)
    meters_list.append(line)
line_list = []
inp_f = open('input_for_nn.txt', 'r', encoding='utf-8')
for line in inp_f.read().splitlines():
    print(line)
    line_list.append(line)

for meters, line in zip(meters_list, line_list):
    wr.writerow([line, meters])

