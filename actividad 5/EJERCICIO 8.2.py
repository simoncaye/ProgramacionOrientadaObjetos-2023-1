#EJERCICIO 8.2
import tkinter as tk
from tkinter import messagebox
import statistics

class notas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de notas")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.notaentrada = []
        self.inter= []

        for i in range(5):
            label = tk.Label(self.root, text=f"Nota {i+1}:")
            label.grid(row=i, column=0, padx=10, pady=10)

            entrada = tk.Entry(self.root)
            entrada.grid(row=i, column=1)
            self.notaentrada.append(entrada)

        calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        calcular.grid(row=5, column=0, columnspan=2, pady=10)

        self.inter.append(tk.Label(self.root, text="Promedio:"))
        self.inter[0].grid(row=6, column=0, columnspan=2)

        self.inter.append(tk.Label(self.root, text="Desviación Estándar:"))
        self.inter[1].grid(row=7, column=0, columnspan=2)

        self.inter.append(tk.Label(self.root, text="Mayor Nota:"))
        self.inter[2].grid(row=8, column=0, columnspan=2)

        self.inter.append(tk.Label(self.root, text="Menor Nota:"))
        self.inter[3].grid(row=9, column=0, columnspan=2)

    def calcular(self):
        notas = []
        for entrada in self.notaentrada:
            try:
                nota = float(entrada.get())
                notas.append(nota)
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para la nota.")
                return

        promedio = sum(notas) / len(notas)
        desviacion = statistics.stdev(notas)
        mayornota = max(notas)
        menornota = min(notas)

        self.inter[0].config(text=f"Promedio: {promedio}")
        self.inter[1].config(text=f"Desviación Estándar: {desviacion}")
        self.inter[2].config(text=f"Mayor Nota: {mayornota}")
        self.inter[3].config(text=f"Menor Nota: {menornota}")

    def run(self):
        self.root.mainloop()

gui = notas()
gui.run()
