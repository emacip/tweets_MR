import json
from mrjob.job import MRJob
from mrjob.step import MRStep

""" Abrimos el diccionario de palabras del txt y lo incluimos en un diccionario con el que poder trabajar """
file = open("AFINN-111.txt")
scores = {}
for line in file:
	term, score = line.split("\t")
	scores[term] = int(score)
file.close()

# print('Diccionario',puntuacion)

""" Esta clase se llama desde __name__ """
class MRWordFrequencyCount(MRJob):

	""" Se declara el mapper  """
	def mapper(self, _, line):

		""" Se ejecuta un try para el caso en el que alguna de las lineas de twitter falle y no se pueda leer """
		try:
			""" leemos linea por linea para procesar """
			linea = json.loads(line)

			""" Se incluyen las variables del pais para asegurarnos de que esta en USA """
			localizacion = linea.get("place").get("country_code")
			localizacion2 = linea.get("place").get("country")
			if (localizacion == "US" or localizacion2 == "United States"):

				""" Guardamos el codigo del estado """
				location = linea.get("place").get("full_name").split(',')
				if len(location) == 2:
					location = location[1].strip()
				if len(location) == 2:
					score = 0
					""" separamos el texto del tweet en palabras para despues leerlas una por una y comprobar si pertenecen a nuestro diccionario"""
					words = linea.get("text").split()
					key = location

					""" Recorremos las palabras para ver si pertenecen al diccionario y darle el valor """
					for word in words:
						if word in scores:
							score += scores[word]
						else:
							score += 0

						""" Si tienen hashtag contamos con las palabras para el trending topic  """
						if word.startswith('#'):
							yield (word, 1)
					""" Si los tweets tienen puntuacion los contamos para el reducer """
					if score != 0:
						yield (key,score)
		except:
			None

	""" comienza el reducer """
	def reducer(self, key, values):
		suma = 0
		count = 0
		""" saca todos los values para hacerlo en bucle"""
		for i in values:
			""" Si no es un hashtag lo cuenta para el analisis de sentimiento y le pone un contador  para la media y suma sus valores """
			if not key.startswith('#'):
				suma += i
				count += 1
			""" Si es un hashtag lom cuenta para hacer la cuenta de trending topics """
			else:
				count += 1


		""" Dependiendo del resultaod que queramos mostrar(hashtag o no hashtag) mostraremos el yield de una manera u otra """
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