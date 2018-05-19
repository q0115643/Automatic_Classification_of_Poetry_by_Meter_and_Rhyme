# output: syllable txt file
#         " " is the boundary of syllables,
#         "|" is the boundary of words.


import re
import csv

WB = '|'
processed_syllables = open('processed_syllables.txt', 'w')
with open("syllables.txt") as syllable_txt, open("lines.txt") as lines_txt:
    for syllables, line in zip(syllable_txt, lines_txt):

        '''
        preprocess syllable.txt
        '''
        syllables = re.sub('[.]', '', syllables)
        syllables = re.sub('[^a-zA-Z\| ]+', ' ', syllables)
        syllables = re.sub('\([^)]+\)', '', syllables)
        syllables = re.sub("[\|]+", " ", syllables)
        syllables = re.sub("\s\s+", " ", syllables)
        syllables = syllables.strip()
        syllables = syllables.lower()

        '''
        preprocess lines.txt
        '''
        line = re.sub('[^a-zA-Z ]+', ' ', line)
        line = re.sub("\s\s+", " ", line)
        line = line.strip()
        line = line.lower()

        print("***before insertion of Word Boundary marker***")
        print("syllables: {0}\nline: {1}".format(syllables, line))
        syllab_len = len(syllables)
        line_len = len(line)

        '''
        add word boundaries to syllable.txt
        '''
        j = 0
        i = 0
        while i < line_len:
            if syllables[j]==' ' and line[i]!=' ':
                j += 1
            if line[i]==' ' and syllables[j]==' ':
                syllables = syllables[:j] + ' ' + WB + syllables[j:]
                j += len(WB)
            elif line[i]==' ':
                syllables = syllables[:j] + WB + syllables[j:]
                j += len(WB) - 1
            j += 1
            i += 1
        syllables = WB + ' ' + syllables + ' ' + WB

        print("***after insertion of Word Boundary marker***")
        print("syllables: {0}\nline: {1}\n".format(syllables, line))
        processed_syllables.write(syllables + '\n')
processed_syllables.close()
syllable_txt.close()
lines_txt.close()


'''
get the meters set
'''
processed_meters = open('processed_meters.txt', 'w')
with open('4B4V.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        line = row[1]
        processed_meters.write(line + '\n')
processed_meters.close()
myFile.close()
