from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre_cientifico):
        self.nombre_cientifico = nombre_cientifico
    
    @abstractmethod
    def obtener_sonido(self):
        pass
    
    @abstractmethod
    def obtener_alimentos(self):
        pass
    
    @abstractmethod
    def obtener_habitat(self):
        pass
    
    def obtener_nombre_cientifico(self):
        return self.nombre_cientifico

class Canido(Animal):
    def obtener_alimentos(self):
        return "Carnívoro"
    
class Felino(Animal):
    def obtener_alimentos(self):
        return "Carnívoro"

class Perro(Canido):
    def __init__(self):
        super().__init__("Canis lupus familiaris")
    
    def obtener_sonido(self):
        return "Ladrido"
    
    def obtener_habitat(self):
        return "Doméstico"

class Lobo(Canido):
    def __init__(self):
        super().__init__("Canis lupus")
    
    def obtener_sonido(self):
        return "Aullido"
    
    def obtener_habitat(self):
        return "Bosque"

class Leon(Felino):
    def __init__(self):
        super().__init__("Panthera leo")
    
    def obtener_sonido(self):
        return "Rugido"
    
    def obtener_habitat(self):
        return "Pradera"

class Gato(Felino):
    def __init__(self):
        super().__init__("Felis silvestris catus")
    
    def obtener_sonido(self):
        return "Maullido"
    
    def obtener_habitat(self):
        return "Doméstico"

def main():
    lista_animales = [Perro(), Lobo(), Leon(), Gato()]
    
    for animal in lista_animales:
        print("Nombre científico:", animal.obtener_nombre_cientifico())
        print("Sonido:", animal.obtener_sonido())
        print("Alimentos:", animal.obtener_alimentos())
        print("Hábitat:", animal.obtener_habitat())
        print()

if __name__ == "__main__":
    main()
