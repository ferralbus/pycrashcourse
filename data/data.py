##----------------------------------------------------PINTAR UNA GRAFICA
#import matplotlib.pyplot as pyplot

#squares = []
#for i in range(0,5):
	#squares.append(i*i)
#pyplot.plot(squares)
#pyplot.show()

##----------------------------------GROSOR LINEA, FORMATEAR EJES, TITULO

#import matplotlib.pyplot as pyplot

#squares = []
#for i in range(0,5):
	#squares.append(i*i)
#pyplot.plot(squares,linewidth=5)
#pyplot.title("Numeros cuadrados",fontsize=24)
#pyplot.xlabel("Valor",fontsize=14)
#pyplot.ylabel("Cuadrado",fontsize=14)
#pyplot.tick_params(axis='both',labelsize=14)
#pyplot.show()

##NOTA:el primer valor de y se lo da por defecto a x=0. Correccion:

##------------------------------------------------------VALORES DE X e Y

#import matplotlib.pyplot as pyplot

#input_values = []
#output_values = []
#for i in range(1,6):
	#input_values.append(i)
	#output_values.append(i*i)
#print(input_values)
#print(output_values)
#pyplot.plot(input_values,output_values,linewidth = 5)
#pyplot.show()

##-----------------------------------------------------GRAFICO DE PUNTOS

#import matplotlib.pyplot as pyplot

#x_values = list(range(1,1001))
#y_values = [x**2 for x in x_values]

#pyplot.scatter(x_values,y_values,s=20)

##fijar rango de los ejes
#pyplot.axis([0,1100,0,1100000])

#pyplot.show()

##------------------colores

#import matplotlib.pyplot as pyplot

#x_values = list(range(1,1001))
#y_values = [x**2 for x in x_values]

#pyplot.scatter(x_values,y_values,c='red',edgecolor='none',s=20)
##también se puede hacer con RGB: c=(0,0,0.8)
#pyplot.axis([0,1100,0,1100000])

#pyplot.show()

##-------------------------------------------------------------COLORMAPS
#colorear gráfico en funcion a criterios. Ver matplotlib.org

#import matplotlib.pyplot as pyplot

#x_values = list(range(1,1001))
#y_values = [x**2 for x in x_values]

#pyplot.scatter(x_values,y_values,c=y_values,cmap=pyplot.cm.Blues,
	#edgecolor='none',s=20)

#pyplot.axis([0,1100,0,1100000])

#pyplot.show()

##------------------------------------------------------GRABAR A FICHERO

#import matplotlib.pyplot as pyplot

#x_values = list(range(1,1001))
#y_values = [x**2 for x in x_values]

#pyplot.scatter(x_values,y_values,c='red',edgecolor='none',s=20)

#pyplot.axis([0,1100,0,1100000])

##Sin recortar blancos alrededor
#pyplot.savefig('plot_1.png')
##Recortados blancos alrededor
#pyplot.savefig('plot_2.png',bbox_inches='tight')

##----------------------------------------------------------RANDOM WALKS

##Clase sin argumentos. Atributos: número de máximo de pasos del walk, 
##valores x e y de cada paso (necesita random.choice)
##crear en fichero random_walk.py
##método para calcular todos los puntos del walk

#import matplotlib.pyplot as pyplot

##importar clase, crear un RandoWalk, generar sus puntos y dibujar

#from random_walk import RandomWalk

#rm = RandomWalk(5000)
#rm.fill_walk()

#pyplot.scatter(rm.x_points,rm.y_points,s=1)
#pyplot.show()

##---------------------------------styling

#import matplotlib.pyplot as pyplot

#from random_walk import RandomWalk

#rm = RandomWalk(50000)
#rm.fill_walk()
#point_number = list(range(rm.max_points))

##poner principio y fin de otro color y más grades
#pyplot.scatter(rm.x_points,rm.y_points,c=point_number,
	#cmap=pyplot.cm.Blues, s=1)
#pyplot.scatter(rm.x_points[0],rm.y_points[0],c='green',s=70)
#pyplot.scatter(rm.x_points[-1],rm.y_points[-1],c='red',s=70)

