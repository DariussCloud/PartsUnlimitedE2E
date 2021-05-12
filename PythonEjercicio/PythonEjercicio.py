import datetime
import sqlite3
import time
import locale
import pytz
import string
from tkinter import *
from tkinter import messagebox



root = Tk()


n1 = StringVar()
n2 = StringVar()
r = StringVar()
signos = ["/", "*", "-", "+"]
relog_ = StringVar()
locale.setlocale(locale.LC_ALL, 'es-MX')
dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
fecha = dt.strftime("%A %d %B %Y")
hora =  dt.strftime("%I:%M:%S")








def calculadora():
    

    msg.grid_remove()
    crear.grid_remove()
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    sal.grid_remove()
    
    
    global numero1
    global entryNum
    global numero2
    global entryNum2
    global resultado
    global resultado2
    global mas
    global menos
    global por
    global entre
    global Vlogs
    global salr
    global back

    numero1 = Label(root, text="\nNumero 1       ",font=("Arial Bold", 10))
    numero1.grid(row=3, column=0, padx=5, pady=5, sticky="se")
    
    entryNum = Entry(root, justify=CENTER, textvariable=n1)
    entryNum.grid(row=4, column=0, padx=5, pady=5, sticky="ne"  )
    
    
    
    numero2 = Label(root, text="\nNumero 2",font=("Arial Bold", 10))
    numero2.grid(row=3, column=1, padx=5, pady=5, sticky="s")
    
    entryNum2 = Entry(root, justify=CENTER, textvariable=n2)
    entryNum2.grid(row=4, column=1, padx=5, pady=5, sticky="n")
    
    
    
    resultado = Label(root, text="\nResultado",font=("Arial Bold", 10))
    resultado.grid(row=3, column=2, padx=5, pady=5, sticky="s")
    
    resultado2 = Entry(root, justify=CENTER, state=DISABLED, textvariable=r)
    resultado2.grid(row=4, column=2, padx=5, pady=5, sticky="n")
    
    mas = Button(root, text="+", command=sumar,font=("Arial Bold", 10))
    mas.grid(row=3,column=3, padx=5, pady=5, sticky="w", ipadx=8, ipady=5)
    
    menos = Button(root, text="-", command=restar,font=("Arial Bold", 10))
    menos.grid(row=3,column=4, padx=5, pady=5, sticky="e", ipadx=8, ipady=5)
    
    por = Button(root, text="*", command=multiplicar,font=("Arial Bold", 10))
    por.grid(row=4,column=3, padx=5, pady=5, sticky="w", ipadx=8, ipady=5)
    
    entre = Button(root, text="/", command=dividir,font=("Arial Bold", 10))
    entre.grid(row=4,column=4, padx=5, pady=5, sticky="e", ipadx=8, ipady=5)
    
    Vlogs = Button(root, text="Ver los logs", command=logs,font=("Arial Bold", 10))
    Vlogs.grid(row=3,column=5, padx=5, pady=5, sticky="w")
    
    salr = Button(root, text="Salir", command=salir,font=("Arial Bold", 10))
    salr.grid(row=4,column=5, padx=5, pady=5, sticky="w")
    
    back = Button(root, text="⪻", command=remove,font=("Arial Bold", 10))
    back.grid(row=4,column=5, padx=5, pady=5, sticky="e")
    

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
    try:
        r.set(float( n1.get() ) + float(n2.get() ) )

        global operacion
        operacion = signos[3]
        commit()
        borrar()
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
        
        
        
def restar():
    try:
        
        r.set( float( n1.get() ) - float(n2.get() ) )

        global operacion
        operacion = signos[2]
        commit()
        borrar()
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
        
        
        
