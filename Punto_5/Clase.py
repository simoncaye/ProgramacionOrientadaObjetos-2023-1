import tkinter as tk
from tkinter import messagebox

class persona:
    def __init__(self, nombre, apellidos, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono

class interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro")

        self.personas = []

        self.tagnombre = tk.Label(ventana, text="Nombre:")
        self.tagnombre.pack()
        self.espacionombre = tk.Entry(ventana)
        self.espacionombre.pack()

        self.tagapellidos = tk.Label(ventana, text="Apellidos:")
        self.tagapellidos.pack()
        self.espacioapellidos = tk.Entry(ventana)
        self.espacioapellidos.pack()

        self.tagdireccion = tk.Label(ventana, text="Dirección:")
        self.tagdireccion.pack()
        self.espaciodireccion = tk.Entry(ventana)
        self.espaciodireccion.pack()

        self.tagtelefono = tk.Label(ventana, text="Teléfono:")
        self.tagtelefono.pack()
        self.espaciotelefono = tk.Entry(ventana)
        self.espaciotelefono.pack()

        self.botonagregar = tk.Button(ventana, text="Añadir", command=self.aggpersona)
        self.botonagregar.pack()

        self.botonconsultar = tk.Button(ventana, text="Consultar", command=self.consultarpersonas)
        self.botonconsultar.pack()

        self.borrarseleccionado = tk.Button(ventana, text="Borrar al seleccionado", command=self.borrarseleccionado)
        self.borrarseleccionado.pack()

        self.borrartodos = tk.Button(ventana, text="Borrar Todos", command=self.borrartodos)
        self.borrartodos.pack()

        self.listapersonas = tk.Listbox(ventana)
        self.listapersonas.pack()

    def aggpersona(self):
        nombre = self.espacionombre.get()
        apellidos = self.espacioapellidos.get()
        direccion = self.espaciodireccion.get()
        telefono = self.espaciotelefono.get()

        nueva_persona = persona(nombre, apellidos, direccion, telefono)
        self.personas.append(nueva_persona)

        self.listapersonas.insert(tk.END, f"{nueva_persona.nombre} {nueva_persona.apellidos}")

        messagebox.showinfo("Aviso", "Persona agregada")

        self.espacionombre.delete(0, tk.END)
        self.espacioapellidos.delete(0, tk.END)
        self.espaciodireccion.delete(0, tk.END)
        self.espaciotelefono.delete(0, tk.END)

    def consultarpersonas(self):
        if len(self.personas) == 0:
            messagebox.showinfo("Aviso", "No hay personas registradas.")
        else:
            messagebox.showinfo("Personas Registradas", self.obtener_listapersonas())

    def obtener_listapersonas(self):
        lista = ""
        for persona in self.personas:
            lista += f"Nombre: {persona.nombre}\n"
            lista += f"Apellidos: {persona.apellidos}\n"
            lista += f"Dirección: {persona.direccion}\n"
            lista += f"Teléfono: {persona.telefono}\n\n"
        return lista

    def borrarseleccionado(self):
        seleccionado = self.listapersonas.curselection()
        if seleccionado:
            indice = seleccionado[0]
            persona_seleccionada = self.personas[indice]
            mensaje = f"¿Seguro de que quieres borrar a {persona_seleccionada.nombre} {persona_seleccionada.apellidos}?"
            confirmacion = messagebox.askyesno("Confirmar", mensaje)
            if confirmacion:
                del self.personas[indice]
                self.listapersonas.delete(indice)
                messagebox.showinfo("Aviso", "Persona eliminada")
        else:
            messagebox.showinfo("Aviso", "No se seleccionó a nadie")

    def borrartodos(self):
        if len(self.personas) == 0:
            messagebox.showinfo("Aviso", "No hay personas registradas.")
        else:
            confirmacion = messagebox.askyesno("Confirmar", "¿Seguro de borrar todas las personas registradas?")
            if confirmacion:
                self.personas.clear()
                self.listapersonas.delete(0, tk.END)
                messagebox.showinfo("Aviso", "Todas las personas han sido borradas")

ventana = tk.Tk()
app = interfaz(ventana)
ventana.mainloop()