##quitar ejes
#pyplot.axes().get_xaxis().set_visible(False)
#pyplot.axes().get_yaxis().set_visible(False)
#pyplot.show()

##-----------------------------------------------------------------PYGAL

##Crear clase dado con atributo numero de caras y metodo lanzar en otro
##fichero

#from die import Die

#die = Die(6)
#results = []
#for i in range(1,1000):
	#results.append(die.roll())
##print(results)

##calculamos frecuencias de resultados
#freqs = []
#for i in range(1,die.num_sides+1):
	#freq = results.count(i)
	#freqs.append(freq)
#print(freqs)

##-----------------pintar las frecuencias en un histograma

#import pygal
#from die import Die

#die = Die(6)
#results = []

#for i in range(1,1000):
	#results.append(die.roll())

#freqs = []

#for i in range(1,die.num_sides+1):
	#freq = results.count(i)
	#freqs.append(freq)

#hist = pygal.Bar()
#hist.title = "Results of rolling D6 1000 times"
#hist.x_labels = ['1','2','3','4','5','6']
#hist.x_title = 'Result'
#hist.y_title = 'Frequency'

#hist.add('D6',freqs)
#hist.render_to_file('die_visual.svg')

##-------------------lo mismo con dos dados

#import pygal
#from die import Die

#die_1 = Die(6)
#die_2 = Die(6)
#results = []

#for i in range(1,1000):
	#results.append(die_1.roll()+die_2.roll())

#freqs = []

#for i in range(2,die_1.num_sides*2+1):
	#freq = results.count(i)
	#freqs.append(freq)

#hist = pygal.Bar()
#hist.title = "Results of rolling 2 D6 1000 times"
#hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
#hist.x_title = 'Result'
#hist.y_title = 'Frequency'

#hist.add('2D6',freqs)
#hist.render_to_file('die_visual_2.svg')


#-------------------------------------------------------------------CSV

##--------------------------cabeceras a lista

#import csv

#filename = 'WorldCups.csv'
#with open(filename) as f:
	#reader = csv.reader(f)
	#header_row = next(reader)
	#print(header_row)
	
##-----------------------------enumerate

#lista = ['mercedes','fernando','alvaro','merceditas']
#for i,j in enumerate(lista):
	#print(i,j)

	
#import csv

#filename = 'WorldCups.csv'
#with open(filename) as f:
	#reader = csv.reader(f)
	#header_row = next(reader)
	#for i,j in enumerate(header_row):
		#print(i,j)

	
##---------------------------------extraer datos

#import csv
#import pygal

#filename = 'WorldCups.csv'
#with open(filename) as f:
	#reader = csv.reader(f)
	#header_row = next(reader)
	#for i,j in enumerate(header_row):
		#print(i,j)

##El puntero se queda en la primera fila con datos gracias al next
##De lo contrario el for de abajo cogería tb las cabeceras

	#goals = []
	#matches = []
	#ratio = []
	#year = []
	
	#for row in reader:
		#goals.append(int(row[6]))
		#matches.append(int(row[8]))
		#year.append(int(row[0]))
		#ratio.append(round(int(row[6])/int(row[8]),2))	
	#print(year,ratio)
#f.close()

#hist = pygal.Bar()
#hist.title = 'Historic World Cup Average Scored Goals per Match'
#hist.x_labels = year
#hist.x_title = 'Year'
#hist.y_title = 'Goals per Match'
#hist.add('goals',ratio)
#hist.render_to_file('goals_per_match.svg')

##-------------------------------otro: temperaturas

#import csv
#from matplotlib import pyplot as pyplot
#from datetime import datetime

#filename = 'sitka_weather_2014.csv'

##sacar temperaturas maximas

#with open(filename) as f:
	#reader = csv.reader(f)
	#header_row = next(reader)
	#max_temps = []
	#min_temps = []
	#dates = []

