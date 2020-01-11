import json

file_afinn = open("AFINN-111.txt")
"""
Creamos un diccionario con las palabras y su valor. Luego lo usaremos a la hora de cuantificar las palabras

dictionary example

{
"abandon": -2,
"abandoned": -2, 
...
}

"""
my_dictionary = open('my_dictionary.txt','w')

words = {}

for line in file_afinn:
    term, score = line.split("\t")
    words[term] = int(score)

json.dump(words, open("my_dictionary.txt",'w'))
my_dictionary.close()