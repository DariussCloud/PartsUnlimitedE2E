# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 06:59:56 2021

@author: dockt
"""

import datetime
import sqlite3
import locale
import pytz
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
n1 = StringVar()
n2 = StringVar()
r = StringVar()
locale.setlocale(locale.LC_ALL, 'es-MX')
dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
fecha = dt.strftime("%A %d %B %Y")
hora =  dt.strftime("%I:%M:%S")
conexion = sqlite3.connect("PythonEjercicio.db")
cursor = conexion.cursor()
root.title("PythonEjercicio")
root.config(cursor="plus",relief="ridge",bd=15)
root.resizable(0,0)

Id=StringVar()
Numero1=StringVar()
Numero2=StringVar()
Operacion=StringVar()
Resultado=StringVar()
Usuario=StringVar()
Fecha=StringVar()
Hora=StringVar()


def calculadora():
    msg.grid_remove()
    crear.grid_remove()
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    sal.grid_remove()

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
    
    Vlogs = Button(root, text="Ver los logs", command=CRUD,font=("Arial Bold", 10))
    Vlogs.grid(row=3,column=5, padx=5, pady=5, sticky="w")
    
    salr = Button(root, text="Salir", command=salirAplicacion,font=("Arial Bold", 10))
    salr .grid(row=4,column=5, padx=5, pady=5, sticky="w")
    
    connet = Button(root, text="Conectar", command=conexionBDD,font=("Arial Bold", 10))
    connet.grid(row=4,column=5, padx=5, pady=5, sticky="w")

def borrar():
    n1.set('')
    n2.set('')
def sumar():
    try:
        r.set(float( n1.get() ) + float(n2.get() ) )
        global operacion
        operacion = "+"
        commit()
        borrar()
        texto.set('se ha sumado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")
        
        
def restar():
    try:
        r.set( float( n1.get() ) - float(n2.get() ) )
        global operacion
        operacion = "-"
        commit()
        borrar()
        texto.set('se ha restado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")      

def multiplicar():
    try:
        r.set( float( n1.get() ) * float(n2.get() ) )
        global operacion
        operacion = "*"
        commit()
        borrar()
        texto.set('se ha multiplicado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")    

def dividir():
    try:
        r.set( float( n1.get() ) / float(n2.get() ) )
        global operacion
        operacion = "/"
        commit()
        borrar()
        texto.set('se ha dividido correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")       
def crearCuenta():
    Usr = entryUsr.get()
    Pass = str(entryPass.get())
    
    if len(Usr) == 0 or len(Pass) == 0:
        return mesg.set("Los campos son obligatorios")
    else:
        data = [Usr, Pass]
        cursor.execute("""INSERT INTO usuarios VALUES (?,?)""",data)
        conexion.commit()
        mesg.set("Cuenta creada!")
def salirAplicacion():
    
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
        raiz.destroy()
def acceder():
     
    Usr = entryUsr.get()
    Pass = entryPass.get()
    cursor.execute('''SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ? ''',(Usr, Pass))
    
    if cursor.fetchone():
        texto.set("Los datos son correctos!")
        calculadora()
    else:
    	mesg.set("Los datos son incorrectos!")


    conexion.commit()

def commit():
 
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
    messagebox.showinfo("BBDD","Registro insertado con exito")

def inicio():
    ConexionBDU()
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
    crear = Button(root, text="Crear cuenta", command=crearCuenta,font=("Arial Bold", 10))
    crear.grid(row=6, padx=5, pady=5)
    global sal
    sal = Button(root, text="Salir", command=salirAplicacion,font=("Arial Bold", 10))
    sal.grid(row=7, padx=5, pady=5)
    
    
    
def ConexionBDU():
    try:
        cursor.execute('''CREATE TABLE "usuarios"  
                           ("nombre"	VARCHAR(100) NOT NULL,
                            "contraseña"	VARCHAR(100) NOT NULL)''') 
        conexion.commit()
        messagebox.showinfo("BDU","La base de datos creado con exito")     
    except:
        messagebox.showwarning("¡Atención!","Ya estas conectado\na la base de datos")
        
def conexionBDD():
        
        try:

            cursor.execute("""CREATE TABLE "logs" (
        	"ID"	INTEGER NOT NULL UNIQUE,
        	"Numero1"	VARCHAR(100) NOT NULL,
        	"Operacion"	VARCHAR(5) NOT NULL,
        	"Numero2"	VARCHAR(100) NOT NULL,
        	"Resultado"	VARCHAR(100) NOT NULL,
        	"Usuario"	VARCHAR(50) NOT NULL,
        	"Hora"	VARCHAR(10) NOT NULL,
        	"Fecha"	VARCHAR(10) NOT NULL,
        	PRIMARY KEY("ID" AUTOINCREMENT)
            )""")
        
            messagebox.showinfo("BBDD","La base de datos creado con exito")

        except:
            messagebox.showwarning("¡Atención!","Ya estas conectado\na la base de datos")
    
def ventanaDeDatos():
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()    
    root = tkinter.Tk()
    root.title("Hoja de datos")
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
    for row in rows:
        tree.insert("", tkinter.END, values=row)   
    tree.column("#1", anchor=tkinter.CENTER)
        
    tree.heading("#1", text="ID")
        
    tree.column("#2", anchor=tkinter.CENTER)
        
    tree.heading("#2", text="PrimerNum")
        
    tree.column("#3", anchor=tkinter.CENTER)
    
    tree.heading("#3", text="Operacion")
    
    tree.column("#4", anchor=tkinter.CENTER)
    
    tree.heading("#4", text="SegundoNum")
    
    tree.column("#5", anchor=tkinter.CENTER)
    
    tree.heading("#5", text="Resultado")
    
    tree.column("#6", anchor=tkinter.CENTER)
    
    tree.heading("#6", text="Usuario")
    
    tree.column("#7", anchor=tkinter.CENTER)
    
    tree.heading("#7", text="Fecha")
    
    tree.column("#8", anchor=tkinter.CENTER)
    
    tree.heading("#8", text="Hora")

    tree.grid()   
def limpiar():
    Id.set('')
    Numero1.set('')
    Numero2.set('')
    Operacion.set('')
    Resultado.set('')
    Usuario.set('')
    Fecha.set('')
    Hora.set('')
    
def crearRegistro():
    if e2.get() and e3.get() and e4.get() and  e5.get() and e6.get() and e7.get() and e8.get():
        datos=e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()
        cursor.execute("INSERT INTO logs VALUES(NULL,?,?,?,?,?,?,?)", (datos))
        conexion.commit()
        messagebox.showinfo("BBDD","Registro insertado con éxito")
    else:
        messagebox.showerror("Error-", "Introduce todos los campos!")

def actualizar():
    try:
        cursor.execute('''SELECT * FROM logs WHERE ID=''' + e1.get())
        if cursor.fetchone():
            datos=e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()
            cursor.execute("UPDATE logs SET Numero1=?, Operacion=?, Numero2=?, Resultado=?, Usuario=?, Fecha=?, Hora=? "+
            "WHERE ID=" + e1.get(),(datos))
            conexion.commit()
            messagebox.showinfo("BBDD","Registro actualizado con éxito")
        else:
            messagebox.showerror("Error-", "El dato no existe")

    except:
        messagebox.showerror("Error-", "Introduce el indice\nque quieres actualizar!")

    


def borrarDatos():
    try:
    
        cursor.execute('''SELECT * FROM logs WHERE ID=''' + e1.get())
    except:
        messagebox.showerror("Error-", "Introduce el indice\nque quieres eliminar!")
    if cursor.fetchone():
        cursor.execute("DELETE FROM logs WHERE ID=" + e1.get())
        conexion.commit()
        messagebox.showinfo("BBDD","Registro borrado con éxito")
    else:
        messagebox.showerror("Error-", "El dato no existe")
    
def CRUD():
    global raiz
    raiz = tkinter.Tk()
    raiz.geometry("325x300")
    raiz.title("CRUD")
    raiz.config(cursor="plus",relief="ridge",bd=15)
    inf=Label(raiz, text="Editor de datos",font=("Arial Bold", 10))
    inf.grid(column=1, row=0)

    l1=Label(raiz, text="ID: ",font=("Arial Bold", 10))
    l1.grid(column=0, row=2, sticky="e")
    
    global e1
    e1=Entry(raiz, textvariable=Id)
    e1.grid(column=1, row=2, sticky="e")
    
    global l2
    l2=Label(raiz, text="Numero1:",font=("Arial Bold", 10))
    l2.grid(column=0, row=3, sticky="e")
    
    global e2
    e2=Entry(raiz, textvariable=Numero1)
    e2.grid(column=1, row=3, sticky="e")
    
    global l3
    l3=Label(raiz, text="Operacion:",font=("Arial Bold", 10))
    l3.grid(column=0, row=4, sticky="e")
    
    global e3
    e3=Entry(raiz,textvariable=Operacion)
    e3.grid(column=1, row=4, sticky="e")
    
    global l4
    l4=Label(raiz, text="Numero2:",font=("Arial Bold", 10))
    l4.grid(column=0, row=5, sticky="e")
    
    global e4
    e4=Entry(raiz,textvariable=Numero2)
    e4.grid(column=1, row=5, sticky="e")
    
    global l5
    l5=Label(raiz, text="Resultado:",font=("Arial Bold", 10))
    l5.grid(column=0, row=6, sticky="e")
    
    global e5
    e5=Entry(raiz,textvariable=Resultado)
    e5.grid(column=1, row=6, sticky="e")
    
    global l6
    l6=Label(raiz, text="Usuario:",font=("Arial Bold", 10))
    l6.grid(column=0, row=7, sticky="e")

    global e6
    e6=Entry(raiz,textvariable=Usuario)
    e6.grid(column=1, row=7, sticky="e")
    
    global l7
    l7=Label(raiz, text="Hora:",font=("Arial Bold", 10))
    l7.grid(column=0, row=8, sticky="e")
    
    global e7
    e7=Entry(raiz,textvariable=Fecha)
    e7.grid(column=1, row=8, sticky="e")
    
    global l8
    l8=Label(raiz, text="Fecha:",font=("Arial Bold", 10))
    l8.grid(column=0, row=9, sticky="e")
    
    global e8
    e8=Entry(raiz,textvariable=Hora)
    e8.grid(column=1, row=9, sticky="e")
    
    b1=Button(raiz, text="Create", command=crearRegistro,font=("Arial Bold", 10))
    b1.place(x=0,y=240)
    
    b2=Button(raiz, text="Read", command=ventanaDeDatos,font=("Arial Bold", 10))
    b2.place(x=54,y=240)
    
    b3=Button(raiz, text="Update", command=actualizar,font=("Arial Bold", 10))
    b3.place(x=99,y=240)

    b4=Button(raiz, text="Delete", command=borrarDatos,font=("Arial Bold", 10))
    b4.place(x=156,y=240)   

    b5=Button(raiz, text="Conect", command=conexionBDD,font=("Arial Bold", 10))
    b5.place(x=209,y=240)

    b6=Button(raiz, text="Exit",     command=salirAplicacion,font=("Arial Bold", 10))
    b6.place(x=265,y=240)

    # b7=Button(raiz, text="Clear", command=limpiar)
    # b7.place(x=290,y=250)

    raiz.mainloop()    
inicio()
root.mainloop() 
conexion.close()