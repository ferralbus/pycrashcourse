# ***********************************************************HELLO WORLD

# hello = "hello world!"
# print(hello)
# tabulador antes
# print("\t"+hello)
# salto de linea antes
# print("\n"+hello)

# ***************************************************************NUMBERS

# -----------Potencias

# print(2**2)

# ------------Número a texto

# print("Dos y dos son "+str(2+2))

# ****************************************************************LISTAS

# numeros = ["uno","dos","tres"]
# print(numeros)

# -----------Modificar

# numeros = ["uno","dos","tres"]
# numeros[0] = "cuatro"
# print(numeros)

# -------------Añadir al final

# numeros = []
# numeros.append("uno")
# print(numeros)

# ------------Insertar valor

# numeros = ["uno","tres"]
# numeros.insert(1,"dos")
# print(numeros)

# -----------------Borrar valor (no almacenable)

# numeros = ["uno","dos","tres"]
# print(numeros)
# del numeros[1]
# print(numeros)

# ------------------Borrar último valor (almacenable)

# numeros = ["uno","dos","tres"]
# print(numeros)
# ultimo = numeros.pop()
# print(numeros)
# print("He borrado el "+ultimo)

# -------------------Borrar cualquier valor (almacenable)

# numeros = ["uno","dos","tres"]
# print(numeros)
# ultimo = numeros.pop(0)
# print(numeros)
# print("He borrado el "+ultimo)

# ------------------Borrar por valor

# numeros = ["uno","dos","tres"]
# print(numeros)
# numeros.remove("uno")
# print(numeros)

# ----------------Ordenar creciente/decreciente

# numeros = ["uno","dos","tres"]
# print(numeros)
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)

# --------------Enseñar (sin modificar) ordenado creciente/decreciente

# numeros = ["uno","dos","tres"]
# print(numeros)
# print(sorted(numeros))
# print(numeros)
# print(sorted(numeros,reverse=True))
# print(numeros)

# ---------------Minimo, máximo, suma

# numeros = [1,2,3]
# print(numeros)
# print(min(numeros))
# print(max(numeros))
# print(sum(numeros))

# -----------------Tamaño de una lista

# numeros = [1,2,3]
# tamaño = len(numeros)
# print("La lista tiene "+str(tamaño)+" numeros")

# ***************************************************************LOOPING

# ------------------FOR loop

# numeros = [1,2,3]
# for numero in numeros:
    # print(numero)

# ------------Rangos

# for value in range(1,6):
    # print(value)

# imprime valores del 1 al 5, ojo.

# ------------Rangos con salto

# for value in range(2,9,2):
    # print(value)
# print("Números pares")

# ------------Construir lista a partir de rango

# numeros = list(range(1,11))
# print(numeros)

# Construir lista con for -permite hacer operaciones al contrario que la
 # anterior-

# potencias_dos = [value**2 for value in range(1,6)]
# print(potencias_dos)

# -----------------Slicing

# numeros = list(range(1,11))
# print(numeros)
# cinco_primeros = numeros[0:5]
# print(cinco_primeros)
# cinco_primeros_2 = numeros[:5]
# print(cinco_primeros_2)
# ultimos_desde_el_cinco = numeros[5:]
# print(ultimos_desde_el_cinco)
# cinco_ultimos = numeros[-5:]
# print(cinco_ultimos)
# print("Los tres últimos números son:")
# for numero in numeros[-3:]:
    # print(numero)

# ------------------Copiar listas

    # Usar siempre slices para copiar listas
    # Si se quiere copiar toda la lista usar [:]
    # IMPORTANTE: no se puede hacer lista1=lista2, sino lista2=lista1[:]
    # Si hacemos lista2=lista1 cada vez que se manipule una de las listas
    # python manipulará también la otra, serán iguales siempre.
    
# --------------Tuplas (listas no modificables)

