class inmueble:
    def __init__(self,identificador,area,direccion):
        self.identificador=identificador
        self.area=area
        self.direccion=direccion
        self.precioVenta=0
    def calcularPrecioVenta(self,valorArea):
        self.precioVenta=int(self.area)*int(valorArea)
    def imprimir(self):
        print(f"Identificador Inmboliario: {self.identificador}\n Area: {self.area}\n Direccion: {self.direccion}\n Precio de Venta: {self.precioVenta} $")

class inmuebleVivienda(inmueble):
    def __init__(self,identificador,area,direccion,numeroHabitaciones,numeroBanos):
        super().__init__(identificador,area,direccion)
        self.numeroHabitaciones=numeroHabitaciones
        self.numeroBanos=numeroBanos
    def imprimir(self):
        super().imprimir()
        print(f" Numero de habitaciones: {self.numeroHabitaciones}\n Numero de Baños: {self.numeroBanos}")

class local(inmueble):
    def __init__(self, identificador, area, direccion,tipoLocal):
        super().__init__(identificador, area, direccion)
        self.tipoLocal=tipoLocal
    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipoLocal}")

class localComercial(local):
    def __init__(self, identificador, area, direccion, tipoLocal,centroComercial):
        super().__init__(identificador, area, direccion, tipoLocal)
        self.valorArea=3000000
        self.centroComercial=centroComercial
    def imprimir(self):
        super().imprimir()
        print(f"Centro Comercial: {self.centroComercial}")
    def calcularPrecioVenta(self):
        return super().calcularPrecioVenta(self.valorArea)

class oficina(local):
    def __init__(self, identificador, area, direccion, tipoLocal,esGobierno):
        super().__init__(identificador, area, direccion, tipoLocal)
        self.valorArea=3500000
        self.esGobierno=esGobierno
    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {self.esGobierno}")
    def calcularPrecioVenta(self):
        super().calcularPrecioVenta(self.valorArea)

class casa(inmuebleVivienda):
    def __init__(self,identificador,area,direccion,numeroHabitaciones,numeroBanos,numeroPisos):
        super().__init__(identificador,area,direccion,numeroHabitaciones,numeroBanos)
        self.numeroPisos=numeroPisos
    def imprimir(self):
        super().imprimir()
        print(f"Numero de Pisos: {self.numeroPisos}")

class casaRural(casa):
    def __init__(self,identificador,area,direccion,numeroHabitaciones,numeroBanos,numeroPisos,distanciaCabecera,altitud):
        super().__init__(identificador,area,direccion,numeroHabitaciones,numeroBanos,numeroPisos)
        self.valorArea=1500000
        self.distanciaCabecera=distanciaCabecera
        self.altitud=altitud
    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal: {self.distanciaCabecera} km\n Altitud sobre el nivel del mar: {self.altitud} metros")
    def calcularPrecioVenta(self):
        return super().calcularPrecioVenta(self.valorArea)

class casaUrbana(casa):
    def __init__(self,identificador,area,direccion,numeroHabitaciones,numeroBanos,numeroPisos):
        super().__init__(identificador,area,direccion,numeroHabitaciones,numeroBanos,numeroPisos)
    def imprimir(self):
        super().imprimir()

class casaConjuntoCerrado(casaUrbana):
    def __init__(self, identificador, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificador, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.valorArea=2500000
        self.valorAdministracion=valorAdministracion
        self.tienePiscina=tienePiscina
        self.tieneCamposDeportivos=tieneCamposDeportivos
    def imprimir(self):
        super().imprimir()
        print(f"Valor de Administracion: {self.valorAdministracion}\n Tiene Piscina?: {self.tienePiscina} \n Tiene campos deportivos?: {self.tieneCamposDeportivos}")
    def calcularPrecioVenta(self):
        super().calcularPrecioVenta(self.valorArea)

class casaIndpendiente(casaUrbana):
    def __init__(self, identificador, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificador, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.valorArea=3000000
    def imprimir(self):
        super().imprimir()
    def calcularPrecioVenta(self):
        return super().calcularPrecioVenta(self.valorArea)

class apartamento(inmuebleVivienda):
    def __init__(self,identificador,area,direccion,numeroHabitaciones,numeroBanos):
        super().__init__(identificador,area,direccion,numeroHabitaciones,numeroBanos)
    def imprimir(self):
        super().imprimir()

class apartamentoFamiliar(apartamento):
    def __init__(self, identificador, area, direccion, numeroHabitaciones, numeroBanos,valorAdministracion):
        super().__init__(identificador, area, direccion, numeroHabitaciones, numeroBanos)
        self.valorArea=2000000
        self.valorAdministracion=valorAdministracion
    def imprimir(self):
        super().imprimir()
        print(f"Valor de la Administracion: {self.valorAdministracion} $")
    def calcularPrecioVenta(self):
        super().calcularPrecioVenta(self.valorArea)
    
class apartaEstudio(apartamento):
    def __init__(self, identificador, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificador, area, direccion, 1, 1)
        self.valorArea=1500000
    def imprimir(self):
        super().imprimir()
    def calcularPrecioVenta(self):
        super().calcularPrecioVenta(self.valorArea)