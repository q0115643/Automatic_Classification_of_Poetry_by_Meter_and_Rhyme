from xml.etree import ElementTree as ET
import os
import json
import re
import csv
import random

def getText(a, iterStr):
    noteTag = iterStr + 'note'
    text = ""
    if a.text and a.tag != noteTag:
        text += a.text
    for child in a.getchildren():
        text += getText(child, iterStr)
    return text

def getData(path, iterStr):
    with open(path, 'r', encoding='utf-8') as file:
        str_xml = file.read()
        str_xml2 = (str_xml + '.')[:-1]
        str_xml = re.sub('<caesura/>', '', str_xml)
        str_xml = re.sub('<sb[^>]*>', '', str_xml)
        str_xml = re.sub('</sb>', '', str_xml)
        str_xml = re.sub('<rhyme[^>]*>', '', str_xml)
        str_xml = re.sub('</rhyme>', '', str_xml)
        str_xml = re.sub('</seg>', '</seg>', str_xml)

        str_xml2 = re.sub('<caesura/>', ' ', str_xml2)
        str_xml2 = re.sub('<sb[^>]*>', ' ', str_xml2)
        str_xml2 = re.sub('</sb>', ' ', str_xml2)
        str_xml2 = re.sub('<rhyme[^>]*>', ' ', str_xml2)
        str_xml2 = re.sub('</rhyme>', ' ', str_xml2)
        str_xml2 = re.sub('</seg>', ' </seg>', str_xml2)

        root = ET.XML(str_xml)
        lines = list(root.iter(iterStr + 'l'))
        reals = [re.sub('[\(\)]', '', (re.sub('\|.*$', '', str(a.get('real'))))) for a in lines]
        meters = [a.get('met') for a in lines]
        text = [re.sub('\n', ' ', getText(a, iterStr)).strip() for a in lines]
        real_meters = [met if re.sub("\s\s+", " ", real) == '' else real for real, met in zip(reals, meters)]

        root2 = ET.XML(str_xml2)
        lines2 = list(root2.iter(iterStr + 'l'))
        reals2 = [re.sub('[\(\)]', '', (re.sub('\|.*$', '', str(a.get('real'))))) for a in lines2]
        meters2 = [a.get('met') for a in lines2]
        text2 = [re.sub('\n', ' ', getText(a, iterStr)).strip() for a in lines2]
        real_meters2 = [met if re.sub("\s\s+", " ", real) == '' else real for real, met in zip(reals2, meters2)]
        return list(zip(text, real_meters)), list(zip(text2, real_meters2))

result_syl = []
result_word = []

for rt, dirs, files in os.walk('data/4B4V_poems'):
    global linecnt
    for fl in files:
        path = os.path.join(rt, fl)
        iterStr = '{http://www.tei-c.org/ns/1.0}'
        item_word, item_syl = getData(path, iterStr)
        result_syl += item_syl
        result_word += item_word
        iterStr = ''
        item_word, item_syl = getData(path, iterStr)
        result_syl += item_syl
        result_word += item_word

result_syl = [a for index, a in enumerate(result_syl) if a[0] != '']
result_word = [a for index, a in enumerate(result_word) if a[0] != '']

permutation = list(range(len(result_syl)))
random.shuffle(permutation)
print(permutation)
result_syl_shuffled = []
result_word_shuffled = []
for i in permutation:
    result_syl_shuffled.append(result_syl[i])
    result_word_shuffled.append(result_word[i])

f_csv = open('4B4V_wordbase.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f_csv)
for row in result_word_shuffled:
    wr.writerow(row)
f_csv.close()

f_csv = open('4B4V_syl.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f_csv)
for row in result_syl_shuffled:
    wr.writerow(row)
f_csv.close()


f_syl = open('4B4V_syl.csv', 'r', encoding='utf-8')
f_word = open('4B4V_wordbase.csv', 'r', encoding='utf-8')
syl_reader = csv.reader(f_syl)
word_reader = csv.reader(f_word)
for row1, row2 in zip(syl_reader, word_reader):
    print(row1[0])
    print(row2[0])




















