import sys
from collections import Counter

dic = {}
with open('reduce', 'r') as file:
    for line in file:
        location, value = line.split('\t')
        #value = int(value)

        value = value.split('/')
        value[1] = value[1].replace('\n', '')

        if location in dic:
            dic[location]['score'] += int(value[0])
            if value[1] != "empty":
               dic[location]['hashtag'].append(value[1])
        else:
            dic[location] = {}

            dic[location]['score'] = int(value[0])
            dic[location]['hashtag'] = []
            if value[1] != "empty":
                dic[location]['hashtag'].append(value[1])

for key in dic.keys():
    res = [key for key, value in Counter(dic[key]['hashtag']).most_common()]
    print('{0}\t{1}'.format(key, str(dic[key]['score'])+" "+ str(res[:10])))
