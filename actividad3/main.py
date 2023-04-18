from tkinter import *
from popaps import emergentes



def principal():
    raiz=Tk()

    frame=Frame()
    frame.pack()
    frame.config(bg="blue")

    def EjerciciosInterfaz(ejer):
        raiz.destroy()
        emergentes(ejer)
        principal()

    boton1=Button(frame,text="Ejercicio 1",width=10,command=lambda:EjerciciosInterfaz("1"))
    boton1.grid(row=3,column=0,padx=12,pady=4)

    boton2=Button(frame,text="Ejercicio 2",width=10,command=lambda:EjerciciosInterfaz("2"))
    boton2.grid(row=4,column=0,padx=12,pady=4)


    boton3=Button(frame,text="Ejercicio 3",width=10,command=lambda:EjerciciosInterfaz("3"))
    boton3.grid(row=5,column=0,padx=12,pady=4)

    boton4=Button(frame,text="Ejercicio 4",width=10,command=lambda:EjerciciosInterfaz("4"))
    boton4.grid(row=3,column=1,padx=12,pady=4)

    boton5=Button(frame,text="Ejercicio 5",width=10,command=lambda:EjerciciosInterfaz("5"))
    boton5.grid(row=4,column=1,padx=12,pady=4)

    boton6=Button(frame,text="Ejercicio 6",width=10,command=lambda:EjerciciosInterfaz("6"))
    boton6.grid(row=5,column=1,padx=12,pady=4)


    boton7=Button(frame,text="Ejercicio 7",width=10,command=lambda:EjerciciosInterfaz("7"))
    boton7.grid(row=3,column=2,padx=12,pady=4)

    boton8=Button(frame,text="Ejercicio 8",width=10,command=lambda:EjerciciosInterfaz("8"))
    boton8.grid(row=4,column=2,padx=12,pady=4)

    boton8=Button(frame,text="part2",width=10,command=lambda:EjerciciosInterfaz("parte2"))
    boton8.grid(row=5,column=2,padx=12,pady=4)


    raiz.mainloop()



if __name__ == "__main__":
    principal()