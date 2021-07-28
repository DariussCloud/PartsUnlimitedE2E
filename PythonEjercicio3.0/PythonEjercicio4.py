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
root.config(cursor="hand1",relief="ridge",bd=15)
root.resizable(0,0)
texto = StringVar()
texto.set("")
newTime = None
newDate = None
resultadoAuto  = None

def inicio():
    vncmd = (root.register(on_validateN),'%S', '%P')

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
    entryUsr = Entry(root,validate="key", validatecommand=vncmd)
    entryUsr.grid(row=2, padx=5, pady=5)
    entryUsr.config(justify="center", state="normal")


    global labelPass
    labelPass = Label(root, text="Contraseña:",font=("Arial Bold", 10))
    labelPass.grid(row=3, padx=5, pady=5)
    
    
    global entryPass
    entryPass = Entry(root,validate="key", validatecommand=vncmd)
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

def acceder():
    Usr = entryUsr.get()
    Pass = entryPass.get()
    cursor.execute('''SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ? ''',(Usr, Pass))
    if cursor.fetchone():
        texto.set("Calculadora")
        calculadora()
    else:
    	mesg.set("Los datos son\nincorrectos!")
    conexion.commit()

def crearCuenta():
    Usr = entryUsr.get()
    Pass = entryPass.get()

    if len(Usr) == 0 or len(Pass) == 0:
        return mesg.set("Los campos\nson obligatorios")
    elif len(Usr) < 4:
        return mesg.set("El nombre de\nusuario es muy corto\nMinimo 4 caracteres")
    elif len(Pass) < 4:
        return mesg.set("La contraseña\nes muy corta\nMinimo 4 caracteres")
    else:
        try:
            data = [Usr, Pass]
            cursor.execute("""INSERT INTO usuarios VALUES (NUll,?,?)""",data)
            conexion.commit()
            mesg.set("Cuenta creada!")
        except:
            return mesg.set("El nombre de usuario\nya esta en uso")

def calculadora():
    msg.grid_remove()
    crear.grid_remove()
    labelUsr.grid_remove()
    labelPass.grid_remove()
    entryUsr.grid_remove()
    entryPass.grid_remove()
    acc.grid_remove()
    sal.grid_remove()

    vfcmd = (root.register(on_validateF),'%S','%P')

    label = Label(root,font=("Arial Bold", 10))
    label.grid(column=1, row=0, padx=5, pady=5)
    label.config(textvariable=texto )

    numero1 = Label(root, text="\nNumero 1       ",font=("Arial Bold", 10))
    numero1.grid(row=3, column=0, padx=5, pady=5, sticky="se")
    
    entryNum = Entry(root, justify=CENTER, textvariable=n1,validate="key", validatecommand=vfcmd)
    entryNum.grid(row=4, column=0, padx=5, pady=5, sticky="ne"  )
    
    
    numero2 = Label(root, text="\nNumero 2",font=("Arial Bold", 10))
    numero2.grid(row=3, column=1, padx=5, pady=5, sticky="s")
    
    entryNum2 = Entry(root, justify=CENTER, textvariable=n2,validate="key", validatecommand=vfcmd)
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
    global bEdit
    bEdit = Button(root, text="Editar", command=CRUD,font=("Arial Bold", 10))
    bEdit.grid(row=3,column=5, padx=5, pady=5, sticky="w")
    
    salr = Button(root, text="Salir", command=salirAplicacion,font=("Arial Bold", 10))
    salr .grid(row=4,column=5, padx=5, pady=5, sticky="w")
    entryNum.focus()

    n1.set('')
    n2.set('')
    r.set('')

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
        if float(n1.get()) != 0:
            r.set(  float(n1.get())  / float(n2.get()) )
            global operacion
            operacion = "/"
            commit()
            borrar()
            texto.set('se ha dividido correctamente')
        else:
            texto.set("Error-\nNo se puede dividir entre cero!")
    except ValueError:
        texto.set("Error-\ningresa los campos correctamente")
    except ZeroDivisionError:
        texto.set("Error-\nNo se puede dividir entre cero!")
    except:
        texto.set("Error-\ningresa los campos correctamente")       

def borrar():
    n1.set('')
    n2.set('')

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

