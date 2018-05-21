input_data = open('input.txt', 'w')

with open("processed_meters.txt") as meters_txt, open("processed_syllables.txt") as syllables_txt, open("lines_4B4V.txt") as lines_txt:
    for meters, syllables, line in zip(meters_txt, syllables_txt, lines_txt):
        len_meters = len(meters) - 1
        len_syllables = len(syllables.split())
        if len_meters != len_syllables:
            print(line)
            print(syllables)
        print('# of meters: ' + str(len_meters))
        print('# of syllables: ' + str(len_syllables) + '\n')
input_data.close()
meters_txt.close()
syllables_txt.close()