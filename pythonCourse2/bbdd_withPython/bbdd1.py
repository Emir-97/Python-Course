import sqlite3

#Se crea la conexión a la base de datos, y en connect() el nombre de la base de datos
myConnection = sqlite3.connect("Data Base 1")

#Se crea el cursor para poder crear luego una tabla
myCursor = myConnection.cursor()

#De esta manera creamos los componentes de la base de datos
#Se crea una tabla con sus distintas columnas, pero una vez ejecutada se debe comentar ya que fue creada una vez

#myCursor.execute("CREATE TABLE PRODUCTS (ARTICLE_NAME VARCHAR(50), PRICE INTEGER, SECTION VARCHAR(20))")

#Se inserta registro en la tabla creada, luego se comenta como con la tabla
myCursor.execute("INSERT INTO PRODUCTS VALUES('Ball', 30, 'Sports')")

#Con este método se confirman los cambios que se realicen en nuestra tabla
myConnection.commit()

#Cierro la conexión a la base de datos
myConnection.close()
