from claseRaiz import *

tipoInmueble=input("Ingrese el tipo de inmueble 'Vivienda' o 'Local'\n")
identificador=input("Ingrese el identificador del Inmueble\n")
area=input("Ingrese el area del Inmueble\n")
direccion=input("Ingrese la direccion del Inmueble\n")

inmueble1=inmueble(identificador,area,direccion)


if tipoInmueble=="Vivienda":
    habitaciones=int(input("ingrese el numero de habitaciones\n"))
    baños=int(input("ingrese el numero de baños\n"))

    vivienda=inmuebleVivienda(identificador,area,direccion,habitaciones,baños)

    tipoVivienda=input("Ingrese el tipo de vivienda 'Casa' o 'Apartamento'\n")
    if tipoVivienda=="Casa":
        pisos=int(input("ingrese el numero de pisos\n"))

        casa1=casa(identificador,area,direccion,habitaciones,baños,pisos)

        tipoCasa=input("Ingrese el tipo de Casa 'Rural' o 'Urbana'\n")
        if tipoCasa=="Rural":
            dist=int(input("ingrese la distancia a la cabecera en metros\n"))
            altiitud=int(input("ingrese la altitud\n"))

            rural=casaRural(identificador,area,direccion,habitaciones,baños,pisos,dist,altiitud)
            rural.calcularPrecioVenta()
            rural.imprimir()

        elif tipoCasa=="Urbana":

            urbana=casaUrbana(identificador,area,direccion,habitaciones,baños,pisos)
            urbana.imprimir()

            tipoUrbana=input("Ingrese el tipo de Casa Urbana 'Conjunto Cerrado' o 'Independiente'\n")
            if tipoUrbana=="Conjunto Cerrado":
                valorAdministracion=int(input("Valor de la administracion"))
                piscina=int(input("tiene Piscina?"))
                campos=int(input("tiene campos deportivos?"))

                conjunto=casaConjuntoCerrado(identificador,area,direccion,habitaciones,baños,pisos,valorAdministracion,piscina,campos)
                conjunto.calcularPrecioVenta()
                conjunto.imprimir()

            elif tipoUrbana=="Independiente":
                ind=casaIndpendiente(identificador,area,direccion,habitaciones,baños,pisos)
                ind.calcularPrecioVenta()
                ind.imprimir()


    
    elif tipoVivienda=="Apartamento":
        apto=apartamento(identificador,area,direccion,habitaciones,baños)

        tipoApartamento=input("Ingrese el tipo de Apartamento 'Familiar' o 'Estudio'")
        if tipoApartamento=="Familiar":
            valorAdmin=int(input("Ingrese el valor de la administracion"))

            aptofam=apartamentoFamiliar(identificador,area,direccion,habitaciones,baños,valorAdmin)
            aptofam.calcularPrecioVenta()
            aptofam.imprimir()

    
        elif tipoApartamento=="Estudio":
            aptoEst=apartaEstudio()
            aptoEst.calcularPrecioVenta(identificador,area,direccion,habitaciones,baños)
            aptoEst.imprimir()

elif tipoInmueble=="Local":
    tipoLocal=input("Ingrese el tipo del local")
    local1=local(identificador,area,direccion,tipoLocal)

    tipo2=input("Ingrese si el local es 'Comercial' o 'Oficina'")
    if tipo2=="Comercial":
        centroComecial=input("Ingrese el centro comercial")

        localcom=localComercial(identificador,area,direccion,tipoLocal,centroComecial)
        localcom.calcularPrecioVenta()
        localcom.imprimir()

    elif tipo2=="Oficina":
        esgobierno=input("la oficina es Goburnamental?")

        ofi=oficina(identificador,area,direccion,tipoLocal,esgobierno)
        ofi.calcularPrecioVenta()
        ofi.imprimir()

else:
    print("Ingresaste un valor no valido")
