from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

#--------------Functions------------------
#Se crea la ventana de salida de la aplicación, una venta OK/CANCEL
def outApp():
    value = messagebox.askokcancel("Out", "Do you like out the app?")
    if value == True:
        root.destroy()

def connectBBDD():
    myConnection = sqlite3.connect("Users")
    myCursor = myConnection.cursor()
    try:
       myCursor.execute('''
         CREATE TABLE DATAUSERS  (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME_USER VARCHAR(50),
         Password VARCHAR(50),
         LASTNAME VARCHAR(50),
         ADDRESS VARCHAR(50),
         COMMENTS VARCHAR(100))
         ''')
       messagebox.showinfo("Database", "Your databe was created successfully")
    except:
       messagebox.showwarning("Warning!!!!", "The Database already exists")
#Con esta función establezco todas mis variables como vacias.
def clearFields():
    myName.set("")
    myId.set("")
    myLastname.set("")
    myAddress.set("")
    myPassword.set("")
    #Establezco que se borre desde el primer caracter hasta el final
    comments_comments.delete('1.0', END)

def create():
    try:
        myConnection = sqlite3.connect("Users")
        myCursor = myConnection.cursor()
        varUser = [
          myName.get(),
          myPassword.get(),
          myLastname.get(),
          myAddress.get(),
          comments_comments.get('1.0', END)
        ]
        myCursor.execute('INSERT INTO DATAUSERS VALUES(NULL,?,?,?,?,?)',varUser)
        myConnection.commit()
        messagebox.showinfo("Information", "The register was created succesfully!!")
    except:
        messagebox.showwarning('Table does not exists', 'The table DATAUSERS cannot search!')

def read():
    myConnection = sqlite3.connect('Users')
    myCursor = myConnection.cursor()

    myCursor.execute("SELECT * FROM DATAUSERS WHERE ID=" + myId.get())
    theUser = myCursor.fetchall()

    for user in theUser:
        myId.set(user[0])
        myName.set(user[1])
        myPassword.set(user[3])
        myAddress.set(user[4])
        comments_comments.insert(1.0, user[5])
    myConnection.commit()

def update():
            myConnection = sqlite3.connect("Users")
            myCursor = myConnection.cursor()
            varUser = [
              myName.get(),
              myPassword.get(),
              myLastname.get(),
              myAddress.get(),
              comments_comments.get('1.0', END)
            ]
            myCursor.execute("UPDATE DATAUSERS SET NAME_USER='" +varUser[0] +
            "', Password='" +varUser[1]+
            "', LASTNAME='" +varUser[2]+
            "', ADDRESS='" +varUser[3]+
            "', COMMENTS='" +varUser[4]+
            "' WHERE ID="+ myId.get())
            myConnection.commit()
            messagebox.showinfo("Information", "The register was updated succesfully!!")

def delete1():
                myConnection = sqlite3.connect("Users")
                myCursor = myConnection.cursor()
                myCursor.execute("DELETE FROM DATAUSERS WHERE ID=" +myId.get())
                myConnection.commit()

                messagebox.showinfo("Database",  "The register was deleted with succesfully!!")

#--------------Menu-----------------------
menu1 = Menu(root)
root.config(menu=menu1, width=100, height=100)

menu_BBDD = Menu(menu1, tearoff=0)
menu_delete = Menu(menu1, tearoff=0)
menu_CRUD = Menu(menu1, tearoff=0)
menu_Help = Menu(menu1, tearoff=0)

menu1.add_cascade(label="BBDD", menu=menu_BBDD)
menu1.add_cascade(label="Delete", menu=menu_delete)
menu1.add_cascade(label="CRUD", menu=menu_CRUD)
menu1.add_cascade(label="Help", menu=menu_Help)

menu_BBDD.add_command(label="Connect", command=connectBBDD)
menu_BBDD.add_command(label="Exit", command=outApp)

menu_delete.add_command(label="Clear Fields", command=clearFields)

menu_CRUD.add_command(label="Create", command=create)
menu_CRUD.add_command(label="Read", command=read)
menu_CRUD.add_command(label="Update", command=update)
menu_CRUD.add_command(label="Delete", command=delete1)

menu_Help.add_command(label="License")
menu_Help.add_command(label="Abaout of...")
#-------------Frame------------------------
frame = Frame(root)
frame.pack()

#--------------Entrys----------------------
myId = StringVar()
myName = StringVar()
myLastname = StringVar()
myPassword = StringVar()
myAddress = StringVar()

id_entry = Entry(frame, textvariable=myId)
id_entry.grid(row=0, column=1, padx=10, pady=10)
id_entry.config(justify='right')

name_entry = Entry(frame, textvariable=myName)
name_entry.grid(row=1, column=1, padx=10, pady=10)
name_entry.config(justify='right')

password_entry = Entry(frame, textvariable=myPassword)
password_entry.grid(row=2, column=1, padx=10, pady=10)
password_entry.config(show="*", justify='right')

lastname_entry = Entry(frame, textvariable=myLastname)
lastname_entry.grid(row=3, column=1, padx=10, pady=10)
lastname_entry.config(justify='right')

address_entry = Entry(frame, textvariable=myAddress)
address_entry.grid(row=4, column=1, padx=10, pady=10)
address_entry.config(justify='right')

comments_comments = Text(frame, width=16, height=5)
comments_comments.grid(row=5, column=1, padx=10, pady=10)
#---------------Scroll Bar for comments_comments----------------
scrollbar1 = Scrollbar(frame, command=comments_comments.yview)
scrollbar1.grid(row=5, column=2, sticky="nsew")
comments_comments.config(yscrollcommand=scrollbar1.set)

#-----------------Labels-------------------
id_label = Label(frame, text="Id")
id_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

name_label = Label(frame, text="Name")
name_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

password_label = Label(frame, text='Password')
password_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

lastname_label = Label(frame, text="Lastname")
lastname_label.grid(row=3, column=0, sticky='e', padx=10, pady=10)

address_label = Label(frame, text="Address")
address_label.grid(row=4, column=0, sticky='e', padx=10, pady=10)

comments_label =Label(frame, text="Comments")
comments_label.grid(row=5, column=0, sticky='e', padx=10, pady=10)


#--------------------------Buttons---------------------------
#SE CREA UN NUEVO FRAME PARA LA PARTE INFERIOR DE LA GRÁFICA
#DONDE SE AGREGARÁN LOS BOTONES EN ELLA PARA NO AFECTAR EL DISEÑO
frame2 = Frame(root)
frame2.pack()

create = Button(frame2, text="Create", command=create)
create.grid(row=6, column=0, sticky='e', padx=15, pady=15)

read = Button(frame2, text="Read", command=read)
read.grid(row=6, column=1, sticky='e', padx=15, pady=15)

update = Button(frame2, text="Update", command=update)
update.grid(row=6, column=2, sticky='e', padx=15, pady=15)

delete = Button(frame2, text="Delete", command=delete1)
delete.grid(row=6, column=3, sticky='e', padx=15, pady=15)


root.mainloop()
