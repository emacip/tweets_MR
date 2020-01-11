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
			localizacion = linea.get("place").get("country_code")
			localizacion2 = linea.get("place").get("country")
			if (localizacion == "US" or localizacion2 == "United States"):

				location = linea.get("place").get("full_name").split(',')
				if len(location) == 2:
					location = location[1].strip()
				if len(location) == 2:
					score = 0
					words = linea.get("text").split()
					key = location
					for word in words:

						if word in scores:
							score += scores[word]
						else:
							score += 0
						if word.startswith('#'):
							yield (word, 1)

					if score != 0:
						yield (key,score)
		except:
			None

	def reducer(self, key, values):
		suma = 0
		count = 0
		for i in values:
			if not key.startswith('#'):
				suma += i
				count += 1
			else:
				count += 1
		if not key.startswith('#'):
			yield (key, {'Total': suma , 'Media': suma/count})
		else:
			yield (key, {'Cont': count})



	def steps(self):
		return [
			MRStep(mapper=self.mapper,
				   reducer=self.reducer)

		]


if __name__ == '__main__':
	MRWordFrequencyCount.run()