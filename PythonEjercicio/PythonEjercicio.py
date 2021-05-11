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


n1 = StringVar()
n2 = StringVar()
r = StringVar()
signos = ["/", "*", "-", "+"]
sig = StringVar()
def calculadora():
    

    msg.grid_remove()
    crear.grid_remove()
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    

    a = Label(root, text="\nNumero 1",font=("Arial Bold", 10)).grid(row=3, column=0, padx=5, pady=5)
    b = Entry(root, justify=CENTER, textvariable=n1).grid(row=4, column=0, padx=5, pady=5)

    c = Label(root, justify=CENTER, textvariable = sig).grid(row=4, column=1, padx=5, pady=5, ipadx=5, sticky="w")
    
    
    d = Label(root, text="\n           Numero 2",font=("Arial Bold", 10)).grid(row=3, column=1, padx=5, pady=5)
    e = Entry(root, justify=CENTER, textvariable=n2).grid(row=4, column=1, padx=5, pady=5, sticky="e")

    f = Label(root, text="\nResultado",font=("Arial Bold", 10)).grid(row=3, column=2, padx=5, pady=5)
    g = Entry(root, justify=CENTER, state=DISABLED, textvariable=r).grid(row=4, column=2, padx=5, pady=5, sticky="e")

    
    h = Button(root, text="+", command=sumar,font=("Arial Bold", 10)).grid(row=3,column=3, padx=5, pady=5, sticky="w", ipadx=8, ipady=5)
    i = Button(root, text="-", command=restar,font=("Arial Bold", 10)).grid(row=3,column=4, padx=5, pady=5, sticky="e", ipadx=8, ipady=5)
    j = Button(root, text="*", command=multiplicar,font=("Arial Bold", 10)).grid(row=4,column=3, padx=5, pady=5, sticky="w", ipadx=8, ipady=5)
    k = Button(root, text="/", command=dividir,font=("Arial Bold", 10)).grid(row=4,column=4, padx=5, pady=5, sticky="e", ipadx=8, ipady=5)
    l = Button(root, text="Ver los logs", command=logs,font=("Arial Bold", 10)).grid(row=3,column=5, padx=5, pady=5, sticky="w")
    m = Button(root, text="Salir", command=salir,font=("Arial Bold", 10)).grid(row=4,column=5, padx=5, pady=5, sticky="w")
    n = Button(root, text="⪻", command=remove,font=("Arial Bold", 10)).grid(row=4,column=5, padx=5, pady=5, sticky="e")
    
    


def convertirTupla(tup):
    str =  ''.join(tup)
    return str





def crear():
    mesg.set("Cuenta creada!")
    
    
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()
    
    Usr = str(entryUsr.get())
    Pass = str(entryPass.get())
    data = [Usr, Pass]
    cursor.execute("""INSERT INTO usuarios VALUES (?,?)""",data)
    
    
    conexion.commit()
    conexion.close()
    

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
    	mesg.set("Los datos son incorrectos!")


    conexion.close()


def borrar():
    n1.set('')
    n2.set('')
    
def sumar():
    r.set(float( n1.get() ) + float(n2.get() ) )
    sig.set("+")
    global operacion
    operacion = signos[3]
    commit()
    borrar()
    
def restar():
    r.set( float( n1.get() ) - float(n2.get() ) )
    sig.set("-")
    global operacion
    operacion = signos[2]
    commit()
    borrar()
    
def multiplicar():
    r.set( float( n1.get() ) * float(n2.get() ) )
    sig.set("*")
    global operacion
    operacion = signos[1]
    commit()
    borrar()
def dividir():
    r.set( float( n1.get() ) / float(n2.get() ) )
    sig.set("*")
    global operacion
    operacion = signos[0]
    
    commit()
    borrar()

def logs():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()
    
    
    
    for log in cursor.execute('''SELECT * FROM logs''').fetchall():
       
        """
       asd = ""
        a = log[0],log[1],log[2]," = ",log[3]," Por ",log[4]," A las ",log[5]," Hora india"
        strtexto = convertirTupla(a)
        asd += strtexto
        Label(root, text=asd).grid()
    """
    
    asd = ""
    for log in cursor.execute('''SELECT * FROM logs''').fetchall():
        a = log[0],log[1],log[2],"=",log[3]," Por ",log[4]," A las ",log[5]," Hora india\n"

        strtexto = convertirTupla(a)
        print(strtexto)
        asd += strtexto

    messagebox.showinfo("Logs", asd)

      
        
        
        

        
        
        
    conexion.commit
    conexion.close()





def commit():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()




    locale.setlocale(locale.LC_ALL, 'es-MX')
    dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    hora = dt.strftime("%A %d %B %Y %I:%M:%S")
    resultado = r.get()
    num1 = str(n1.get())
    num2 = str(n2.get())
    Usr = str(entryUsr.get())
    

    cursor.execute('INSERT INTO logs (numero1, numero2, operacion, resultado, usuario, Hora) VALUES (?,?,?,?,?,?)',
        [
        num1,
        num2,
        operacion,
        resultado,
        Usr,
        hora,
        ])
    

    conexion.commit()
    conexion.close()




root.title("PythonEjercicio")
root.iconbitmap('linux.ico')
root.config(cursor="plus",relief="ridge",bd=15)
root.geometry('650x780')
root.resizable(0,0)


def remove():
    pass
    
    
    
def inicio():




    global mesg
    mesg = StringVar()
    mesg.set("Iniciar sesion")
    global msg
    msg = Label(root,font=("Arial Bold", 15))
    msg.grid(column=0)
    msg.config(textvariable=mesg, relief="ridge", justify="left")


    global labelUsr
    labelUsr = Label(root, text="Usuario:",font=("Arial Bold", 10))
    labelUsr.grid(row=1, column=0, padx=50, pady=5)
    labelUsr.config(justify="center")

    global entryUsr
    entryUsr = Entry(root)
    entryUsr.grid(row=2, column=0, padx=5, pady=5)
    entryUsr.config(justify="center", state="normal")


    global labelPass
    labelPass = Label(root, text="Contraseña:",font=("Arial Bold", 10))
    labelPass.grid(row=3, column=0, padx=5, pady=5)
    
    
    global entryPass
    entryPass = Entry(root)
    entryPass.grid(row=4, column=0, padx=5, pady=5)
    entryPass.config(justify="center", show="*")

    global texto
    texto = StringVar()
    texto.set("")
    label = Label(root, text="Usuario:",font=("Arial Bold", 10))
    label.grid(row=0, column=1, padx=5, pady=5)
    label.config(textvariable=texto )


    global button_acceder
    button_acceder = StringVar()
    button_acceder.set("Acceder")


    global acc
    acc = Button(root, textvariable=button_acceder, command=acceder)
    acc.grid(row=5, column=0, padx=5, pady=5)

    global crear
    crear = Button(root, text="Crear cuenta", command=crear)
    crear.grid(row=6, column=0, padx=5, pady=5)
inicio()
root.mainloop()











