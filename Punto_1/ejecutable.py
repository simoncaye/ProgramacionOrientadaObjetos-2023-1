from Clases import * 

tipoCuenta=input("Ingrese tipo de cuenta 'Ahorros' o 'Córriente\n")
saldo=input("Ingrese el saldo inicial\n")
tasa=input("Ingrese la tasa de la comision (en decimales)\n")

if tipoCuenta=="Ahorros":
    miCuenta=cuentaAhorros(float(saldo),float(tasa))
else:
    miCuenta=cuentaCorriente(float(saldo),float(tasa))

desicion=True
while desicion==True:
    accion=input("digite '0' para realizar un movimiento o '1' para finalizar e imprimir comprobante\n")
    if int(accion)==0:
        accion2=input("digite '0' para retirar, '1' consignar\n")
        if int(accion2)==0:
            cantidadretiro=int(input("Ingrese la cantidad a retirar\n"))
            miCuenta.retirar(cantidadretiro)
            

        elif int(accion2)==1:
            cantidadconsignar=int(input("Ingrese la cantidad a consignar\n"))
            miCuenta.consignar(cantidadconsignar)
            
    else:
        miCuenta.extractoMensual()
        miCuenta.imprimir()
        desicion=False

 