def multiplicar():
    try:
        r.set( float( n1.get() ) * float(n2.get() ) )

        global operacion
        operacion = signos[1]
        
        commit()
        borrar()
        
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
        
        
        
        
def dividir():
    try:
        r.set( float( n1.get() ) / float(n2.get() ) )
        global operacion
        operacion = signos[0]
        
        commit()
        borrar()
    
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
        
        
def logs():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()
    
    global asd
    
    for log in cursor.execute('''SELECT * FROM logs''').fetchall():
       
    
       asd = ""
       a = log[0] + log[1] + log[2] + " = " + log[3] + " Hecho por " + log[4] + " El dia " + log[5] + " A las " + log[6]
       strtexto = convertirTupla(a)
       asd += strtexto
       loglabel = Label(root, text=asd, font=("Arial Bold", 10))
       loglabel.config()
       loglabel.grid()        

        
    conexion.commit
    conexion.close()
  
      
def commit():
    conexion = sqlite3.connect("PythonEjercicio.db")
    cursor = conexion.cursor()




    
    resultado = r.get()
    num1 = str(n1.get())
    num2 = str(n2.get())
    Usr = str(entryUsr.get())
    

    cursor.execute('INSERT INTO logs (numero1, numero2, operacion, resultado, usuario, fecha, Hora) VALUES (?,?,?,?,?,?,?)',
        [
        num1,
        num2,
        operacion,
        resultado,
        Usr,
        fecha,
        hora
        ])
    

    conexion.commit()
    conexion.close()




root.title("PythonEjercicio")
root.iconbitmap('linux.ico')
root.config(cursor="plus",relief="ridge",bd=15)
root.resizable(0,0)



def time():
    
    
    clock = Label(root,font=("Arial Bold", 10))
    clock.grid(row=0,column=5,pady=5,padx=5)

    dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    hora =  dt.strftime("%I:%M:%S")
    clock.config(text=hora)
    clock.after(200,time)





def remove():
    numero1.grid_remove()
    entryNum.grid_remove()
    numero2.grid_remove()
    entryNum2.grid_remove()
    resultado.grid_remove()
    resultado2.grid_remove()
    mas.grid_remove()
    menos.grid_remove()
    por.grid_remove()
    entre.grid_remove()
    Vlogs.grid_remove()
    salr.grid_remove()
    back.grid_remove()
    texto.set("")
    
    inicio()
    
def inicio():




    global mesg
    mesg = StringVar()
    mesg.set("Iniciar  sesion")
    global msg
    msg = Label(root,font=("Arial Bold", 15))
    msg.grid(row=0)
    msg.config(textvariable=mesg, relief="ridge", justify="center")


    global labelUsr
    labelUsr = Label(root, text="Usuario:",font=("Arial Bold", 10))
    labelUsr.grid(row=1, padx=50, pady=5)
    labelUsr.config(justify="center")

    global entryUsr
    entryUsr = Entry(root)
    entryUsr.grid(row=2, padx=5, pady=5)
    entryUsr.config(justify="center", state="normal")


    global labelPass
    labelPass = Label(root, text="Contraseña:",font=("Arial Bold", 10))
    labelPass.grid(row=3, padx=5, pady=5)
    
    
    global entryPass
    entryPass = Entry(root)
    entryPass.grid(row=4, padx=5, pady=5)
    entryPass.config(justify="center", show="*")

    global texto
    texto = StringVar()
    texto.set("")
    label = Label(root, text="Usuario:",font=("Arial Bold", 10))
    label.grid(column=1, row=0, padx=5, pady=5)
    label.config(textvariable=texto )


    global button_acceder
    button_acceder = StringVar()
    button_acceder.set("Acceder")


    global acc
    acc = Button(root, textvariable=button_acceder, command=acceder,font=("Arial Bold", 10))
    acc.grid(row=5, padx=5, pady=5)

    global crear
    crear = Button(root, text="Crear cuenta", command=crear,font=("Arial Bold", 10))
    crear.grid(row=6, padx=5, pady=5)
    global sal
    sal = Button(root, text="Salir", command=salir,font=("Arial Bold", 10))
    sal.grid(row=7, padx=5, pady=5)
    
    
    
    
time()  
inicio()
root.mainloop()












