from re import *

name1 = "Emir Zatta"
name2 = "Monica Miranda"
name3 = "Agustin Caballero"
name4 = "Naim Zatta"
code = "fdsufhiuqhfsiudhapuhfiuahoih324ndasjndsadsa"

#match() nos retorna verdadero si encontramos la palabra deseada e IGNORECASE
#hace que sea indistinta de mayúsculas y minúsculas
if match("emir", name1, IGNORECASE):
    print("We find Emir on the var")
else:
    print("We do not find Emir on the var")

#El punto "." sirve como un comodin para una letra
if match(".onica", name1, IGNORECASE):
    print("We find Monica on the var")
else:
    print("We do not find Monica on the var")

print()

#search() se utiliza para encontrar una cadena en un texto en este caso un número
if search("324", code):
    print("We find the number on the var")
else:
    print("We do not find the number on the var")
