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
from tkcalendar import Calendar



root = Tk()
n1 = DoubleVar()
n2 = DoubleVar()
r = DoubleVar()
conexion = sqlite3.connect("PythonEjercicio.db")
cursor = conexion.cursor()
root.title("PythonEjercicio")
root.config(cursor="plus",relief="ridge",bd=15)
root.resizable(0,0)
texto = StringVar()
texto.set("")


def calculadora():
    msg.grid_remove()
    crear.grid_remove()
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    sal.grid_remove()


    label = Label(root, text="Usuario:",font=("Arial Bold", 10))
    label.grid(column=1, row=0, padx=5, pady=5)
    label.config(textvariable=texto )



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
    
    por = Button(root, text="x", command=multiplicar,font=("Arial Bold", 10))
    por.grid(row=4,column=3, padx=5, pady=5, sticky="w", ipadx=8, ipady=5)
    
    entre = Button(root, text="/", command=dividir,font=("Arial Bold", 10))
    entre.grid(row=4,column=4, padx=5, pady=5, sticky="e", ipadx=8, ipady=5)
    
    Vlogs = Button(root, text="Editar", command=CRUD,font=("Arial Bold", 10))
    Vlogs.grid(row=3,column=5, padx=5, pady=5, sticky="w")
    
    salr = Button(root, text="Salir", command=salirAplicacion,font=("Arial Bold", 10))
    salr .grid(row=4,column=5, padx=5, pady=5, sticky="w")
    entryNum.focus()
    n1.set('')
    n2.set('')
    r.set('')
def borrar():
    n1.set('')
    n2.set('')
