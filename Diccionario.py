huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}

print (huespedes)#Imprime el diccionario
print (huespedes.items())#Imprime la separación por items del diccionario

print (huespedes.keys())#Imprime Los codigos o llavez de un diciconario
for key in huespedes:#Ciclo que imprime las llavez del diccionario
    print (key)#Imprime las llavez

print (huespedes.values())#Imprime los datos contenidos del diccionario (solo los elementos sin las llaves)
for key in huespedes:#Ciclo for que imprime los valores contenidos de las llavez
    print (huespedes[key])#Imprime las llavez
print()

for habitacion in huespedes: #Se le asigno el nombre habitaciones a las llavez, e imprime 
    print (habitacion,':',huespedes[habitacion])#imprime las llavez = habitacion separadas con ':' y luego el contenido dr cada llave
print()#imprime un "Enter"

for habitacion,huesped in huespedes.items():#ciclo que hace la separacion por intems del diciconario, e imprime llavez = habitacion y el contenido = huesped
    print (habitacion,':',huespedes[key])#imprime las llavez  = habitacion separas con un ':' y luego el contenido en una sola linea
    
for indice, key in enumerate(huespedes): #Ciclo que enumera el contenido y lo almacena en una variable llamada indice 
    print (indice+1,key,huespedes[key])# imprime la numeracion = indice, con las llavez y el contenido
print()#Imprime un "Enter"

print (huespedes[105])#imprime el valor de la llave 105
print (huespedes.get(105))#Devuelve un valor o contenido asociado a la llave 105

print ('====================================')

huespedes[102]='Fanny Lu'#Añadir, inserta o crea llave y contenido al diciconario
huespedes[107]='Don Omar'#Añadir, inserta o crea una llave y contenido al diciconario
huespedes.setdefault('109','Luis Miguel')#Inserta o crea un valor de una llave y el contenido

for huesped in huespedes.items(): #Ciclo que recorre y separa por items(llavez y contenido) del diccionario 
    print (habitacion,':',huesped)#imprime las llavez separas con un ':' y luego el contenido en una sola linea, de una sola habitacion
print()#Imprime un "Enter"

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}#Crea y añade registros al diccionario
huespedes.update(registroshoy)#Actualiza registros
for habitacion, huesped in huespedes.items():#ciclo que recorre, por habitacion = llavez, contenido y separa por items el diciconario
    print (habitacion,':',huesped)#imprime las llavez separas con un ':' y luego el contenido en una sola linea
print()#Imprime un "Enter"

print ('====================================')

huespedes[107]='Ricky Martin' #Añade llave y contenido al diciconario
print (huespedes)#Imprime el diccionario 

print ('====================================')


del huespedes[102]#elimina un valor del diccionario huespedes con la llave 102
huespedes.pop(202)#elimina el elemento de una lista en este caso 202
print(huespedes)#Imprime el diccionario huespedes

print ('====================================')

copia1=huespedes.copy()#duplica el valor del diccionario, en la avriaple copia1
print ('copia1: ',copia1)#imprime el diciconario ahora llamado copia1 con el inicio de 'copia1:'
copia2={}#crea una lista
copia2.update(huespedes)#Actualiza, la lista con los objetos del diccionario huesped
print ("copia2: ",copia2)#imprime la lista actualizada con los datos de el diciconario ahora llamado copia2 con el inicio de 'copia2:'

print ('====================================')

lista=[2,5,7,1]#Se creo una lista
diccio=dict.fromkeys(lista,"xxx")# se creo un diccionario con base a los numeros de la lsita, tomandolas como llavez y a cada llave se le asigno el valor de 'xxx'
print(diccio)#Se imprime el diccionario

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}#crear diciconario inverntario
print (inventario)#imprimir diccionario
inventario["cartera"].sort()#Organizar diccionario un la parte de "cartera"
print(inventario)#Imprime el diccionario
inventario["cartera"].remove("Monedas")#No funciona, debido a que no existe el elemento monedas en la lista del diciconario cartera
print(inventario)#Imprime el diconario
print(inventario.get("plata")[0])#Devuelve un valor o contenido asociado a la llave plata en la posicion 0
