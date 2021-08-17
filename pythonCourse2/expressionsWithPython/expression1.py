from re import *

string1 = "We go to learn regular expressions"

searchText = "lear2"

#Método para encontrar una cadena en un texto retorna None si no se halla
if search(searchText, string1) is not None:
    print("We find the text")

else:
    print("We do not find the text")

#Este método me indica en que índice o posición comienza la palabra buscada en el texto
print(search("go", string1).start())

#Este método me indica en que índice o posición termina la palabra buscada en el texto
print(search("go", string1).end())

string2 = "Hello Word, Hello everyone!"

#Este método nos retorna en una lista con todas las veces
#que aparece nuestra palabra buscada en el texto
print(findall("Hello", string2))

#Con len toma la longitud o cantidad de valores
print(len(findall("Hello", string2)))
