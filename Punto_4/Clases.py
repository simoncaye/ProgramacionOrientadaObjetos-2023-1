from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_carrera = 0
    
    def get_identificador(self):
        return self.__identificador
    
    def set_identificador(self, identificador):
        self.__identificador = identificador
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_tiempo_carrera(self):
        return self.__tiempo_carrera
    
    def set_tiempo_carrera(self, tiempo_carrera):
        self.__tiempo_carrera = tiempo_carrera
    
    def imprimir_datos(self):
        print("Identificador:", self.__identificador)
        print("Nombre:", self.__nombre)
    
    @abstractmethod
    def imprimir_tipo(self):
        pass

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_sprint):
        super().__init__(identificador, nombre)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_sprint = velocidad_sprint
    
    def get_potencia_promedio(self):
        return self.__potencia_promedio
    
    def set_potencia_promedio(self, potencia_promedio):
        self.__potencia_promedio = potencia_promedio
    
    def get_velocidad_sprint(self):
        return self.__velocidad_sprint
    
    def set_velocidad_sprint(self, velocidad_sprint):
        self.__velocidad_sprint = velocidad_sprint
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print("Potencia promedio:", self.__potencia_promedio)
        print("Velocidad en sprint:", self.__velocidad_sprint)
    
    def imprimir_tipo(self):
        return "Es un Velocista"

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa
    
    def get_aceleracion_promedio(self):
        return self.__aceleracion_promedio
    
    def set_aceleracion_promedio(self, aceleracion_promedio):
        self.__aceleracion_promedio = aceleracion_promedio
    
    def get_grado_rampa(self):
        return self.__grado_rampa
    
    def set_grado_rampa(self, grado_rampa):
        self.__grado_rampa = grado_rampa
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print("Aceleración promedio en subida:", self.__aceleracion_promedio)
        print("Grado de rampa soportada:", self.__grado_rampa)
    
    def imprimir_tipo(self):
        return "Es un Escalador"

class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self.__velocidad_maxima = velocidad_maxima
    
    def get_velocidad_maxima(self):
        return self.__velocidad_maxima
    
    def set_velocidad_maxima(self, velocidad_maxima):
        self.__velocidad_maxima = velocidad_maxima
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print("Velocidad máxima:", self.__velocidad_maxima)
    
    def imprimir_tipo(self):
        return "Es un Contrarrelojista"

class Equipo:
    def __init__(self, nombre_equipo, pais_equipo):
        self.__nombre_equipo = nombre_equipo
        self.__pais_equipo = pais_equipo
        self.__ciclistas = []
    
    def get_nombre_equipo(self):
        return self.__nombre_equipo
    
    def set_nombre_equipo(self, nombre_equipo):
        self.__nombre_equipo = nombre_equipo
    
    def get_pais_equipo(self):
        return self.__pais_equipo
    
    def set_pais_equipo(self, pais_equipo):
        self.__pais_equipo = pais_equipo
    
    def imprimir_datos(self):
        print("Nombre del equipo:", self.__nombre_equipo)
        print("País del equipo:", self.__pais_equipo)
    
    def agregar_ciclista(self, ciclista):
        self.__ciclistas.append(ciclista)
    
    def get_ciclistas(self):
        return self.__ciclistas
    
    def calcular_tiempo_total(self):
        tiempo_total = 0
        for ciclista in self.__ciclistas:
            tiempo_total += ciclista.get_tiempo_carrera()
        return tiempo_total

# Clase de prueba
class Prueba:
    @staticmethod
    def main():
        equipos = []

        # Crear equipos
        equipo1 = Equipo("Equipo A", "País A")
        equipo2 = Equipo("Equipo B", "País B")
        equipos.append(equipo1)
        equipos.append(equipo2)

        # Crear ciclistas
        ciclista1 = Velocista("1", "Ciclista 1", 300, 40)
        ciclista2 = Escalador("2", "Ciclista 2", 5, 10)
        ciclista3 = Contrarrelojista("3", "Ciclista 3", 50)

        # Agregar ciclistas a los equipos
        equipo1.agregar_ciclista(ciclista1)
        equipo1.agregar_ciclista(ciclista2)
        equipo2.agregar_ciclista(ciclista3)

        # Mostrar equipos y seleccionar uno
        print("Equipos:")
        for i, equipo in enumerate(equipos):
            print(i + 1, "-", equipo.get_nombre_equipo())
        
        equipo_seleccionado = None
        while equipo_seleccionado is None:
            opcion = input("Seleccione un equipo (Ingrese el número correspondiente): ")
            if opcion.isdigit() and 0 < int(opcion) <= len(equipos):
                equipo_seleccionado = equipos[int(opcion) - 1]
            else:
                print("Opción inválida. Intente nuevamente.")

        # Mostrar los nombres de los ciclistas del equipo seleccionado
        print("Nombres de los ciclistas del equipo:")
        for ciclista in equipo_seleccionado.get_ciclistas():
            print(ciclista.get_nombre())

        # Obtener datos de un ciclista por identificador
        identificador = input("Ingrese el identificador del ciclista: ")
        ciclista_encontrado = None
        for ciclista in equipo_seleccionado.get_ciclistas():
            if ciclista.get_identificador() == identificador:
                ciclista_encontrado = ciclista
                break
        
        if ciclista_encontrado is not None:
            print("Datos del ciclista:")
            ciclista_encontrado.imprimir_datos()
            print(ciclista_encontrado.imprimir_tipo())
        else:
            print("No se encontró ningún ciclista con ese identificador.")

# Ejecutar la clase de prueba
if __name__ == "__main__":
    Prueba.main()
