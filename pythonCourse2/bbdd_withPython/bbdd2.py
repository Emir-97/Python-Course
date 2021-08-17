import sqlite3

#AHORA SE INSERTARAN EN ESTE ARCHIVO VARIOS REGISTROS A LA TABLA PRODUCTS YA CREADA
myConnection = sqlite3.connect("Data Base 1")

myCursor = myConnection.cursor()

severalProducts = [

  ("Shirt", 10, "Sports"),
  ("Toy", 70, "Toys"),
  ("Book", 50, "Library")

]

#Método para insertar una lista en la tabla anteriormente creada
#En el parentesis con signos de interrogaación equivale a cada columna de la tabla

#myCursor.executemany("INSERT INTO PRODUCTS VALUES (?, ?, ?)", severalProducts)

myCursor.execute("SELECT * FROM PRODUCTS")

#Recura la información de la base de datos, en este caso de la tabla PRODUCTS
severalProducts = myCursor.fetchall()
#Imprime la información en forma de tuplas de los datos de la tabla PRODUCTS
print(severalProducts)

#Ahora solo imprime registro por registro
for product in severalProducts:
    print("Article name: ", product[0], " has a price of ", product[1], " Section: ", product[2])

#Actualiza y agrega los cambios a la tabla
myConnection.commit()

myConnection.close()
