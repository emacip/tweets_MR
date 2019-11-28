import sys

dic = {}

for line in sys.stdin:
    location, value = line.split('\t')
    value = int(value)
    if location in dic:
        dic[location] += value
    else:
        dic[location] = value

for key in dic.keys():
    print('{0}\t{1}'.format(key, dic[key]))