# La única forma de sobreescribir una tupla es sobreescribiéndola entera
# numeros = (200,300)
# print("Tupla original:")
# for numero in numeros:
    # print(numero)
# print("Nueva tupla:")
# numeros = (400,500)
# for numero in numeros:
    # print(numero)
    
# ******************************************************Normas de estilo

# Indentar con cuatro espacios
# Evitar excesivas lineas en blanco
# Lineas de 80 caracteres
# Meter espacios en los iguales y en los operadores lógicos:
    # if a == 2: mejor que if a=2:

# *********************************************************IF STATEMENTS
    
# numeros = list(range(1,10))
# for numero in numeros:
    # if numero <= 3:
        # print("El número "+str(numero)+" es pequeño")
    # elif numero <=6:
        # print("El número "+str(numero)+" es mediano")
    # else:
        # print("El número "+str(numero)+" es grande")

# -------------------Expresiones lógicas
        
    # igualdad ==    -las mayúsculas importan-
    # desigualdad !=
    # mayor o igual >=
    # and: x and y
    # or: x or y
    
# -------------Chequear si un valor está/no está en una lista (in/not in)

# numeros = list(range(1,6))
# if 2 in numeros:
    # print("El número 2 está en la lista")
# else:
    # print("El número 2 no está en la lista")
    
# ------------Listas vacías

# numeros = []
# if numeros:
    # print("La lista tiene valores")
# else:
    # print("La lista está vacía")

# -------------Ejemplo vaciar una lista uno a uno

# numeros = list(range(1,4))
# print("La lista es:")
# print(numeros)
# print("Vaciando lista:")
# tamaño = len(numeros)
# for valor in range(1,tamaño+1):
    # if numeros:
        # numeros.pop()
        # print(numeros)
# if numeros:
    # print("La lista todavía está llena.")
    # print(numeros)
# else:
    # print("La lista está vacía")

# **********************************************************DICCIONARIOS    

# edades = {'mercedes':2,'alvaro':5}
# print(edades)
# print("la edad de mercedes es "+str(edades['mercedes']))
# prueba = {1:5,2:10,3:15}
# print(prueba)
# print("dos por cinco igual a "+str(prueba[2]))

# ----------------Añadir nuevas keys

# edades = {'mercedes':2,'alvaro':5}
# print(edades)
# edades['mama'] = 37
# print(edades)

# ---------------Diccionarios vacios

# edades = {}
# print(edades)
# edades['alvaro'] = 5
# print(edades)
# edades['mercedes'] = 2
# print(edades)

# -----------------Modificar valores

# alien = {'posicion_x':0,'velocidad':'alta'}
# print("La posicion inicial es: "+str(alien['posicion_x']))
# if alien['velocidad'] == 'baja':
    # incremental = 1
# elif alien['velocidad'] == 'media':
    # incremental = 2
# else:
    # incremental = 3
# modificamos la posicion:
# alien['posicion_x'] = alien['posicion_x'] + incremental
# print("La posicion final es: "+str(alien['posicion_x']))

# -------------------Borrar parejas de datos

# edades = {'mercedes':2,'alvaro':5}
# print(edades)
# del edades['alvaro']
# print(edades)

# -------------------Notación limpia

# edades = {
    # 'mercedes':2,
    # 'alvaro':5
    # }
# print(edades)

# -----Acceder a claves+valores de un diccionario -indentacion limpia de 
# -----prints-

# edades = {
    # 'alvaro':5,
    # 'mercedes':2,
    # 'mama':37,
    # 'papa':38
    # }
# for nombre, edad in edades.items():
    # print("La edad de " + 
        # nombre.title() + 
        # " es " + 
        # str(edad) + 
        # ".")
        
# ---------------Acceder solo a claves de un diccionario

# lenguajes = {
    # 'fernando':'python',
    # 'pele':'c',
    # 'roman':'perl'
    # }
# elegidos = ['pele','roman']
# for nombre in lenguajes.keys():
    # print(nombre)
    # if nombre in elegidos:
        # print("Hombre, " + 
        # nombre.title() + 
        # ", como tu por aquí!")

