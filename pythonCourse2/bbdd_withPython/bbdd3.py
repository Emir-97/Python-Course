import sqlite3

myConnection = sqlite3.connect("Product Management")
myCursor = myConnection.cursor()

#SE CREA UNA TABLA PARA LA NUEVA BASE DE DATOS Product Management
#myCursor.execute('''
#   CREATE TABLE PRODUCTS2 (
#   ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   ARTICLE_NAME VARCHAR(50),
#   PRICE INTEGER,
#   SECTION VARCHAR(20))
#''')
#Se crean los registros para la tabla creada
#products = [

#    ("Bed", 100, "Furniture"),
#    ("Pants", 19, "Clothes"),
#    ("Sun Glasses", 25, "Fashion"),
#    ("Plate", 10, "Bazar")

#]

#Insertar los registros a la tabla
#myCursor.executemany("INSERT INTO PRODUCTS2 VALUES (NULL, ?, ?, ?)", products)

#Se inserta un registro en  la tabla, luego se lo comenta de ejecutado para no dar error
#myCursor.execute("INSERT INTO PRODUCTS2 VALUES (NULL, 'Guitar', 159, 'Musical instruments')")


#Como realizar una actualización o modificación de  los datos o registros de la tabla

#myCursor.execute("UPDATE PRODUCTS2 SET PRICE=35 WHERE ID = 1")


#AHORA PARA BORRAR DATOSO O REGISTROS DE LA TABLA SE REALIZA DE LA SIGUIENTE MANERA:
myCursor.execute("DELETE FROM PRODUCTS2 WHERE ID=5")


myConnection.commit()



myConnection.close()
