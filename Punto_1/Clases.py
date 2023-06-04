class cuenta():
    def __init__(self,saldo,tasa,comision=0,numConsig=0,numRet=0):
        self.saldo=saldo
        self.tasa=tasa
        self.comision=comision
        self.numConsig=numConsig
        self.numRet=numRet
    def consignar(self,consignacion):
        self.saldo=self.saldo+consignacion
        self.numConsig=self.numConsig+1
    def retirar(self,retirado):
        if self.saldo-retirado<0:
            print("Saldo insuficiente para retirar")
            return 
        self.saldo=self.saldo-retirado
        self.numRet=self.numRet+1
    def interesMensual(self):
        tasaMensual=self.tasa/12
        interesMensual=self.saldo*tasaMensual
        self.saldo=self.saldo+interesMensual
    def extractoMensual(self):
        self.saldo=self.saldo-self.comision
        self.interesMensual()
    def imprimir(self):
        print(f"Saldo:{self.saldo}, Tasa Anual:{self.tasa}, Comision Mensual:{self.comision}, # de retiros:{self.numRet}, # De Consignaciones:{self.numConsig} ")

class cuentaAhorros(cuenta):
    def __init__(self, saldo, tasa, comision=0, numConsig=0, numRet=0):
        super().__init__(saldo, tasa, comision, numConsig, numRet)
        if self.saldo<10000:
            self.activa=False
        else:
            self.activa=True
    def consignar(self,consignacion):
        if self.activa==True:
            super().consignar(consignacion)
        else:
            print("La cuenta no se encuentra Activa")
    def retirar(self,retirado):
        if self.activa==True:
            super().retirar(retirado)
        else:
            print("La cuenta no se encuentra Activa")
    def extractoMensual(self):
        if self.numRet>4:
            self.comision=self.comision+((self.numRet-4)*1000)
        super().extractoMensual()
        if self.saldo<10000:
            self.activa=False
    def imprimir(self):
        print(f"Saldo:{self.saldo}, Comision Mensual:{self.comision}, # De Transacciones {self.numConsig+self.numRet} ")

class cuentaCorriente(cuenta):
    def __init__(self, saldo, tasa, comision=0, numConsig=0, numRet=0, sobregiro=0):
        super().__init__(saldo, tasa, comision, numConsig, numRet)
        self.sobregiro=sobregiro

    def consignar(self,consignacion):            
        residuo=self.sobregiro-consignacion
        if self.sobregiro>0:
            if residuo>0:
                self.sobregiro=residuo
                self.saldo=0
                self.numConsig=self.numConsig+1

            else:
                self.sobregiro=0
                self.saldo=-1*residuo
                self.numConsig=self.numConsig+1

        else:
            super().consignar(consignacion)


    def retirar(self,retirado):
        resultado=self.saldo-retirado
        if resultado<0:
            self.sobregiro=self.sobregiro-resultado
            self.saldo=0
        else:
            super().retirar(retirado)
    def extractoMensual(self):
        super().extractoMensual()
    def imprimir(self):
        print(f"Saldo:{self.saldo}, Comision Mensual:{self.comision}, # De Transacciones {self.numConsig+self.numRet}, Valor Sobregiro: {self.sobregiro}")
