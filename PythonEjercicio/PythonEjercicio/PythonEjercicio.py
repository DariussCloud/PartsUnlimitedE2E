import datetime
import sqlite3
import time
import locale
import pytz
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog


root = Tk()

"""

conexion = sqlite3.connect("PythonEjercicio.db")
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE logs (numero1 FLOAT(100), numero2 FLOAT(100), operacion VARCHAR(100), resultado VARCHAR(100), usuario VARCHAR(100), Hora VARCHAR(100))''')
conexion.commit
conexion.close()

"""

n1 = StringVar()
n2 = StringVar()
r = StringVar()
operacion = ""

def calculadora():
    

    
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    
       
    Label(root, text="Numero 1").grid(row=3, column=0, sticky="s", padx=5, pady=5)
    Entry(root, justify=CENTER, textvariable=n1).grid(row=4, column=0, sticky="w", padx=5, pady=5)

    Label(root, text="\nNumero 2").grid(row=3, column=1, sticky="n", padx=5, pady=5)
    Entry(root, justify=CENTER, textvariable=n2).grid(row=4, column=1, sticky="w", padx=5, pady=5)

    Label(root, text="\nResultado").grid(row=3, column=2, sticky="n", padx=5, pady=5)
    Entry(root, justify=CENTER, state=DISABLED, textvariable=r).grid(row=4, column=2, sticky="n", padx=5, pady=5)

    
    button = Button(root, text="Sumar", command=sumar).grid(row=5,column=0,sticky="w", padx=5, pady=5)
    button = Button(root, text="Restar", command=restar).grid(row=5,column=0,sticky="e", padx=5, pady=5)
    button = Button(root, text="Multiplicar", command=multiplicar).grid(row=5,column=1,sticky="w", padx=5, pady=5)
    button = Button(root, text="Dividir", command=dividir).grid(row=5,column=1,sticky="e", padx=5, pady=5)
    button = Button(root, text="Ver los log", command=logs).grid(row=5,column=2,sticky="w", padx=5, pady=5)
    button = Button(root, text="Salir", command=salir).grid(row=5,column=2,sticky="e", padx=5, pady=5)




def salir():
    root.destroy()

def acceder():
    
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()
    Usr = entryUsr.get()
    Pass = entryPass.get()
    cursor.execute('''SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ? ''',(Usr, Pass))
    
    if cursor.fetchone():
        texto.set("Los datos son correctos!")
        calculadora()
    else:
    	texto.set("Los datos son incorrectos!")


    conexion.close()


def borrar():
    n1.set('')
    n2.set('')
    operacion = ""
def sumar():
    r.set(float( n1.get() ) + float(n2.get() ) )
    operacion.join("+")
    commit()
    borrar()
    
def restar():
    r.set( float( n1.get() ) - float(n2.get() ) )
    operacion.join("-")
    commit()
    time.sleep(1)
    borrar()
    
def multiplicar():
    r.set( float( n1.get() ) * float(n2.get() ) )
    operacion.join("*")
    commit()
    borrar()
def dividir():
    r.set( float( n1.get() ) / float(n2.get() ) )
    operacion.join("/")
    commit()
    borrar()
    
def logs():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()
    
    for numero1, numero2, operacion, resultado, usuario, Hora in cursor.executemany("""SELECT * FROM logs"""):
        print(numero1, numero2, operacion, resultado, usuario, Hora)
    
    conexion.commit
    conexion.close()





def commit():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()




    locale.setlocale(locale.LC_ALL, 'es-MX')
    dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    hora = dt.strftime("%A %d %B %Y %I:%M:%S")

    num1 = n1.get()
    num2 = n2.get()
    str(num1)
    str(num2)

    cursor.execute('INSERT INTO logs (numero1, numero2, operacion, resultado, usuario, Hora) VALUES (?,?,?,?,?,?)',
        [
        num1,
        num2,
        operacion,
        r,
        entryUsr,
        hora,
        ])
    

    conexion.commit()
    conexion.close()




root.title("PythonEjercicio")
root.iconbitmap('linux.ico')
root.config(cursor="plus")
root.resizable(0,0)


labelUsr = Label(root, text="Usuario:")
labelUsr.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entryUsr = Entry(root)
entryUsr.grid(row=0, column=1, padx=5, pady=5)
entryUsr.config(justify="left", state="normal")


labelPass = Label(root, text="Contraseña:")
labelPass.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entryPass = Entry(root)
entryPass.grid(row=1, column=1, padx=5, pady=5)
entryPass.config(justify="center", show="*")


texto = StringVar()
texto.set("")
label = Label(root)
label.grid(row=2, column=1, padx=5, pady=5)
label.config()
label.config(textvariable=texto)

acc = Button(root, text="Acceder", command=acceder)
acc.grid(row=2, column=0, sticky="n", padx=5, pady=5)

root.mainloop()











