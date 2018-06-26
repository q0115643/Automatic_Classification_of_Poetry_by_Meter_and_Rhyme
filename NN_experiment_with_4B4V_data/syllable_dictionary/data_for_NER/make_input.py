unk_f = open('unk_words.txt', 'r', encoding='utf-8')
input_f = open('sylibifier_input.txt', 'w', encoding='utf-8')
for line in unk_f.read().splitlines():
    new_line = ''
    for c in line:
        new_line += c + ' '
    input_f.write(new_line.rstrip() + '\n')
