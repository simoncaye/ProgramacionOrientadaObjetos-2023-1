from actividad1 import mama_juan, empleado, cuadracubo, circulo

def main(eleccion):
    if(eleccion=="1"):
        edadDeJuan=int(input("Cuál es la edad de Juan? "))
        ejercicio1=mama_juan(edadDeJuan)
        solucion1=ejercicio1.edades()
        print("Las edades de la familia son ",solucion1)
    elif(eleccion=="3"):
        ejercicio3=empleado()
        solucion3=ejercicio3.dian()
        print("El dinero del esclavo es\n",solucion3)
    elif(eleccion=="4"):
        numero=int(input("Digite el numero "))
        ejercicio4=cuadracubo(numero)
        solucion4=ejercicio4.resultados()
        print(solucion4)
    elif(eleccion=="5"):
        numero = float(input("Digite el numero "))
        ejercicio5=circulo(numero)
        solucion5=ejercicio5.resultados()
        print(solucion5)
    else:
        print("Esa no es una opción valida")   


if __name__=='__main__':
    print("Ejercicio 1")
    print("Ejercicio 3")
    print("Ejercicio 4")
    print("Ejercicio 5")
    eleccion=input("Qué ejercicios vas a realizar? ")
    main(eleccion)