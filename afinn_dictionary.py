import json

file_afinn = open("AFINN-111.txt")
"""
we want to create a dictionary(K,V) from the file_afinn where we can later take the score from a key word directly.
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