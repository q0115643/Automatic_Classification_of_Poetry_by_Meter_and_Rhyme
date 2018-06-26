import pyphen
dic = pyphen.Pyphen(lang='en_US')
print(dic.inserted('haversack'))
str = 'Have won the haven within my head'
strs = str.split(' ')
print(strs)
for w in strs:
    print(dic.inserted(w))
