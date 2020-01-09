import json
from mrjob.job import MRJob
from mrjob.step import MRStep

file = open("AFINN-111.txt")
scores = {}
for line in file:
	term, score = line.split("\t")
	scores[term] = int(score)
file.close()

# print('Diccionario',puntuacion)


class MRWordFrequencyCount(MRJob):

	def mapper(self, _, line):
		try:
			linea = json.loads(line)
			tweet = linea.get("text")
			localizacion = linea.get("place").get("country_code")
			localizacion2 = linea.get("place").get("country")
			estado = linea.get("place").get("full_name")
			if (localizacion == "US" or localizacion2 == "United States"):

				location = linea.get("place").get("full_name").split(',')
				if len(location) == 2:
					location = location[1].strip()
				if len(location) == 2:
					score = 0
					words = linea.get("text").split()
					for word in words:

						if word in scores:
							score += scores[word]
						else:
							score += 0
						if word.startswith('#'):
							key = word
							value = location
						else:
							key = location
							value = score
					if score != 0:
						yield (key,value)
		except:
			None

	def reducer(self, key, values):
		suma = 0
		cont = 0
		for i in values:
			if key.startswith('#'):
				suma = 0
				cont += 1
			else:
				suma += i
				cont += 1

		dic = {}
		dic["total"] = suma
		dic["cont"] = cont
		yield (None, {key: {'total': suma , 'cont': cont}})

	def steps(self):
		return [MRStep(mapper=self.mapper, reducer=self.reducer)]


if __name__ == '__main__':
	MRWordFrequencyCount.run()