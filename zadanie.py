def welcome(lista):
	for name in lista:
		if name.endswith('a'):
			print('Hej ' + name + ', miło Cię widzieć')
		else:
			print('Witaj ' + name + ', wybacz, to warsztaty dla dziewczyn')

lista = ['Magda', 'Ola', 'Adam']
welcome(lista)