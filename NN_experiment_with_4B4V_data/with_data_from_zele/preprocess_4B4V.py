#########
#  for finding matching stressed/unstressed labels from given dataset of size 1000
#########
import re

processed_lines = open('processed_meters.txt', 'w')

cnt = 0
with open("4B4V_lines.txt") as lines_large_txt, open("lines.txt") as lines_small_txt, open("4B4V_meters.txt") as meters_small_txt:
    for line_large, line_small, meters_small in zip(lines_large_txt, lines_small_txt, meters_small_txt):
        line_large = re.sub('[^a-zA-Z]+', '', line_large)
        line_large = line_large.strip()
        line_large = line_large.lower()
        line_small = re.sub('[^a-zA-Z]+', '', line_small)
        line_small = line_small.strip()
        line_small = line_small.lower()
        meters_small = meters_small.strip()
        print(line_large)
        print(line_small)
        print(meters_small)
        if line_small == line_large:
            processed_lines.write(meters_small + '\n')
            cnt += 1

processed_lines.close()
lines_large_txt.close()
lines_small_txt.close()
meters_small_txt.close()
print(str(cnt))
