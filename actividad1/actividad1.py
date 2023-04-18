import math

class mama_juan():
    def __init__(self, edadJuan):
        self.edadJuan = edadJuan

    def edades(self):
        edadJuan = self.edadJuan
        edadAlberto = edadJuan*2/3
        edadAna= edadJuan*4/3
        edadMama= edadJuan+edadAlberto+edadAna
        edadFamilia = {
            'edadJuan': edadJuan,
            'edadAlberto': edadAlberto,
            'edadAna': edadAna,
            'edadMama': edadMama,
        }
        return edadFamilia

class empleado():
    def __init__(self):
        self.horas = 48
        self.retencion = 12.5/100
        self.salario = 5000
    
    def dian(self):
        horas = self.horas
        salario = self.salario
        retencion = self.retencion
        ganado = horas*salario
        retenido = ganado*retencion
        neto = ganado-retenido
        datos = {
            'Salario Total': ganado,
            'Retenido Total': retenido,
            'Salario Neto': neto,
        }
        return datos

class cuadracubo():
    def __init__(self, numb):
        self.numb = numb
        self.cuadrado = self.numb**2
        self.cubo = self.numb**3

    def resultados(self):
        numero = self.numb
        cuadrado = self.cuadrado
        cubo = self.cubo
        datos = {
            'Número Inicial' : numero,
            'Cuadrado' : cuadrado,
            'cubo' : cubo
        }
        return datos

class circulo():
    def __init__(self, radio):
        self.radio = radio
        self.area = math.pi*((self.radio)**2)
        self.longitud = 2*math.pi*self.radio

    def resultados(self):
        radio = self.radio
        area = self.area
        longitud = self.longitud
        datos = {
            'Radio' : radio,
            'Area' : area,
            'Longitud' : longitud
        }
        return datos