def sumar():
    try:
        r.set(  float(n1.get())  + float(n2.get()) )
        global operacion
        operacion = "+"
        commit()
        borrar()
        texto.set('se ha sumado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")
    except:
        texto.set("Error-\ningresa los campos correctamente")
        
        
        
def restar():
    try:
        r.set(  float(n1.get())  - float(n2.get()) )
        global operacion
        operacion = "-"
        commit()
        borrar()
        texto.set('se ha restado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")     
    except:
        texto.set("Error-\ningresa los campos correctamente") 

def multiplicar():
    try:
        r.set(  float(n1.get())  * float(n2.get()) )
        global operacion
        operacion = "*"
        commit()
        borrar()
        texto.set('se ha multiplicado correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")
    except:
        texto.set("Error-\ningresa los campos correctamente")   

def dividir():
    try:
        r.set(  float(n1.get())  / float(n2.get()) )
        global operacion
        operacion = "/"
        commit()
        borrar()
        texto.set('se ha dividido correctamente')
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")
    except:
        texto.set("Error-\ningresa los campos correctamente")       



def crearCuenta():
    Usr = entryUsr.get()
    Pass = entryPass.get()

    if len(Usr) == 0 or len(Pass) == 0:
        return mesg.set("Los campos son obligatorios")
    elif len(Usr) < 4:
        return mesg.set("El nombre de usuario es muy corto\nMinimo 4 caracteres")
    elif len(Usr) > 16:
        return mesg.set("El nombre de usuario es muy largo\nMaximo 16 caracteres")
    elif len(Pass) < 4:
        return mesg.set("La contraseña es muy corta\nMinimo 4 caracteres")
    elif len(Pass) > 16:
        return mesg.set("La contraseña es muy larga\nMaximo 16 caracteres")
    else:
        try:
            data = [Usr, Pass]
            cursor.execute("""INSERT INTO usuarios VALUES (NUll,?,?)""",data)
            conexion.commit()
            mesg.set("Cuenta creada!")
        except:
            return mesg.set("El nombre de usuario\nya esta en uso")
            

def salirAplicacion():
    
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
        try:
            raiz.destroy()
        except:
            pass
def acceder():
     
    Usr = entryUsr.get()
    Pass = entryPass.get()
    cursor.execute('''SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ? ''',(Usr, Pass))
    
    if cursor.fetchone():
        texto.set("Calculadora")
        calculadora()
    else:
    	mesg.set("Los datos son incorrectos!")


    conexion.commit()

def commit():
    locale.setlocale(locale.LC_ALL, 'es-MX')
    dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    fecha = dt.strftime("%d/%m/%y")
    hora =  dt.strftime("%I:%M:%S")


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
    entryUsr.focus()
    
def ConexionBDU():
    try:
        cursor.execute('''CREATE TABLE "usuarios"  
                        ("ID"	INTEGER NOT NULL UNIQUE,
                        "nombre"	VARCHAR(16) NOT NULL UNIQUE,
                        "contraseña"	VARCHAR(16) NOT NULL UNIQUE,
                        PRIMARY KEY("ID" AUTOINCREMENT))''') 

        
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
        
        conexion.commit()

    except:
        pass
def ventanaDeDatos():
    global datos
    datos = tkinter.Tk()
    datos.title("Hoja de datos")
    tree = ttk.Treeview(datos, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
    
    for row in cursor.execute("SELECT * FROM logs"):
        tree.insert("", tkinter.END, values=row)   
    tree.column("#1", anchor=tkinter.CENTER, width=25)
        
    tree.heading("#1", text="ID")
        
    tree.column("#2", anchor=tkinter.CENTER, width=50)
        
    tree.heading("#2", text="Primero")
        
    tree.column("#3", anchor=tkinter.CENTER, width=40)
    
    tree.heading("#3", text="/x-+")
    
    tree.column("#4", anchor=tkinter.CENTER, width=55)
    
    tree.heading("#4", text="Segundo")
    
    tree.column("#5", anchor=tkinter.CENTER, width=75)
    
    tree.heading("#5", text="Resultado")
    
    tree.column("#6", anchor=tkinter.CENTER, width=75)
    
    tree.heading("#6", text="Usuario")
    
    tree.column("#7", anchor=tkinter.CENTER, width=50)
    
    tree.heading("#7", text="Hora")
    
    tree.column("#8", anchor=tkinter.CENTER, width=125)
    
    tree.heading("#8", text="Fecha")

    menubar=Menu(datos)
    menuOpciones=Menu(menubar, tearoff=0)

    menuOpciones.add_command(label="actualizar", command=actualizarHojaDeDatos)
    menuOpciones.add_command(label="Salir", command=salirHojaDeDatos)
    menubar.add_cascade(label="Opciones", menu=menuOpciones)

    datos.resizable(0, 0)
    datos.config(cursor="plus",relief="ridge",bd=15, menu=menubar)      
    tree.pack()  

def salirHojaDeDatos():
    datos.destroy()

def actualizarHojaDeDatos():
    datos.destroy()
    ventanaDeDatos()

    
def crearRegistro():
    if e2.get().isdigit() and e4.get().isdigit():
        result()
        try:
            if e2.get() and e3.get() and e4.get() and resultadoAuto and e6.get() and newTime and newDate:
                datos=e2.get(),e3.get(),e4.get(),resultadoAuto,e6.get(),newTime,newDate
                cursor.execute("INSERT INTO logs VALUES(NULL,?,?,?,?,?,?,?)", (datos))
                conexion.commit()
                messagebox.showinfo("BBDD","Registro insertado con éxito")
            else:
                messagebox.showerror("Error-", "Introduce todos los campos!")
        except:
            messagebox.showerror("Error-", "Introduce todos los campos!")
    else:
        messagebox.showerror("Error-", "Introduce bien los campos!")
def result():
    global resultadoAuto
    if e3.get() == " + ":
        if float(e2.get()) + float(e4.get()) != float(e5.get()):
            valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
            if valor == "yes":
                resultadoAuto = float(e2.get()) + float(e4.get())
            else:
                resultadoAuto = float(e5.get())
        else:
            resultadoAuto = float(e5.get())
    if e3.get() == " - ":
        if float(e2.get()) + float(e4.get()) != float(e5.get()):
            valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
            if valor == "yes":
                resultadoAuto = float(e2.get()) - float(e4.get())
            else:
                resultadoAuto = float(e5.get())
        else:
            resultadoAuto = float(e5.get())
    if e3.get() == " x ":
        if float(e2.get()) + float(e4.get()) != float(e5.get()):
            valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
            if valor == "yes":
                resultadoAuto = float(e2.get()) * float(e4.get())
            else:
                resultadoAuto = float(e5.get())
        else:
            resultadoAuto = float(e5.get())
    if e3.get() == " / ":
        if float(e2.get()) + float(e4.get()) != float(e5.get()):
            valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
            if valor == "yes":
                resultadoAuto = float(e2.get()) / float(e4.get())
            else:
                resultadoAuto = float(e5.get())
        else:
            resultadoAuto = float(e5.get())


def actualizar():
    if e1.get():    
        if e2.get().isdigit() and e4.get().isdigit():
            result()
            cursor.execute("SELECT * FROM usuarios WHERE ID="+ e1.get())
            if cursor.fetchone() != None:
                 messagebox.showerror("Error-", "El indice no existe!")
            else:
                if e2.get() and e3.get() and e4.get() and resultadoAuto and e6.get() and newTime and newDate:
                    datos=e2.get(),e3.get(),e4.get(),resultadoAuto,e6.get(),newTime,newDate
                    cursor.execute("UPDATE logs SET Numero1=?, Operacion=?, Numero2=?, Resultado=?, Usuario=?, Hora=?, Fecha=? "+
                    "WHERE ID=" + e1.get(),(datos))
                    conexion.commit()
                    messagebox.showinfo("BBDD","Registro actualizado con éxito")
                else:
                    messagebox.showerror("Error-", "Introduce todos los campos!")
        else:
            messagebox.showerror("Error-", "Introduce bien los campos!")
    else:
        messagebox.showerror("Error-", "Introduce el indice\nque quieres actualizar!")

def borrarDatos():
    if e1.get():
        try:
            cursor.execute('''SELECT * FROM logs WHERE ID=''' + e1.get())
            cursor.execute("DELETE FROM logs WHERE ID=" + e1.get())
            conexion.commit()
            messagebox.showinfo("BBDD","Registro borrado con éxito")
        except:
            messagebox.showerror("Error-", "El registro\nno existe")
    else:
        messagebox.showerror("Error-", "Introduce el indice\nque quieres eliminar!")




def CRUD():
    usrList = [usr for usr in cursor.execute("SELECT nombre FROM usuarios")]
    global raiz
    raiz = tkinter.Tk()
    raiz.geometry("275x300")
    raiz.title("CRUD")
    raiz.resizable(0, 0)
    Label(raiz, text="   Editor de datos",font=("Arial Bold", 10)).grid(column=1, row=0, sticky="w")
    menubar=Menu(raiz)
    menuSalir=Menu(menubar, tearoff=0)
    crud=Menu(menubar, tearoff=0)

    crud.add_command(label="Añadir", command=crear)
    crud.add_command(label="Leer", command=ventanaDeDatos)
    crud.add_command(label="actualizar", command=actualizar)
    crud.add_command(label="Borrar", command=borrar)
    menubar.add_cascade(label="CRUD", menu=crud)

    menuSalir.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Salir", menu=menuSalir)

    raiz.config(cursor="plus",relief="ridge",bd=15, menu=menubar)

    l1=Label(raiz, text="ID:",font=("Arial Bold", 10))
    l1.grid(column=0, row=2, sticky="e")
    
    global e1
    e1=Entry(raiz)
    e1.grid(column=1, row=2, sticky="w")
    
    global l2
    l2=Label(raiz, text="Numero1:",font=("Arial Bold", 10))
    l2.grid(column=0, row=3, sticky="e")
    
    global e2
    e2=Entry(raiz)
    e2.grid(column=1, row=3, sticky="w")
    
    global l3
    l3=Label(raiz, text="Operacion:",font=("Arial Bold", 10))
    l3.grid(column=0, row=4, sticky="e")
    
    global e3
    e3=ttk.Combobox(raiz, justify="center",width=3,state="readonly", values=[" + ", " - ", " x ", " / "])
    e3.grid(column=1, row=4, sticky="w")
    
    global l4
    l4=Label(raiz, text="Numero2:",font=("Arial Bold", 10))
    l4.grid(column=0, row=5, sticky="e")
    
    global e4
    e4=Entry(raiz)
    e4.grid(column=1, row=5, sticky="w")
    
    global l5
    l5=Label(raiz, text="Resultado:",font=("Arial Bold", 10))
    l5.grid(column=0, row=6, sticky="e")
    
    global e5
    e5=Entry(raiz)
    e5.grid(column=1, row=6, sticky="w")
    
    global l6
    l6=Label(raiz, text="Usuario:",font=("Arial Bold", 10))
    l6.grid(column=0, row=7, sticky="e")

    global e6
    e6=ttk.Combobox(raiz, justify="left",width=10,state="readonly")
    e6['values']=usrList
    e6.grid(column=1, row=7, sticky="w")
    
    global l7
    l7=Label(raiz, text="Hora:",font=("Arial Bold", 10))
    l7.grid(column=0, row=8, sticky="e")
    
    global l8
    l8=Label(raiz, text="Fecha:",font=("Arial Bold", 10))
    l8.grid(column=0, row=9, sticky="e")
    
    global e8
    e8=Button(raiz, text="Seleccionar fecha", command=calendario,font=("Arial Bold", 10))
    e8.grid(column=1, row=9, sticky="e")
    
    b1=Button(raiz, text="Create", command=crearRegistro,font=("Arial Bold", 10))
    b1.place(x=0,y=242)
    
    b2=Button(raiz, text="Read", command=ventanaDeDatos,font=("Arial Bold", 10))
    b2.place(x=54,y=242)
    
    b3=Button(raiz, text="Update", command=actualizar,font=("Arial Bold", 10))
    b3.place(x=99,y=242)

    b4=Button(raiz, text="Delete", command=borrarDatos,font=("Arial Bold", 10))
    b4.place(x=156,y=242)   

    b6=Button(raiz, text="Exit", command=salirAplicacion,font=("Arial Bold", 10))
    b6.place(x=209,y=242)

    b7=Button(raiz, text="Seleccionar hora", command=selHora,font=("Arial Bold", 10))
    b7.grid(column=1, row=8, sticky="w")
    
    e1.focus()
    raiz.mainloop()  

def selHora():
    global newTime
    def salirHora():
        global newTime
        newTime = laHora.get() + ":" + losMinutos.get() + ":" + segundos.get()
        ventanaHora.destroy()
        print(newTime)
    ventanaHora = tkinter.Tk()
    ventanaHora.title("Hora")
    Label(ventanaHora, text="Hora",font=("Arial Bold", 10)).grid()
    laHora = Spinbox(ventanaHora,from_=0,to=23,wrap=True,width=25,justify=CENTER, xscrollcommand=True)
    laHora.grid()

    Label(ventanaHora, text="Minutos",font=("Arial Bold", 10)).grid()
    losMinutos = Spinbox(ventanaHora,from_=0,to=59,wrap=True,width=25, justify=CENTER)
    losMinutos.grid()

    Label(ventanaHora, text="Segundos",font=("Arial Bold", 10)).grid()
    segundos = Spinbox(ventanaHora,from_=0,to=59,wrap=True,width=25, justify=CENTER)
    segundos.grid()
    Button(ventanaHora, text="  Confirmar  ", command=salirHora,font=("Arial Bold", 10)).grid(pady=5)


 
    ventanaHora.resizable(0,0)
    ventanaHora.config(cursor="plus",relief="ridge",bd=15)
    ventanaHora.mainloop()




def calendario():
    global fecha 
    fecha = tkinter.Tk()
    fecha.title("Fecha")
    fecha.geometry("282x255")
    global newDate

    cal = Calendar(fecha, selectmode = 'day',
                year = 2021, month = 7,
                day = 19,font=("Arial Bold", 10))
    
    cal.grid(row=0 , column=0)
    def salirCalendario():
        global newDate
        newDate = cal.get_date()
        fecha.destroy()
    Button(fecha, text = "    Confirmar    ",
        command = salirCalendario,font=("Arial Bold", 10)).grid(pady=5)

    fecha.config(cursor="plus",relief="ridge",bd=15)
    fecha.resizable(0,0)
    fecha.mainloop() 

inicio()
root.mainloop() 
conexion.close()