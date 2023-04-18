from tkinter import *
from back import *
from popaps2 import *

def Interejercicio1():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")
    def back():
        raiz.destroy()

    def enviar():
        codigo=cuadroCodigo.get()
        nombre=cuadroNombre.get()
        horas=cuadroHoras.get()
        valor=cuadroValor.get()
        porcentaje=cuadroPorcentaje.get()

        datos=ejercicio_1(int(codigo),nombre,int(horas),int(valor),float(porcentaje))
        info=datos.salarioEmpleado()
        salarioBruto=info["salarioBruto"]
        salarioNeto=info["salarioNeto"]
        respuesta=f"Empleado de nombre {nombre} con codigo {codigo}, salario {salarioBruto} y salario neto {salarioNeto} "

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=6,column=0)


    Titulo=Label(frame,text="Ejercicio  1 ")
    Titulo.grid(row=0,column=0)
    
    textCodigo=Label(frame,text="Codigo Del Empleado")
    textCodigo.grid(row=3,column=0)
    cuadroCodigo=Entry(frame)
    cuadroCodigo.grid(row=3,column=1)
    
    textNombre=Label(frame,text="Nombre")
    textNombre.grid(row=3,column=2)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=3)

    textHoras=Label(frame,text="Horas trabajadas al mes")
    textHoras.grid(row=4,column=0)
    cuadroHoras=Entry(frame)
    cuadroHoras.grid(row=4,column=1)

    textValor=Label(frame,text="Valor por hora trabajada")
    textValor.grid(row=4,column=2)
    cuadroValor=Entry(frame)
    cuadroValor.grid(row=4,column=3)

    textPorcentaje=Label(frame,text="Porcentaje de retencion en la fuente")
    textPorcentaje.grid(row=5,column=0)
    cuadroPorcentaje=Entry(frame)
    cuadroPorcentaje.grid(row=5,column=1)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=9,column=2)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0,sticky=SW)
    raiz.mainloop()

def Interejercicio2():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def back():
        raiz.destroy()
    
    def enviar():
        lado=cuadroLado.get()

        datos=ejercicio_2(float(lado))
        area=datos.Area()
        altura=datos.Altura()
        perimetro=datos.Perimetro()
        respuesta=f"Area: {area}. Altura: {altura}. Perimetro: {perimetro}"
        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)
        

    Titulo=Label(frame,text="Ejercicio  2 ")
    Titulo.grid(row=0,column=0,columnspan=3)

    textLado=Label(frame,text="Lado del triangulo")
    textLado.grid(row=3,column=0,columnspan=3)

    cuadroLado=Entry(frame)
    cuadroLado.grid(row=4,column=0,columnspan=3)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=5,column=0,columnspan=3)


    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0,sticky=SW)
    raiz.mainloop()

def Interejercicio3():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def back():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()
        b=cuadroB.get()

        datos=ejercicio_3(int(a),int(b))
        mensaje=datos.desicion()

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)
        Titulo=Label(frame,text=mensaje,fg="red")
        Titulo.grid(row=7,column=0,columnspan=4)



    Titulo=Label(frame,text="Ejercicio  3 ")
    Titulo.grid(row=0,column=0,columnspan=4)

    textA=Label(frame,text="Valor de A")
    textA.grid(row=3,column=0)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=1)
    
    textB=Label(frame,text="Valor de B")
    textB.grid(row=3,column=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=3,column=3)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,columnspan=3)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0,sticky=SW)
    raiz.mainloop()

def Interejercicio4():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def back():
        raiz.destroy()
    def enviar():
        inscripcion=cuadroNum.get()
        nombre=cuadroNombre.get()
        patrimonio=cuadroPatr.get()
        estrato=cuadroEstrato.get()

        datos=ejercicio_4(inscripcion,nombre,int(patrimonio),int(estrato))
        total=datos.pago()
        respuesta=f"el estudiante {nombre} con numero de inscripcion{inscripcion}, debe pagar {total} tiene un patrimonio {patrimonio}"
        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)


    Titulo=Label(frame,text="Ejercicio 4")
    Titulo.grid(row=0,column=0,columnspan=4)
    
    textNum=Label(frame,text="Numero de Inscripcion")
    textNum.grid(row=3,column=0)
    cuadroNum=Entry(frame)
    cuadroNum.grid(row=3,column=1)
    
    textNombre=Label(frame,text="Nombre")
    textNombre.grid(row=3,column=2)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=3)

    textPatr=Label(frame,text="Patrimonio")
    textPatr.grid(row=4,column=0)
    cuadroPatr=Entry(frame)
    cuadroPatr.grid(row=4,column=1)

    textEstrato=Label(frame,text="Estrato Social")
    textEstrato.grid(row=4,column=2)
    cuadroEstrato=Entry(frame)
    cuadroEstrato.grid(row=4,column=3)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,columnspan=3)


    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0,sticky=SW)
    raiz.mainloop()