# ---------------Alternativa, quitar el .keys()

# lenguajes = {
    # 'fernando':'python',
    # 'pele':'c',
    # 'roman':'perl'
    # }
# elegidos = ['pele','roman']
# for nombre in lenguajes:
    # print(nombre.title())
    # if nombre in elegidos:
        # print("Hombre, " + 
        # nombre.title() + 
        # ", como tu por aquí!")

# ----------------Acceder a valores de un diccionario

# lenguajes = {
    # 'fernando':'python',
    # 'pele':'c',
    # 'roman':'python'
    # }
# for nombre in lenguajes.values():
    # print(nombre)
    
# -----------------ACCEDER A VARIOS VALORES SIN REPETIR

# lenguajes = {
    # 'fernando':'python',
    # 'pele':'c',
    # 'roman':'python'
    # }
# for valor in set(lenguajes.values()):
    # print(valor)

# nombres = {
# 'fernando':'yo',
# 'mercedes':'mujer',
# 'alvaro':'hijo',
# 'merceditas':'hija'
# }

# hombres=['fernando','alvaro']
# for persona in nombres:
    # if persona in hombres:
        # print(persona.title()+' es un hombre')
    # else:
        # print(persona.title()+' es una mujer')

# -----------------NESTING

# ---------------Lista de diccionarios

# alien_0 = {'color':'verde','puntos':5}
# alien_1 = {'color':'amarillo','puntos':10}
# alien_2 = {'color':'rojo','puntos':15}
# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
    # print(alien)
    
# ----------------Generar muchos diccionarios (30)

# aliens = []
# for i in range(30):
    # nuevo_alien = {'color':'verde','puntos':5,'velocidad':'lenta'}
    # aliens.append(nuevo_alien)
# Enseñar los 5 primeros
# for alien in aliens[:5]:
    # print(alien)
# print('...')
# print('Se han creado '+str(len(aliens))+' aliens.')
# Mirar los 3 primeros y si son verdes cambiar a amarillos, velocidad y
# puntos
# for alien in aliens[:3]:
    # if alien['color'] == 'verde':
        # alien['color'] = 'amarillo'
        # alien['puntos'] = 10
        # alien['velocidad'] = 'medio'
# for alien in aliens[:6]:
    # print(alien)

# --------------------Lista en un diccionario

# pizza = {'crust':'thick','toppings':['ham','bacon']}
# print('You ordered a '+pizza['crust']+'-crust pizza with:')
# for topping in pizza['toppings']:
    # print('\t' + topping)

# ---------------------Diccionario en un diccionario

# users = {
    # 'aeinstein':{
        # 'full_name':'albert',
        # 'surname':'einstein',
        # 'city':'bern'
        # },
    # 'mcurie':{
        # 'full_name':'marie',
        # 'surname':'curie',
        # 'city':'paris'
        # }
# }
# for user,info in users.items():
    # print('\nUsername: ' + user)
    # nombre = info['full_name'] + " " + info['surname']
    # ciudad = info['city']
    # print('\t'+nombre.title())
    # print('\t'+ciudad.title())


# ***********************************************WHILE LOOP & USER INPUT

# dato = input('Mete un dato: ')
# print('El dato es ' + dato)

# input() considera la entrada como string (no necesario str() arriba)

# edad = input('Cuantos años tienes: ')
# edad = int(edad)
# if edad >= 18:
    # print('Mayor')
# else:
    # print('Menor')

# ---------------OPERADOR MODULO

# entrada = input('Dime un numero: ')
# entrada = int(entrada)
# if entrada % 2 == 0:
    # print('Par')
# else:
    # print('Impar')

# ------------------WHILE LOOP

# numero = 1
# while numero <= 5:
    # print(numero)
# incremental
    # numero += 1
    