def ConexionBDU():
    try:
        cursor.execute('''CREATE TABLE "usuarios"  
                        ("ID"	INTEGER NOT NULL UNIQUE,
                        "nombre"	VARCHAR(17) NOT NULL UNIQUE,
                        "contraseña"	VARCHAR(17) NOT NULL UNIQUE,
                        PRIMARY KEY("ID" AUTOINCREMENT))''') 

        cursor.execute("""CREATE TABLE "logs" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "Numero1"	VARCHAR(10) NOT NULL,
        "Operacion"	VARCHAR(1) NOT NULL,
        "Numero2"	VARCHAR(10) NOT NULL,
        "Resultado"	VARCHAR(10) NOT NULL,
        "Usuario"	VARCHAR(17) NOT NULL,
        "Hora"	VARCHAR(10) NOT NULL,
        "Fecha"	VARCHAR(10) NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
        )""")
        
        conexion.commit()
    except:
        pass

def CRUD():
    
    def wLog():
        if e1.get():
            cursor.execute("SELECT * FROM logs WHERE ID="+ e1.get())
            if cursor.fetchone() != None:
                id =  e1.get()
                limpiar()
                for log in cursor.execute("SELECT * FROM logs WHERE ID="+id):
                    e1.insert(0,log[0])
                    e2.insert(0,log[1])
                    e3.insert(0,log[2])
                    e4.insert(0,log[3])
                    e5.insert(0,log[4])
                    e6.insert(0,log[5])
                e3.config(state="readonly")
                e6.config(state="readonly")
            else:
                messagebox.showerror("Error-", "El indice no existe!")
        else:
            messagebox.showerror("Error-", "Introduce un indice!")
    
    bEdit.config(state=DISABLED)
    global usrList
    usrList = [usr for usr in cursor.execute("SELECT nombre FROM usuarios")]
    global raiz
    raiz = tkinter.Tk()
    raiz.geometry("275x300")
    raiz.title("CRUD")
    raiz.resizable(0, 0)
    vcmd = (raiz.register(on_validate),'%S', '%P')
    vfcmd = (raiz.register(on_validateF),'%S', '%P')
    Label(raiz, text="Editor de datos",font=("Arial Bold", 10), relief="ridge", borderwidth=5).grid(column=1, row=0, sticky="w")
    menubar=Menu(raiz)
    menuSalir=Menu(menubar, tearoff=0)
    crud=Menu(menubar, tearoff=0)
    opciones=Menu(menubar, tearoff=0)
    

    crud.add_command(label="Añadir", command=crearRegistro)
    crud.add_command(label="Leer", command=ventanaDeDatos)
    crud.add_command(label="actualizar", command=actualizar)
    crud.add_command(label="Borrar", command=borrarDatos)
    menubar.add_cascade(label="CRUD", menu=crud)

    opciones.add_command(label="Limpiar campos", command=limpiar)
    opciones.add_command(label="Escribir log", command=wLog)
    menubar.add_cascade(label="Opciones", menu=opciones)

    menuSalir.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Salir", menu=menuSalir)


    raiz.config(cursor="hand1",relief="ridge",bd=15, menu=menubar)

    l1=Label(raiz, text="ID:",font=("Arial Bold", 10))
    l1.grid(column=0, row=2, sticky="e")
    
    global e1
    e1=Entry(raiz,validate="key", validatecommand=vcmd)
    e1.grid(column=1, row=2, sticky="w")

    global l2
    l2=Label(raiz, text="Numero1:",font=("Arial Bold", 10))
    l2.grid(column=0, row=3, sticky="e")
    
    global e2
    e2=Entry(raiz,validate="key", validatecommand=vfcmd)
    e2.grid(column=1, row=3, sticky="w")
    
    global l3
    l3=Label(raiz, text="Operacion:",font=("Arial Bold", 10))
    l3.grid(column=0, row=4, sticky="e")
    
    global e3
    e3=ttk.Combobox(raiz, justify="center",width=2, values=["+", "-", "x", "/"],state="readonly")
    e3.grid(column=1, row=4, sticky="w")
    
    global l4
    l4=Label(raiz, text="Numero2:",font=("Arial Bold", 10))
    l4.grid(column=0, row=5, sticky="e")
    
    global e4
    e4=Entry(raiz,validate="key", validatecommand=vfcmd)
    e4.grid(column=1, row=5, sticky="w")
    
    global l5
    l5=Label(raiz, text="Resultado:",font=("Arial Bold", 10))
    l5.grid(column=0, row=6, sticky="e")
    
    global e5
    e5=Entry(raiz,validate="key", validatecommand=vfcmd)
    e5.grid(column=1, row=6, sticky="w")
    
    global l6
    l6=Label(raiz, text="Usuario:",font=("Arial Bold", 10))
    l6.grid(column=0, row=7, sticky="e")

    global e6
    e6=ttk.Combobox(raiz, justify="left",width=12,state="readonly")
    e6['values']=usrList
    e6.grid(column=1, row=7, sticky="w")
    
    global l7
    l7=Label(raiz, text="Hora:",font=("Arial Bold", 10))
    l7.grid(column=0, row=8, sticky="e")
    
    global l8
    l8=Label(raiz, text="Fecha:",font=("Arial Bold", 10))
    l8.grid(column=0, row=9, sticky="e")
    
    global b8
    global b7
    global b2
    b8=Button(raiz, text="Seleccionar fecha", command=calendario,font=("Arial Bold", 10))
    b8.grid(column=1, row=9, sticky="e")
    
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
    def salirEdit():
        try:
            bEdit.config(state=NORMAL)
            raiz.destroy()
        except:
            raiz.destroy()
    e1.focus()
    raiz.protocol("WM_DELETE_WINDOW", salirEdit)
    raiz.mainloop() 

