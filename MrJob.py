import json
from mrjob.job import MRJob
from mrjob.step import MRStep

file = open("AFINN-111.txt")
scores = {}
for line in file:
	term, score = line.split("\t")
	scores[term] = int(score)
file.close()

file = open("Redondo_words.csv")
puntuacion = {}
for line in file:
	term, score = line.split("\t")
	puntuacion[term] = float(score)
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
				valor = 0
				words = tweet.split()
				for word in words:
					if word in puntuacion.keys():
						valor += puntuacion[word]

					elif word in scores.keys():
						valor += scores[word] + 5

				if valor != 0:
					yield (estado, valor)
		except:
			None

	def reducer(self, key, values):
		cont = 0.0
		suma = 0.0
		for i in values:
			suma += i
			cont += 1

		dic = {}
		dic["total"] = suma
		dic["media"] = suma / cont
		# yield (key, dic)
		yield (None, {key: {'media': suma / cont, 'n_tweets': cont, "total": suma}})

	def steps(self):
		return [MRStep(mapper=self.mapper, reducer=self.reducer)]


if __name__ == '__main__':
	MRWordFrequencyCount.run()