# mensaje = 'Dime palabra y la repito hasta que digas "quit"'
# mensaje += '\nCual es la palabra: '
# palabra = ""
# while palabra != 'quit':
    # palabra = input(mensaje)
    # if palabra != 'quit':
        # print(palabra) 

# -------------------USO DE FLAGS

# mensaje = 'Dime palabra y la repito hasta que digas "quit"'
# mensaje += '\nCual es la palabra: '
# activo = True
# while activo:
    # palabra = input(mensaje)
    # if palabra == 'quit':
        # activo = False
    # else:
        # print(palabra) 

# ---------------------BREAK

# mensaje = 'Dime palabra y la repito hasta que digas "quit"'
# mensaje += '\nCual es la palabra: '
# while True:
    # palabra = input(mensaje)
    # if palabra == 'quit':
        # break
    # else:
        # print(palabra)

# ----------------CONTINUE

# mensaje = 'Dime palabra y la repito hasta que digas "quit"'
# mensaje += '\nCual es la palabra: '
# activo = True
# while activo:
    # palabra = input(mensaje)
    # print(palabra)
    # if palabra != 'quit':
        # continue
    # else:
        # activo = False
        
# ----------------LISTAS Y WHILES

# usuarios_pendientes = ['fer','fat','ant']
# usuarios_confirmados = []

# while usuarios_pendientes:
    # saliente = usuarios_pendientes.pop()
    # print('Usuario saliente: ' + saliente.title())
    # usuarios_confirmados.append(saliente)

# print('\nUsuarios confirmados: ')
# for usuario in usuarios_confirmados:
    # print(usuario.title())
    
# -------------Quitar valor repetido en lista

# pets = ['cat','dog','fish','cat']
# active = True
# while active:
    # borrable = input('Cual quieres quitar?: ')
    # if borrable in pets:
        # while borrable in pets:
            # pets.remove(borrable)
        # print('Borrado!')
        # print(pets)
        # active = False
    # else:
        # print('No existe, prueba otro.')

# ----------------Meter valores en diccionario

# encuesta = {}
# activo = True
# while activo:
    # nombre = input('\nComo te llamas: ')
    # edad = input('Edad: ')
    # encuesta[nombre] = edad
    # invalido = True
    # while invalido:
        # seguir = input('\nSeguimos? (s/n)')
        # if seguir in ['s','n']:
            # invalido = False
            # if seguir == 'n':
                # activo = False
# for n,e in encuesta.items():
    # print(n.title() + ' tiene ' + e.title() + ' años.')

# *************************************************************FUNCIONES

# def greet_user():
    # """Decir hola"""
    # print('hola')
# greet_user()

# def greet_user(username):
    # """decir hola"""
    # print('hola, ' + username.title())
# greet_user('jesse')
# username es el parámetro, jesse es el argumento

# -----------------------positional arguments, el orden importa

# def greet_user(username, edad):
    # """dice hola"""
    # print('Hola ' + username.title() + ', tienes ' + str(edad) + 
    # ' años.')
# a='fernando'
# b=38
# greet_user(a,b)

# --------------------keyword arguments, el orden no importa

# def greet_user(username, edad):
    # """dice hola"""
    # print('Hola ' + username.title() + ', tienes ' + str(edad) + 
    # ' años.')
# greet_user(edad = 38,username = 'fernando')

# ----------------------argumento por defecto

# def greet_user(username, edad = 38):
    # """dice hola"""
    # print('Hola ' + username.title() + ', tienes ' + str(edad) + 
    # ' años.')
# greet_user('fernando')
# greet_user('antonio',40)


# ----------------------------return

# def suma_de_dos(sumando1, sumando2):
    # """suma de dos numeros"""
    # return (sumando1 + sumando2)
# salida = suma_de_dos(3,5)
# print(salida)

# ----------------------------hacer un argumento opcional