def ventanaDeDatos():
    b2.config(state=DISABLED)
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
    def salirHojaDeDatos():
        datos.destroy()
        try:
            b2.config(state=NORMAL)
        except:
            pass
    menubar=Menu(datos)
    menuOpciones=Menu(menubar, tearoff=0)

    menuOpciones.add_command(label="actualizar", command=actualizarHojaDeDatos)
    menuOpciones.add_command(label="Salir", command=salirHojaDeDatos)
    menubar.add_cascade(label="Opciones", menu=menuOpciones)


    datos.resizable(0, 0)
    datos.config(cursor="hand1",relief="ridge",bd=15, menu=menubar)   
    datos.protocol("WM_DELETE_WINDOW",salirHojaDeDatos)
   
    tree.pack()  

def actualizarHojaDeDatos():
    datos.destroy()
    ventanaDeDatos()

def crearRegistro():
    if e2.get():
        if e3.get():
            if e4.get():
                if e5.get():
                    result()
                    if e6.get():
                        if resultadoAuto != None:
                            if newTime:
                                if newDate:
                                    datos=e2.get(),e3.get(),e4.get(),resultadoAuto,e6.get(),newTime,newDate
                                    cursor.execute("INSERT INTO logs VALUES(NULL,?,?,?,?,?,?,?)", (datos))
                                    conexion.commit()
                                    messagebox.showinfo("BBDD","Registro insertado con éxito")
                                    limpiar()
                                    e3.config(state="readonly")
                                    e6.config(state="readonly")
                                else:
                                    messagebox.showerror("Error-", "Introduce la fecha!")
                            else:
                                messagebox.showerror("Error-", "Introduce la hora!")
                        else:
                            pass
                    else:
                        messagebox.showerror("Error-", "Introduce el usuario!") 
                else:
                    messagebox.showerror("Error-", "Introduce el resultado!")
            else:
                messagebox.showerror("Error-", "Introduce el segundo numero!")
        else:
                messagebox.showerror("Error-", "Introduce el signo!")
    else:
        messagebox.showerror("Error-", "Introduce el primer numero!")

