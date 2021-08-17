from io import open

text_file = open("file.txt",  "a")
#Se agrega texto al final del archivo creado
#siempre cuando se abre con la letra "a" que es append
text_file.write("\nIt is always a good time to learn python.")
text_file.close()
