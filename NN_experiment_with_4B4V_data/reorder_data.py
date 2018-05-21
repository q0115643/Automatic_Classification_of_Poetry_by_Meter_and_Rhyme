input_data = open('input.txt', 'w')

with open("processed_meters.txt") as meters_txt, open("processed_syllables.txt") as syllables_txt:
    for meters, syllables in zip(meters_txt, syllables_txt):
        len_meters = len(meters) - 1
        len_syllables = len(syllables.split())
        print('# of meters: ' + str(len_meters))
        print('# of syllables: ' + str(len_syllables) + '\n')
input_data.close()
meters_txt.close()
syllables_txt.close()