def actualizar():
    if e1.get():
        cursor.execute("SELECT * FROM logs WHERE ID="+ e1.get())
        if cursor.fetchone() != None:
            if e2.get():
                if e3.get():
                    if e4.get():
                        if e5.get():
                            result()
                            if e6.get():
                                if resultadoAuto != None:
                                    if newTime != None:
                                        if newDate != None:
                                            datos=e2.get(),e3.get(),e4.get(),resultadoAuto,e6.get(),newTime,newDate
                                            cursor.execute("UPDATE logs SET Numero1=?, Operacion=?, Numero2=?, Resultado=?, Usuario=?, Hora=?, Fecha=? "+
                                            "WHERE ID=" + e1.get(),(datos))
                                            conexion.commit()
                                            messagebox.showinfo("BBDD","Registro actualizado con éxito")
                                            limpiar()
                                            e3.config(state="readonly")
                                            e6.config(state="readonly")
                                        else:
                                            messagebox.showerror("Error-", "Introduce una fecha!") 
                                    else:
                                        messagebox.showerror("Error-", "Introduce una hora!")
                                else:
                                    pass
                            else:
                                messagebox.showerror("Error-", "Introduce un usuario!")                                    
                        else:
                            messagebox.showerror("Error-", "Introduce un resultado!")                                    
                    else:
                        messagebox.showerror("Error-", "Introduce \nel segundo numero!")                                    
                else:
                    messagebox.showerror("Error-", "Introduce un signo!")                                    
            else:
                messagebox.showerror("Error-", "Introduce \nel primer numero!")                                    
        else:
            messagebox.showerror("Error-", "El indice no existe!")                                    
    else:
        messagebox.showerror("Error-", "Introduce el indice que quieres actualizar!") 

def borrarDatos():

    if e1.get():
        cursor.execute("SELECT * FROM logs WHERE ID="+ e1.get())
        if cursor.fetchone() != None:
            cursor.execute("DELETE FROM logs WHERE ID=" + e1.get())
            conexion.commit()
            messagebox.showinfo("BBDD","Registro borrado con éxito")
        else:
            messagebox.showerror("Error-", "El indice no existe")

    else:
        messagebox.showerror("Error-", "Introduce el indice\nque quieres eliminar!")

def result():
    
    try:
        global resultadoAuto
        resultadoAuto = None
        if e3.get() == "+":
            if float(e2.get()) + float(e4.get()) != float(e5.get()):
                valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
                if valor == "yes":
                    resultadoAuto = float(e2.get()) + float(e4.get())
                else:
                    resultadoAuto = float(e5.get())
            else:
                resultadoAuto = float(e5.get())
        elif e3.get() == "-":
            if float(e2.get()) - float(e4.get()) != float(e5.get()):
                valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
                if valor == "yes":
                    resultadoAuto = float(e2.get()) - float(e4.get())
                else:
                    resultadoAuto = float(e5.get())
            else:
                resultadoAuto = float(e5.get())
        elif e3.get() == "x":
            if float(e2.get()) * float(e4.get()) != float(e5.get()):
                valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
                if valor == "yes":
                    resultadoAuto = float(e2.get()) * float(e4.get())
                else:
                    resultadoAuto = float(e5.get())
            else:
                resultadoAuto = float(e5.get())
        elif e3.get() == "/":
            if float(e2.get()) / float(e4.get()) != float(e5.get()):
                valor=messagebox.askquestion("Error-","El resultado que pusiste esta mal\nquieres que se ponga el resultado correcto automaticamente?")
                if valor == "yes":
                    resultadoAuto = float(e2.get()) / float(e4.get())
                else:
                    resultadoAuto = float(e5.get())
            else:
                resultadoAuto = float(e5.get())
    except NameError:
        return messagebox.showerror("Error-", "Introduce un signo!")
    except ValueError:
        return messagebox.showerror("Error-", "Introduce bien los campos!")

def limpiar():

    e1.grid_forget()
    e2.grid_forget()
    e3.grid_forget()
    e4.grid_forget()
    e5.grid_forget()
    e6.grid_forget()
    def limpiar2():
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global resultadoAuto
        global newDate
        global newTime

        resultadoAuto = None
        newDate = None
        newDate = None
        vcmd = (raiz.register(on_validate),'%S', '%P')
        vfcmd = (raiz.register(on_validateF),'%S', '%P')
        e1=Entry(raiz,validate="key", validatecommand=vcmd)
        e1.grid(column=1, row=2, sticky="w")

        e2=Entry(raiz,validate="key", validatecommand=vfcmd)
        e2.grid(column=1, row=3, sticky="w")

        e3=ttk.Combobox(raiz, justify="center",width=3, values=[" + ", " - ", " x ", " / "])
        e3.grid(column=1, row=4, sticky="w")
    
        e4=Entry(raiz,validate="key", validatecommand=vfcmd)
        e4.grid(column=1, row=5, sticky="w")

        e5=Entry(raiz,validate="key", validatecommand=vfcmd)
        e5.grid(column=1, row=6, sticky="w")

        e6=ttk.Combobox(raiz, justify="left",width=10)
        e6['values']=usrList
        e6.grid(column=1, row=7, sticky="w")
    limpiar2()