# def formatea_nombre(nombre,apellido,segundo_nombre=''):
    # """formatea nombres"""
    # if segundo_nombre:
        # nombre_completo = (nombre.title() + ' ' + segundo_nombre.title()
        # + ' ' + apellido.title())
        # atención, meter paréntesis si se quiere romper la linea
    # else:
        # nombre_completo = nombre.title() + ' ' + apellido.title()
    # return nombre_completo
# salida1 = formatea_nombre('fernando','torrico')
# salida2 = formatea_nombre('fernando','torrico','maria')
# print(salida1)
# print(salida2)

# --------------------devolver diccionario

# def construye_nombre(nombre,apellido):
    # """construye diccionario con nombre y apellido"""
    # persona = {'nombre':nombre,'apellido':apellido}
    # return persona
# salida = construye_nombre('fernando','torrico')
# print(salida)

# -------------------------pasar listas como argumentos

# def saluda_lista(nombres):
    # for nombre in nombres:
        # print('Hola ' + nombre.title())
# nombres = ['fernando','antonio','fatima']
# saluda_lista(nombres)

# -------------------------modificando listas

# sin funciones

# incompletas = ['casa','perro','silla']
# completas = []
# while incompletas:
    # imprimiendo = incompletas.pop()
    # print('\nImprimiendo: ' + imprimiendo)
    # completas.append(imprimiendo)
# print('\nFiguras impresas: ')
# for completa in completas:
    # print(completa)

# con funciones

# def imprimir(lista_completa,lista_incompleta):
    # """pasar objetos de la incompleta a la completa"""
    # while lista_incompleta:
        # imprimiendo = lista_incompleta.pop()
        # print('\nImprimiendo: ' + imprimiendo)
        # lista_completa.append(imprimiendo)
# def enseña_completa(lista_completa):
    # """muestra las figuras impresas"""
    # print('\nFiguras impresas: ')
    # for completa in lista_completa:
        # print(completa)
# incompletas = ['casa','perro','silla']
# completas = []
# imprimir(completas,incompletas)
# enseña_completa(completas)

# ---------------impedir que una lista que se pase como argumento cambie

# def imprimir(lista_completa,lista_incompleta[:])
# de esta manera la función no borrará la variable que se le pase como
# lista_incompleta

# ------------------pasar un número indefinido de argumentos como tupla

# la función hará una tupla con lo que se le pase de la siguiente forma:

# def hacer_pizza(*ingredientes):
    # print('\nHaciendo una pizza con los siguientes ingredientes:')
    # for ingrediente in ingredientes:
        # print('-' + ingrediente)
# hacer_pizza('pepperoni')
# hacer_pizza('queso','tomate','jamón')

# IMPORTANTE: si se usa este tipo de argumentos junto con otros, los del
# asterisco tienen que ir siempre los últimos para que se reconozcan

# def hacer_pizza(tamaño,*ingredientes):
    # print('\nHaciendo una pizza de ' +
    # str(tamaño) +' con los siguientes ingredientes:')
    # for ingrediente in ingredientes:
        # print('-' + ingrediente)
# hacer_pizza(12,'pepperoni')
# hacer_pizza(18,'queso','tomate','jamón')

# -------------pasar un número indefinido de argumentos como diccionario

# def hacer_perfil(nombre,apellido,**resto_datos):
    # """hace un diccionario con informacion del perfil"""
    # perfil = {}
    # perfil['nombre'] = nombre
    # perfil['apellido'] = apellido
    # for llave,valor in resto_datos.items():
        # perfil[llave] = str(valor)
    # print('Perfil creado:')
    # for llave,valor in perfil.items():
        # print('-' + llave + ': ' + valor)
# hacer_perfil('fernando','torrico',edad=38,altura = 178)

# -------------------------------------Modulos

# guardar las funciones en otro fichero module.py (mismo directorio)

# ----------------importar un módulo entero

# import module
# module.hacer_pizza(16,'queso','tomate','pepperoni','anchoas')

# ---------------importar funciones sueltas

# from module import hacer_pizza
# hacer_pizza(18,'jamon')