def Interejercicio5():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    cont=0

    def back():
        raiz.destroy()

    def enviar():

        nombre=cuadroNombre.get()
        horas=cuadroHoras.get()
        salario=cuadroSalario.get()

        datos=ejercicio_5(nombre,int(salario),int(horas))
        total=datos.pago()
        if total:
            respuesta=f"empleado {nombre} de salario {total}"
            Titulo=Label(frame,text="Respuesta",fg="red")
            Titulo.grid(row=5,column=0,columnspan=4)   
            Titulo=Label(frame,text=respuesta,fg="red")
            Titulo.grid(row=6,column=0,columnspan=4)   
                     

        
        else:
            respuesta=f"empleado {nombre} de salario No habil para mostrar"
            Titulo=Label(frame,text="Respuesta",fg="red")
            Titulo.grid(row=5,column=0,columnspan=4)   
            Titulo=Label(frame,text=respuesta,fg="red")
            Titulo.grid(row=6,column=0,columnspan=4) 

    
    Titulo=Label(frame,text="Ejercicio  5 ")
    Titulo.grid(row=0,column=0,columnspan=4)
    

    textNombre=Label(frame,text="Nombre del Empleado")
    textNombre.grid(row=3,column=0)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=1)
    
    textSalario=Label(frame,text="Salario Basico por Hora")
    textSalario.grid(row=3,column=2)
    cuadroSalario=Entry(frame)
    cuadroSalario.grid(row=3,column=3)

    textHoras=Label(frame,text="Horas trabjadas en el Mes")
    textHoras.grid(row=4,column=0)
    cuadroHoras=Entry(frame)
    cuadroHoras.grid(row=4,column=1)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,columnspan=3)


    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0,sticky=SW)

    raiz.mainloop()

def Interejercicio6():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def back():
        raiz.destroy()

    def enviar():
        Va=cuadroA.get()
        Vb=cuadroB.get()
        Vc=cuadroC.get()

        datos=ejercicio_6(float(Va),float(Vb),float(Vc))
        total=datos.solucion()
        valor1=str(total["valor1"])
        valor2=str(total["valor2"])
        respuesta=f"valor 1: {valor1} valor 2: {valor2}"
        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0,columnspan=4)
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0,columnspan=4)
        
    

    Titulo=Label(frame,text="Ejercicio  6 ")
    Titulo.grid(row=0,column=0,columnspan=4)

    textA=Label(frame,text="Valor de A")
    textA.grid(row=3,column=0)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=1)
    
    textB=Label(frame,text="Valor de B")
    textB.grid(row=3,column=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=3,column=3)

    textC=Label(frame,text="Valor de C")
    textC.grid(row=4,column=0)
    cuadroC=Entry(frame)
    cuadroC.grid(row=4,column=1)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=4,column=2)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=9,column=0)
    raiz.mainloop()

def Interejercicio7():
    raiz=Tk()

    listaNum=StringVar()
    reset=StringVar()
    listaNormal=[]

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")
    
    def back():
        raiz.destroy()

    def add(num):
        listaNum.set(listaNum.get()+str(num)+",")
        listaNormal.append(int(num))
        print(listaNormal)
        reset.set("")

    def enviar(listaNormal):
        datos=ejercicio_7(listaNormal)
        operaciones=datos.solucion()

        cubos=operaciones["cubos"]
        raicez=operaciones["raicez"]
        cuadrados=operaciones["cuadrados"]
        
        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=7,column=0,columnspan=4)
        
        
        fila=9

        for i in range(len(listaNormal)):
            inicial=listaNormal[i]
            cuadrado=cuadrados[i]
            cubo=cubos[i]
            raiz=raicez[i]
            respuesta=f"{inicial} cuadrado: {cuadrado}. cubo: {cubo}. raiz: {raiz}"
            Titulo=Label(frame,text=respuesta,fg="red")
            Titulo.grid(row=fila,column=0,columnspan=4)
            fila+=1


    Titulo=Label(frame,text="Ejercicio  7 ")
    Titulo.grid(row=0,column=0,columnspan=4)


    plant=Label(frame,text="Lista de numeros:")
    plant.grid(row=3,column=0,columnspan=4)
    plantList=Label(frame,textvariable=listaNum)
    plantList.grid(row=4,column=0,columnspan=4)

    textA=Label(frame,text="Numero a añadir a la lista")
    textA.grid(row=5,column=0)
    cuadroA=Entry(frame,textvariable=reset)
    cuadroA.grid(row=5,column=1)
    boton1=Button(frame,text="Añadir",width=10,command=lambda:add(cuadroA.get()))
    boton1.grid(row=5,column=2)

    boton1=Button(frame,text="Enviar",width=10,command=lambda:enviar(listaNormal))
    boton1.grid(row=6,column=0)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=99,column=0)

    raiz.mainloop()

