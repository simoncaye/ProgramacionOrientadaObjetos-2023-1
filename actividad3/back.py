import math

class ejercicio_1():
    def __init__(self,Codigo,nombre,horas,valorHora,retencion):
        self.Codigo=Codigo
        self.nombre=nombre
        self.horas=horas
        self.valorHora=valorHora
        self.retencion=retencion
    def salarioEmpleado(self):
        codigo=self.Codigo
        nombre=self.nombre
        horas=self.horas
        valorHora=self.valorHora
        retencion=self.retencion
        salarioBruto=valorHora*horas
        porcentaje=retencion/100
        salarioNeto=salarioBruto-(salarioBruto*porcentaje)
        return {
            "salarioNeto":salarioNeto,
            "salarioBruto":salarioBruto
        }
    
class ejercicio_2():
    def __init__(self,lado):
        self.lado=lado
    def Area(self):
        lado=self.lado
        Area=(math.sqrt(3)*(lado*lado))/4
        Area=round(Area,2)
        return Area
    def Altura(self):
        lado=self.lado
        Altura=(math.sqrt(3)*lado)/2
        Altura=round(Altura,2)
        return Altura
    def Perimetro(self):
        lado=self.lado
        Perimetro=3*lado
        Perimetro=round(Perimetro,2)
        return Perimetro
    
class ejercicio_3():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def desicion(self):
        a=self.a
        b=self.b
        mensaje=""
        if a > b:
            mensaje=str(a)+" Es mayor que "+str(b)
        elif a < b:
            mensaje=str(a)+" Es menor que "+str(b)
        else:
            mensaje=str(a)+" Es igual que "+str(b)
        return mensaje

class ejercicio_4():
    def __init__(self,Inscripcion,nombres,Patrimonio,Estrato,):
        self.Inscripcion=Inscripcion
        self.nombres=nombres
        self.Patrimonio=Patrimonio
        self.Estrato=Estrato
    def pago(self):
        Inscripcion=self.Inscripcion
        nombres=self.nombres
        Patrimonio=self.Patrimonio
        Estrato=self.Estrato

        valor=50000
        if Patrimonio>2000000 and Estrato>3:
            valor=(Patrimonio*0.03)+valor

        return valor
    
class ejercicio_5():
    def __init__(self,nombre,salario,horas):
        self.nombre=nombre
        self.salario=salario
        self.horas=horas
    def pago(self):
        mensual=int(self.salario)*int(self.horas)
        if mensual>450000 :
            return mensual

class ejercicio_6():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def solucion(self):
        valores = [self.a,self.b,self.c]
        disc=(valores[1]**2)-(4*valores[0]*valores[2])
        if disc<0:
            return{
            "valor1":"No tiene Solucion",
            "valor2":"No tiene Solucion"
        }
        resultado1 = ((-1*valores[1])+math.sqrt((valores[1]**2)-(4*valores[0]*valores[2])))/(2*valores[0])
        resultado2 = ((-1*valores[1])-math.sqrt((valores[1]**2)-(4*valores[0]*valores[2])))/(2*valores[0])
        return{
            "valor1":resultado1,
            "valor2":resultado2
        }
    
class ejercicio_7():
    def __init__(self,lista1):
        self.lista1 = lista1
    def solucion(self):
        lista1=self.lista1
        cuadrados=[]
        raicez=[]
        cubos=[]
        for i in lista1:
            cuadrados.append(i**2)
            raicez.append(round(math.sqrt(i),3))
            cubos.append(i**3)
        print(cubos)
        return{
            "cuadrados":cuadrados,
            "raicez":raicez,
            "cubos":cubos
        }

class ejercicio_8():
    def __init__(self,lista1):
        self.lista1 = lista1
    def solucion(self):
        lista1=self.lista1
        mayor=0
        for i in lista1:
            if i>mayor:
                mayor=i
        return mayor

class ejercicio_figuras():    
    class circulo():
        def __init__(self,radio):
            self.radio = radio
        def Area(self):
            return math.pi*math.pow(self.radio,2)
        def Perimetro(self):
            return 2*math.pi*self.radio
    class rectangulo():
        def __init__(self,base,altura):
            self.base = base
            self.altura = altura
        def Area(self):
            return self.base*self.altura
        def Perimetro(self):
            return (2*self.base)+(2*self.altura)
    class cuadrado():
        def __init__(self,lado):
            self.lado = lado
        def Area(self):
            return self.lado**2
        def Perimetro(self):
            return 4*self.lado
    class triangulo():
        def __init__(self,base,altura):
            self.base = base
            self.altura = altura
        def Area(self):
            return (self.altura*self.base)/2
        def Hipotenusa(self):
            return math.sqrt((self.altura**2)+(self.base**2))
        def Perimetro(self):
            return self.base+self.altura+self.Hipotenusa()
        def TipoTriangulo(self):
            base=self.base
            altura=self.altura
            hipotenusa=self.Hipotenusa()
            if base==altura and base==hipotenusa and altura==hipotenusa:
                return "Equilatero"
            elif base!=altura and base!=hipotenusa and altura!=hipotenusa:
                return "Escaleno"
            else:
                return "Isoceles"
    class rombo():
        def __init__(self,lado,ancho,largo):
            self.lado = lado
            self.ancho = ancho
            self.largo = largo
        def Area(self):
            return (self.largo*self.ancho)/2
        def Perimetro(self):
            return 4*self.lado
    class trapecio():
        def __init__(self,lado,altura,base1,base2):
            self.altura = altura
            self.lado = lado
            self.base1 = base1
            self.base2 = base2
        def Area(self):
            return ((self.base1+self.base2)/2)*self.altura
        def Perimetro(self):
            return self.lado+self.lado+self.base1+self.base2