# -----------------dar un alias a un modulo

# import module as m
# m.hacer_pizza(16,'jamon')

# -------------------dar un alias a una función

# from module import hacer_pizza as hp
# hp(16,'jamon')

# -------------------importar todas las funciones

# from module import *
# hacer_pizza(3,'queso')

# ****************************************************************CLASES

# class Dog():
    # """hacer un perro"""
    # def __init__(self,name,age):
        # """inicializa nombre y edad"""
        # self.name = name
        # self.age = age
    # def sit(self):
        # """simula la accion de sentarse"""
        # print(self.name.title() + ' is now sitting.')
    # def roll_over(self):
        # """simula la accion de rodar"""
        # print(self.name.title() + ' rolled over!')
# my_dog = Dog('tapi',15)
# print('Mi perro se llama ' + my_dog.name.title())
# print(my_dog.name.title() + ' tiene ' + str(my_dog.age) + ' años')
# my_dog.sit()
# my_dog.roll_over()

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + self.año)
        # return nombre
# mi_coche = Coche('toyota','yaris','2011')
# print('Mi coche es un ' + mi_coche.get_descripcion())

# -----------------meter valores por defecto en el constructor

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
        # self.cuentakilometros = 0
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + self.año)
        # return nombre
    # def saca_kilometros(self):
        # print('Este coche tiene ' + str(self.cuentakilometros) + ' Km')
# mi_coche = Coche('toyota','yaris','2011')
# print('Mi coche es un ' + mi_coche.get_descripcion())
# mi_coche.saca_kilometros()

# -------------------modificar atributos

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
        # self.cuentakilometros = 0
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + self.año)
        # return nombre
    # def saca_kilometros(self):
        # print('Este coche tiene ' + str(self.cuentakilometros) + ' Km')
# mi_coche = Coche('toyota','yaris','2011')
# print('Mi coche es un ' + mi_coche.get_descripcion())
# mi_coche.cuentakilometros = 48000
# mi_coche.saca_kilometros

##esta forma de modificar atributos puede hacer que el programa meta
##valores no válidos, como negativos.

# -------------------modificar atributos con métodos

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
        # self.cuentakilometros = 0
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + self.año)
        # return nombre
    # def set_cuentakilometros(self,km):
        # """setter cuentakilometros (solo creciente)"""
        # if km >= self.cuentakilometros:
            # self.cuentakilometros = km
        # else:
            # print('No se pueden reducir los km!')
    # def saca_kilometros(self):
        # """escribe el valor de los km"""
        # print('Este coche tiene ' + str(self.cuentakilometros) + ' Km')
# mi_coche = Coche('toyota','yaris','2011')
# print('Mi coche es un ' + mi_coche.get_descripcion())
# mi_coche.saca_kilometros()
# mi_coche.set_cuentakilometros(48000)
# mi_coche.saca_kilometros()
# mi_coche.set_cuentakilometros(0)

# ------------------------------------------Inheritance

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
        # self.cuentakilometros = 0
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + str(self.año))
        # return nombre
    # def set_cuentakilometros(self,km):
        # """setter cuentakilometros (solo creciente)"""
        # if km >= self.cuentakilometros:
            # self.cuentakilometros = km
        # else:
            # print('No se pueden reducir los km!')
    # def saca_kilometros(self):
        # """escribe el valor de los km"""
        # print('Este coche tiene ' + str(self.cuentakilometros) + ' Km')

# class CocheElectrico(Coche):
    # def __init__(self,marca,modelo,año):
        # """inicializa atributos de la parent class"""
        # super().__init__(marca,modelo,año)

# mi_coche = CocheElectrico('tesla','model s',2016)
# print('Mi coche es un ' + mi_coche.get_descripcion())
# mi_coche.saca_kilometros()
# mi_coche.set_cuentakilometros(48000)
# mi_coche.saca_kilometros()
# mi_coche.set_cuentakilometros(0)

