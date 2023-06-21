#EJERCICIO 8.3
import math
from tkinter import *
from tkinter import messagebox

class figura:
    def calcularvolumen(self):
        pass

    def calcularsuperficie(self):
        pass

class cilindro(figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    
    def calcularvolumen(self):
        return math.pi * self.radio**2 * self.altura
    
    def calcularsuperficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class esfera(figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcularvolumen(self):
        return (4/3) * math.pi * self.radio**3
    
    def calcularsuperficie(self):
        return 4 * math.pi * self.radio**2

class piramide(figura):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    
    def calcularvolumen(self):
        return (1/3) * self.base * self.altura
    
    def calcularsuperficie(self):
        return (self.base * self.apotema) / 2 + self.base * math.sqrt(self.apotema**2 + (self.base/2)**2)

def calcular():
    try:
        figura = None
        if seleccion.get() == "Cilindro":
            figura = cilindro(float(txtRadio.get()), float(txtAltura.get()))
        elif seleccion.get() == "Esfera":
            figura = esfera(float(txtRadio.get()))
        elif seleccion.get() == "Piramide":
            figura = piramide(float(txtBase.get()), float(txtAltura.get()), float(txtApotema.get()))
        
        volumen = figura.calcularvolumen()
        superficie = figura.calcularsuperficie()

        messagebox.showinfo("Resultado", f"Volumen: {volumen}\nSuperficie: {superficie}")
    
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

ventana = Tk()
ventana.title("Calculadora de figuras geometricas")

seleccion = StringVar()
seleccion.set("Cilindro")

lblFigura = Label(ventana, text="Seleccione una figura:")
lblFigura.pack()

rdbCilindro = Radiobutton(ventana, text="Cilindro", variable=seleccion, value="Cilindro")
rdbCilindro.pack()
rdbEsfera = Radiobutton(ventana, text="Esfera", variable=seleccion, value="Esfera")
rdbEsfera.pack()
rdbPiramide = Radiobutton(ventana, text="Pirámide", variable=seleccion, value="Piramide")
rdbPiramide.pack()

lblRadio = Label(ventana, text="Radio:")
lblRadio.pack()
txtRadio = Entry(ventana)
txtRadio.pack()

lblAltura = Label(ventana, text="Altura:")
lblAltura.pack()
txtAltura = Entry(ventana)
txtAltura.pack()

lblBase = Label(ventana, text="Base:")
lblBase.pack()
txtBase = Entry(ventana)
txtBase.pack()

lblApotema = Label(ventana, text="Apotema:")
lblApotema.pack()
txtApotema = Entry(ventana)
txtApotema.pack()

btnCalcular = Button(ventana, text="Calcular", command=calcular)
btnCalcular.pack()

ventana.mainloop()
