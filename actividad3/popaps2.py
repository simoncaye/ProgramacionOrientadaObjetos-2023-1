from tkinter import *
from back import *



def circulo():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")
    

    def volver():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()

        figuras=ejercicio_figuras()
        circulo=figuras.circulo(float(a))
        area=circulo.Area()
        perimetro=circulo.Perimetro()
        respuesta=f"Area: {area}. Perimetro: {perimetro}"
        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0)
        



    Titulo=Label(frame,text="Circulo")
    Titulo.grid(row=0,column=0)
    
    textA=Label(frame,text="Radio")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=9,column=3,)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,sticky=SW)
    raiz.mainloop()

def rectangulo():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def volver():
        raiz.destroy()
    def enviar():
        base=cuadroA.get()
        altura=cuadroB.get()


        figuras=ejercicio_figuras()
        rectangulo=figuras.rectangulo(float(base),float(altura))

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        
        area=rectangulo.Area()
        perimetro=rectangulo.Perimetro()
        respuesta=f"Area: {area}. Perimetro: {perimetro}"
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0)
        
        



    Titulo=Label(frame,text="Rectangulo")
    Titulo.grid(row=0,column=0)

    textA=Label(frame,text="Base")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)

    textB=Label(frame,text="Altura")
    textB.grid(row=4,column=0,)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def cuadrado():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def volver():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()

        figuras=ejercicio_figuras()
        cuadrado=figuras.cuadrado(float(a))

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        
        area=cuadrado.Area()
        perimetro=cuadrado.Perimetro()
        respuesta=f"Area: {area}. Perimetro: {perimetro}"
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0)


    Titulo=Label(frame,text="Valores del Cuadrado")
    Titulo.grid(row=0,column=0)


    textA=Label(frame,text="lado del Circulo")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def triangulo():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def volver():
        raiz.destroy()
    def enviar():
        base=cuadroA.get()
        altura=cuadroB.get()


        figuras=ejercicio_figuras()
        triangulo=figuras.triangulo(float(base),float(altura))

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        
        area=triangulo.Area()
        perimetro=triangulo.Perimetro()
        tipo=triangulo.TipoTriangulo()
        respuesta=f"Area: {area}. Perimetro: {perimetro}. Tipo: {tipo}"
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0) 


    Titulo=Label(frame,text="Triangulo")
    Titulo.grid(row=0,column=0)
    
    textA=Label(frame,text="Base")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)

    textB=Label(frame,text="Altura")
    textB.grid(row=4,column=0,)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def rombo():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def volver():
        raiz.destroy()
    def enviar():
        ancho=cuadroA.get()
        largo=cuadroB.get()
        lado=cuadroC.get()

        figuras=ejercicio_figuras()
        rombo=figuras.rombo(float(lado),float(ancho),float(largo))

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=6,column=0)
        
        area=rombo.Area()
        perimetro=rombo.Perimetro()
        respuesta=f"Area: {area}. Perimetro: {perimetro}"
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=7,column=0)


    Titulo=Label(frame,text="Rombo")
    Titulo.grid(row=0,column=0)
    
    textA=Label(frame,text="Ancho")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)

    textB=Label(frame,text="Largo")
    textB.grid(row=4,column=0,)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,)

    textC=Label(frame,text="Lado")   
    textC.grid(row=5,column=0,)
    cuadroC=Entry(frame)
    cuadroC.grid(row=5,column=2,)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=6,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=15,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def trapecio():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def volver():
        raiz.destroy()
    def enviar():
        base1=cuadroA.get()
        base2=cuadroB.get()
        lado=cuadroC.get()
        altura=cuadroD.get()

        figuras=ejercicio_figuras()
        trapecio=figuras.trapecio(float(lado),float(altura),float(base1),float(base2))

        Titulo=Label(frame,text="Respuesta",fg="red")
        Titulo.grid(row=8,column=0)
        
        
        area=trapecio.Area()
        perimetro=trapecio.Perimetro()
        respuesta=f"Area: {area}. Perimetro: {perimetro}"
        Titulo=Label(frame,text=respuesta,fg="red")
        Titulo.grid(row=9,column=0)


    Titulo=Label(frame,text="Valores del Trapecio")
    Titulo.grid(row=0,column=0)
    
    textA=Label(frame,text="Base 1")
    textA.grid(row=3,column=0,)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,)

    textB=Label(frame,text="Base 2")
    textB.grid(row=4,column=0,)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,)

    textC=Label(frame,text="Lado")   
    textC.grid(row=5,column=0,)
    cuadroC=Entry(frame)
    cuadroC.grid(row=5,column=2,)

    textD=Label(frame,text="Altura")   
    textD.grid(row=6,column=0,)
    cuadroD=Entry(frame)
    cuadroD.grid(row=6,column=2,)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=7,column=3,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=15,column=0,sticky=SW)
    raiz.mainloop()

def interfazFigura(ejer):
    if ejer=="Circulo":
        circulo()
        return
    if ejer=="Rectangulo":
        rectangulo()
        return
    if ejer=="Cuadrado":
        cuadrado()
        return
    if ejer=="Triangulo":
        triangulo()
        return
    if ejer=="Rombo":
        rombo()
        return
    if ejer=="Trapecio":
        trapecio()
        return
