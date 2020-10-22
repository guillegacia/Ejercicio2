from clases import (finanzas, ingresos, egreso)

result1 = 0.0
resultTI = []
resultTE = []

while True:
    print("Bienvenido usuario")
    print("1. Dinero a ingresar")
    print("2. Dinero a egresar")
    print("3. Ingresos realizados")
    print("4. Egresos realidaso")
    print("5. Reporte general de ingresos y egresos")
    print("6. Fondo de la cuenta")
    print("0. Salir")
    selecion = int(input("Selecione una opcion "))
    
    if selecion==1:
        
        ingresoV = float(input("Dinero a ingresar $"))
        resultTI.append(ingresoV)
        ingreso1 = ingresos(ingresoV)
        resultI = ingreso1.sumIngreso()
        result1 = result1+resultI
        print(f"el fondo de la cuenta es de $ {result1}")

    elif selecion==2:
        
        egresoV = float(input("Dinero a egresar $"))
        resultTE.append(egresoV)
        egreso1 =  egreso(egresoV)
        resultE = egreso1.nuevoEgreso()
        result1 = result1 + resultE
        print(f"el fondo de la cuenta es de $ {result1}")

    elif selecion==3:
        for iterator in resultTI:
            print(iterator)

    elif selecion==4:
        for iterator in resultTE:
            print(iterator)
    
    elif selecion==5:
        print("lista de dinero ingrasado")
        for iterator in resultTI:
            print(iterator)
        print("lista de dinero egresado")
        for iterator in resultTE:
            print(iterator)       
    elif selecion==6:
        print(f"la cuenta tiene la cantida de ${result1}")

    elif selecion==0:
        break



    
        

       

        
 


         
          




