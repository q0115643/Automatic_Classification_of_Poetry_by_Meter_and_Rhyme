import csv


out_f = open('output.txt', 'r', encoding='utf-8')
processed_f = open('syl_dict_unk.csv', 'w')
wr = csv.writer(processed_f)
for line in out_f.read().splitlines():
    items = line.split(' ')
    word = ''
    syllable_form = ''
    for i, item in enumerate(items):
        char = item[0]
        tag = item[-1]
        word += char
        syllable_form += char
        if len(items) > i+1:
            next_tag = items[i+1][-1]
            if next_tag == 'b':
                syllable_form += '-'
    wr.writerow([word, syllable_form])
out_f.close()
processed_f.close()