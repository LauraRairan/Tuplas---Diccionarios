t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
print (t)#Imprime la tupla
print (len(t))#Tamaño de la tupla 


print ('=====================================')
print (t[0])#Imprime la posición 0 de la tupa que es 23 
print (t[3])#Imprime la posición 3 de la tupa que es ['perrito, 'gatito']
print (t[1:3])#Imprime los caracteres de la posicion 1 y excluye la posicion 3
print (t[3][1])#Imprime la posicion 3 de la tupla, con el contenido 1 de este, por ejemplo: gatito 


print ('====================================')
print (t[3])#Imprime la posicion 3 de la tupla
t[3].append('lorito')#En la posicion 3 de la tupla, se le añadio una nuevo
#caracter 'lorito' pasando la posicion 3 de
#estar asi: ['perrito', 'gatito'] asi: ['perrito', 'gatito', 'lorito']
print (t)#Imprime de neuvo la tupla

print ('====================================')
for elemento in t: #Ciclo para imprimir una tupla
    print (elemento)

print ('====================================')
for index in range(0,len(t)): #Ciclo para imprimir la tupla con el tamaño o el rango, usando un for i in range
    print (t[index]

print ('====================================')
if 'a' in t: #Un condicional, verificadno o bsucando un elemento de la tupla, por ejemplo 'a'
    print ("El elemento 'a' esta en la tupla")

print ('====================================')
lista=list(t) #a la variable lista, le asigno el contenido de la tupla e igualo la tupla a una lista llandola 'lista'
lista[1]='A' #En la posicion 1 de la lista, modifico el valor de 'a' por 'A'
print (lista) #imprimio  la nueva lista 

tupla=tuple(lista)#creo una nueva tupla, con el contenido de la lista, haciendo que la tupla ya creada tuviera
#los valores de la lista por ejemplo en la igualdad tupla = lista
print (tupla) #imprimio la tupla

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)] #Creo una lista
for x, y in l:#Ciclo for para imprimir una lista en filas y columas, separandolas con ':'
    print (x, ':', y)
