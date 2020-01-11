import sys


dic = {}
vect = {}

with open('reduce', 'r') as file:
    for line in file:
        key, value = line.split('\t')
        if key.startswith('#'):
            if key not in vect:
                vect[key] = 1
            else:
                vect[key] += 1
        else:
            value = int(value)
            if value != 0:
                if key not in dic:
                    dic[key] = {}
                    dic[key]['total'] = {}
                    dic[key]['score'] = {}

                    dic[key]['total'] = 1
                    dic[key]['score'] = value
                else:
                    dic[key]['total'] += 1
                    dic[key]['score'] += value

for key in dic.keys():
    print('{0}\t{1}'.format(key, "Score : " + str(dic[key]['score'] ) + " Total : " + str(dic[key]['total'] ) + " / Media : " + str(dic[key]['score']/ dic[key]['total'])))

aux = {k: v for k, v in sorted(vect.items(), reverse=True, key=lambda item: item[1])[:10]}

for key in aux.keys():
    print('{0}\t{1}'.format(key, vect[key]))
