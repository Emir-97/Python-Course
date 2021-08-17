from re import *

names_list = [

   'Emir Zatta',
   '7asán Zatta',
   'Agustín Caballero',
   'Monica Miranda',
   'Monica Edith'
   ]

for element in names_list:
    #Con el metacarácter ^ en las expresiones significa que comienza o inicia
    if findall('^Agustín', element):
        print(element)

for element in names_list:
    #Con el metacarácter $ en las expresiones significa que termina con....
    if findall('Zatta$', element):
        print(element)