def Interejercicio8():
    raiz=Tk()

    listaNum=StringVar()
    reset=StringVar()
    listaNormal=[]

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")
    
    def back():
        raiz.destroy()

    def add(num):
        listaNum.set(listaNum.get()+str(num)+",")
        listaNormal.append(int(num))
        print(listaNormal)
        reset.set("")

    def enviar(listaNormal):
            datos=ejercicio_8(listaNormal)
            operaciones=datos.solucion()
            respuesta=f"el número más grande es: {operaciones}"
            Titulo=Label(frame,text="Respuesta",fg="red")
            Titulo.grid(row=7,column=0,columnspan=4)
            Titulo=Label(frame,text=respuesta,fg="red")
            Titulo.grid(row=8,column=0,columnspan=4)


    Titulo=Label(frame,text="Ejercicio  8 ")
    Titulo.grid(row=0,column=0,columnspan=4)

    plant=Label(frame,text="Lista de numeros:")
    plant.grid(row=3,column=0,columnspan=4)
    plantList=Label(frame,textvariable=listaNum)
    plantList.grid(row=4,column=0,columnspan=4)

    textA=Label(frame,text="Numero a añadir a la lista")
    textA.grid(row=5,column=0)
    cuadroA=Entry(frame,textvariable=reset)
    cuadroA.grid(row=5,column=1)
    boton1=Button(frame,text="Añadir",width=10,command=lambda:add(cuadroA.get()))
    boton1.grid(row=5,column=2)

    boton1=Button(frame,text="Enviar",width=10,command=lambda:enviar(listaNormal))
    boton1.grid(row=6,column=0)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=99,column=0)

    raiz.mainloop()

def InterejercicioClases():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def back():
        raiz.destroy()
    
    def EjerciciosInterfaz(ejer):
        raiz.destroy()
        interfazFigura(ejer)
        InterejercicioClases()

    Titulo=Label(frame,text="Ejercicio  Clases Geometricas ")
    Titulo.grid(row=0,column=0,columnspan=4)

    boton1=Button(frame,text="Circulo",width=20,command=lambda:EjerciciosInterfaz("Circulo"))
    boton1.grid(row=3,column=0,padx=16,pady=12)

    boton1=Button(frame,text="Rectangulo",width=20,command=lambda:EjerciciosInterfaz("Rectangulo"))
    boton1.grid(row=3,column=2,padx=16,pady=12)

    boton1=Button(frame,text="Cuadrado",width=20,command=lambda:EjerciciosInterfaz("Cuadrado"))
    boton1.grid(row=4,column=0,padx=16,pady=12)

    boton1=Button(frame,text="Triangulo",width=20,command=lambda:EjerciciosInterfaz("Triangulo"))
    boton1.grid(row=4,column=2,padx=16,pady=12)

    boton1=Button(frame,text="Rombo",width=20,command=lambda:EjerciciosInterfaz("Rombo"))
    boton1.grid(row=5,column=0,padx=16,pady=12)

    boton1=Button(frame,text="Trapecio",width=20,command=lambda:EjerciciosInterfaz("Trapecio"))
    boton1.grid(row=5,column=2,padx=16,pady=12)

    boton1=Button(frame,text="Cancelar",width=10,command=back)
    boton1.grid(row=99,column=0)
    raiz.mainloop()


def emergentes(ejer):
    if ejer=="1":
        Interejercicio1()
        return
    if ejer=="2":
        Interejercicio2()
        return
    if ejer=="3":
        Interejercicio3()
        return
    if ejer=="4":
        Interejercicio4()
        return
    if ejer=="5":
        Interejercicio5()
        return
    if ejer=="6":
        Interejercicio6()
        return
    if ejer=="7":
        Interejercicio7()
        return
    if ejer=="8":
        Interejercicio8()
        return
    if ejer=="parte2":
        InterejercicioClases()