# ------------------añadimos atributos a la clase nueva

# class CocheElectrico(Coche):
    # def __init__(self,marca,modelo,año):
        # """inicializa atributos de la parent class"""
        # super().__init__(marca,modelo,año)
        # self.tamaño_bateria = 50
    # def describe_bateria(self):
        # """escribe la descripción de la bateria"""
        # print('Este coche tiene una batería de ' + 
        # str(self.tamaño_bateria) + ' kWh')
# mi_coche = CocheElectrico('tesla','model s',2016)
# print(mi_coche.get_descripcion())
# mi_coche.describe_bateria()

# ----------------------instancias como atributoss

# class Coche():
    # """intenta modelar un coche"""
    # def __init__(self,marca,modelo,año):
        # """constructor"""
        # self.marca = marca
        # self.modelo = modelo
        # self.año = año
        # self.cuentakilometros = 0
    # def get_descripcion(self):
        # """describe el coche en formato bonito"""
        # nombre = (self.marca.title() + ' ' + self.modelo.title() +
        # ' del año ' + str(self.año))
        # return nombre
    # def set_cuentakilometros(self,km):
        # """setter cuentakilometros (solo creciente)"""
        # if km >= self.cuentakilometros:
            # self.cuentakilometros = km
        # else:
            # print('No se pueden reducir los km!')
    # def saca_kilometros(self):
        # """escribe el valor de los km"""
        # print('Este coche tiene ' + str(self.cuentakilometros) + ' Km')

# class Battery():
    # """modeliza una bateria"""
    # def __init__(self,tamaño_bateria=70):
        # """constructor"""
        # self.tamaño_bateria = tamaño_bateria
    # def describe_bateria(self):
        # """imprime una descripción de la bateria"""
        # print('Esta es una batería de ' + 
        # str(self.tamaño_bateria) + ' kWh')

# class CocheElectrico(Coche):
    # def __init__(self,marca,modelo,año):
        # """inicializa atributos de la parent class"""
        # super().__init__(marca,modelo,año)
        # self.battery = Battery()

# mi_tesla = CocheElectrico('tesla','model x',2017)
# print(mi_tesla.get_descripcion())
# mi_tesla.battery.describe_bateria()

# ----------------------------importar clases de un modulo

# creamos un fichero distinto con la clase Car, car.py

# from car import Coche

# mi_coche = Coche('toyota','yaris',2011)
# print(mi_coche.get_descripcion())

# -------------------------importar todas las clases de un modulo

# from car import *

# mi_coche = Coche('seat','ibiza',1995)
# print(mi_coche.get_descripcion())

# ---------------------modulos preinstalados. OrderDict()

# OrderedDict(): clase que actua como un diccionario pero mantiene el 
# orden en el que se insertaron los valores

# from collections import OrderedDict

# mi_diccionario = OrderedDict()
# mi_diccionario['fernando'] = 'java'
# mi_diccionario['pele'] = 'javascript'
# for llave,valor in mi_diccionario.items():
    # print('Soy ' + llave.title() + ' y programo ' +
    # valor)


# ************************************************FICHEROS Y EXCEPCIONES

# -----------------------Abrir un fichero

# with open('pi.txt') as fichero:
    # contenido = fichero.read()
    # print(contenido)
# print('con linea en blanco')
# with open('pi.txt') as fichero:
    # contenido = fichero.read()
    # print(contenido.rstrip())
# print('sin linea en blanco -rstrip')
# #rstrip() quita los espacios blancos de la derecha del string

# -----------------------otros directorios

# mismo directorio donde está el programa
# with open('ficheros_texto\pi.txt') as fichero:
    # contenido = fichero.read()
    # print(contenido)
    
# #directorio distinto a donde está el programa
# #OJO: en windows \U quiere decir texto unicode y se lía. Dos opciones:
# #ruta_fichero = "C:\\Users\\ferna\\Desktop\\ficheros_texto\\pi.txt"
# with open(ruta_fichero) as fichero:
    # contenido = fichero.read()
    # print(contenido)