def selHora():
    global hora
    b7.config(state=DISABLED)
    hora = Tk()
    hora.resizable(0,0)
    hora.title("Hora")
    hora.config(cursor="hand1",relief="ridge",bd=15)


   


    def display_msg():
        global newTime
        m = min_sb.get()
        h = sec_hour.get()
        s = sec.get()
        t = f"La hora seleccionada es {m}:{h}:{s}.\nEs correcto?"
        res = messagebox.askquestion("Confirmar", t)
        if res == "yes":
            newTime = f"{m}:{h}:{s}"
            try:
                hora.destroy()
            except:
                pass
            try:
                b7.config(state=NORMAL)
            except:
                pass
        else:
            pass
    
    fone = Frame(hora)
    ftwo = Frame(hora)

    fone.pack(pady=10)
    ftwo.pack(pady=10)

    min_sb = Spinbox(
        ftwo,
        from_=0,
        to=23,
        wrap=True,
        width=2,
        state="readonly",
        font=("Arial Bold", 30),
        justify=CENTER
        )
    sec_hour = Spinbox(
        ftwo,
        from_=0,
        to=59,
        wrap=True,
        state="readonly",
        font=("Arial Bold", 30),
        width=2,
        justify=CENTER
        )

    sec = Spinbox(
        ftwo,
        from_=0,
        state="readonly",
        to=59,
        wrap=True,
        textvariable=sec_hour,
        width=2,
        font=("Arial Bold", 30),
        justify=CENTER
        )

    min_sb.pack(side=LEFT, fill=X, expand=True)
    sec_hour.pack(side=LEFT, fill=X, expand=True)
    sec.pack(side=LEFT, fill=X, expand=True)

    msg = Label(
        hora, 
        text="  Hora        Minutos      Segundos",
        font=("Arial Bold", 10),
        )
    msg.pack(side=TOP)

    actionBtn =Button(
        hora,
        text="Confirmar",
        font=("Arial Bold", 10),
        padx=5,

        command=display_msg
    )
    actionBtn.pack(pady=10)

    hora.protocol("WM_DELETE_WINDOW", display_msg)
    hora.mainloop()

def calendario():
    b8.config(state=DISABLED)
    global fecha 
    fecha = tkinter.Tk()
    fecha.title("Fecha")
    fecha.geometry("262x255")
    global newDate

    cal = Calendar(fecha, locale="es_MX",  selectmode = 'day',
                year = 2021, month = 7,
                day = 19,font=("Arial Bold", 10),
                showothermonthdays=False,
                showweeknumbers=False, 
                mindate=datetime.date(year=2020, month=1, day=1), 
                maxdate=datetime.date(year=2022, month=12, day=31))
    
    cal.grid(row=0 , column=0)
    def salirCalendario():
        t = "La fecha seleccionada es {}.\nEs correcto?".format(cal.get_date())
        v = messagebox.askyesno("Confirmar", t)
        if v:
            global newDate
            newDate = cal.get_date()
            try:
                b8.config(state=NORMAL)
            except:
                pass
            try:
                fecha.destroy()
            except:
                pass
        else:
            pass

        
    Button(fecha, text = "    Confirmar    ",
        command = salirCalendario,font=("Arial Bold", 10)).grid(pady=5)

    fecha.config(cursor="hand1",relief="ridge",bd=15)
    fecha.resizable(0,0)
    fecha.protocol("WM_DELETE_WINDOW", salirCalendario)

    fecha.mainloop() 

def on_validateN(text, new_text):
    if text.isalnum() and len(new_text) < 17:
        return True
    else:
        return False

def on_validateF(text, new_text):
    if all(c in "0123456789." for c in text) and len(new_text) < 10:
        return True
    else:
        return False

def on_validate(text, new_text):
    if text.isdecimal() and len(new_text) < 3:
        return True
    else:
        return False

def salirAplicacion():
    
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
        try:
            raiz.destroy()
        except:
            pass
        try:
            datos.destroy()
        except:
            pass
        try:
            hora.destroy()
        except:
            pass
        try:
            fecha.destroy()
        except:
            pass

inicio()
root.mainloop() 
conexion.close()