##A prueba de datos vacios

	#for row in reader:
		#try:
			#current_date = datetime.strptime(row[0],"%Y-%m-%d")
			#high = int(row[1])
			#low = int (row[3])
		#except ValueError:
			#print(current_date, 'missing_data')
		#else:
			#dates.append(current_date)
			#max_temps.append(high)	
			#min_temps.append(low)
		
##pintarlo en un plot

#fig = pyplot.figure(dpi=128,figsize=(10,6))
#pyplot.plot(dates,max_temps,c='red',alpha=0.3)
#pyplot.plot(dates,min_temps,c='blue',alpha=0.3)
#pyplot.fill_between(dates,max_temps,min_temps,facecolor='blue',alpha=0.1)

##formateado

#pyplot.title("Daily Temps Max Min, 2014",fontsize = 24)
#pyplot.xlabel('',fontsize=16)
#fig.autofmt_xdate()
#pyplot.ylabel("Temp (F)",fontsize=16)
#pyplot.tick_params(axis='both',which='major',labelsize=16)

#pyplot.show()

##------------------------------------------------------------------JSON

##-------------almacenar JSON a una lista

#import json

#filename = 'population_data.json'

#with open(filename) as f:
	#pop_data = json.load(f)
#f.close()

##ojo con el tratamiento de los numeros. Al sacar datos de 2010 hay
##valores de poblacion con decimales, ojo al imprimir

#for pop_dict in pop_data:
	#if pop_dict['Year'] == '2010':
		#country_name = pop_dict['Country Name']
		#population = int(float(pop_dict['Value']))
		#print(country_name + ": " + str(population))

##------------codigos de pais estandarizados en diccionario COUNTRIES
##(en otro fichero)

#from pygal_maps_world.i18n import COUNTRIES

#def get_country_code(country_name):
	#for code,name in COUNTRIES.items():
		#if country_name == name:
			#return name
		#else:
			#return None
			
##-----comprobar que country_names del fichero coinciden con los de i18n

#import json
#from country_codes import get_country_code

#filename = 'population_data.json'

#with open(filename) as f:
	#pop_data = json.load(f)
#f.close()

#errores = 0
#total = 0

#for pop_dict in pop_data:
	#if pop_dict['Year'] == '2010':
		#total += 1
		#country_name = pop_dict['Country Name']
		#population = int(float(pop_dict['Value']))
		#code = get_country_code(country_name)
		#if code:
			#print(code + ": " + str(population)) 
		#else:
			#print("ERROR--" + country_name)
			#errores += 1

#print("Paises totales: " + str(total))
#print("Errores: " + str(errores))

##-----------------------------world map

#import json
#import pygal.maps.world as pygalwm
#from country_codes import get_country_code

#filename = 'population_data.json'

#with open(filename) as f:
	#pop_data = json.load(f)
#f.close()

#cc_populations = {}

#for pop_dict in pop_data:
	#if pop_dict['Year'] == '2010':
		#country_name = pop_dict['Country Name']
		#population = int(float(pop_dict['Value']))
		#code = get_country_code(country_name)
		#if code:
			#cc_populations[code] = population

#cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
#for c,p in cc_populations.items():
	#if p <= 10000000:
		#cc_pops_1[c] = p
	#elif p <= 1000000000:
		#cc_pops_2[c] = p
	#else:
		#cc_pops_3[c] = p

#wm = pygalwm.World()
#wm.title = 'World Population in 2010 by country'
#wm.add('2010: <10m',cc_pops_1)
#wm.add('2010: <1b',cc_pops_2)
#wm.add('2010: >1b',cc_pops_3)

#wm.render_to_file('world_populations.svg')


##------------------------------------------------------------------APIs

#import requests

#url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#r = requests.get(url)
#print("Status Code: ", r.status_code)

#response_dict = r.json()
#print('Total Count:',response_dict['total_count'])
#print('Incomplete results:',response_dict['incomplete_results'])
#print(response_dict.keys())
#repo_dict = response_dict['items']
#print('Num. Repositorios:',len(repo_dict))
#repo_1 = repo_dict[0]
#print('\nKeys:',len(repo_1))
#for key in repo_1.keys():
	#print(key)