# #segunda opcion, la r informa de que es un raw string
# ruta_fichero = r"C:\Users\ferna\Desktop\ficheros_texto\pi.txt"
# with open(ruta_fichero) as fichero:
    # contenido = fichero.read()
    # print(contenido)

# ----------------------leer linea a linea

# nombre = 'pi.txt'
# with open(nombre) as fichero:
    # print('\nCon lineas al final')
    # for line in fichero:
        # print(line)
# with open(nombre) as fichero:
    # print('\nSin lineas al final (rstrip)')
    # for line in fichero:
        # print(line.rstrip())

# -----------------------lineas a una lista

# nombre = 'pi.txt'
# with open(nombre) as fichero:
    # lineas = fichero.readlines()
# #imprimimos en lineas nuevas
# for linea in lineas:
    # print(linea.rstrip())
# #imprimimos todo seguido
# pi_string = ''
# for linea in lineas:
    # pi_string += linea.rstrip()
# print(pi_string)
# print(len(pi_string))
# #imprimimos sin ningún espacio (strip)
# pi_string = ''
# for linea in lineas:
    # pi_string += linea.strip()
# print(pi_string)
# print(len(pi_string))

# ---------------------------ficheros grandes

# # ---------------------------Dividir texto en palabras

# filename = 'moby.txt'

# try:
	# with open(filename) as libro:
		# texto = libro.read()
	# libro.close()

# except FileNotFoundError:
	# print("No existe el fichero")

# else:
	# palabras = texto.split()
	# print("El libro "+filename+" tiene "+str(len(palabras))+" palabras.")
	

# # --------------------------ficheros multiples. 

# def cuenta_palabras(filename):
	# try:
		# with open(filename) as texto:
			# contenido = texto.read()
	# except FileNotFoundError:
		# print("El fichero no existe")
	# else:
		# palabras = contenido.split()
		# largo = len(palabras)
		# print("El fichero "+filename+" tiene "+str(largo)+" palabras.")
		
# ficheros = ['prueba.txt','no_existo.txt','prueba2.txt']

# for fichero in ficheros:
	# cuenta_palabras(fichero)

# # ----------------------- excepciones silenciosas

# def cuenta_palabras(filename):
	# try:
		# with open(filename) as texto:
			# contenido = texto.read()
	# except FileNotFoundError:
		# pass
	# else:
		# palabras = contenido.split()
		# largo = len(palabras)
		# print("El fichero "+filename+" tiene "+str(largo)+" palabras.")
		
# ficheros = ['prueba.txt','no_existo.txt','prueba2.txt']

# for fichero in ficheros:
	# cuenta_palabras(fichero)

# # ---------------------exportar datos a json

# import json

# filename = 'datos.json'

# numeros = [2,4,6,8,10]

# with open(filename,'w') as f_obj:
	# json.dump(numeros,f_obj)

# # -----------------------importar datos en fichero json

# import json

# with open('datos.json') as f_obj:
	# numeros = json.load(f_obj)

# print(numeros)



##**********************************************************TEST CASES

# #------------------------------Testear funciónes

# def divide_dos(dividendo,divisor):
	# try:
		# cociente = dividendo/divisor
	# except ZeroDivisionError:
		# print("Divisor cero.")
	# else:
		# return cociente

# def suma_dos(a,b):
	# return a + b
		
# #guardar en un módulo (operaciones.py)
# #testear funciones del módulo:

# import unittest
# from operaciones import *

# class OperacionesTestCase(unittest.TestCase):
	# def test_division(self):
		# cociente = division(6,3)
		# self.assertEqual(cociente,2)
	
	# def test_suma_dos(self):
		# suma = suma_dos(2,2)
		# self.assertEqual(suma,4)

# unittest.main()

# #---------------------------------Testear clases


		
