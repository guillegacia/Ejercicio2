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
        #ingresa el valor 
        ingresoV = float(input("Dinero a ingresar $"))
        #lista del punto 3
        resultTI.append(ingresoV)
        #metodo de clase
        ingreso1 = ingresos(ingresoV)
        resultI = ingreso1.sumIngreso()
        #suma para el fondo de la cuenta 
        result1 = result1+resultI
        print(f"el fondo de la cuenta es de $ {result1}")

    elif selecion==2:
        #ingresa el valor 
        egresoV = float(input("Dinero a egresar $"))
        #lista del punto 3
        resultTE.append(egresoV)
        #metodo de clase
        egreso1 =  egreso(egresoV)
        resultE = egreso1.nuevoEgreso()
        #suma para el fondo de la cuenta 
        result1 = result1 + resultE
        print(f"el fondo de la cuenta es de $ {result1}")

    elif selecion==3:
        #para obtener las listas de ingreso 
        for iterator in resultTI:
            print(iterator)

    elif selecion==4:
        #para obtener las listas de egreso 
        for iterator in resultTE:
            print(iterator)
    
    elif selecion==5:
        #para obtener las listas de ingreso y egreso
        print("lista de dinero ingrasado")
        for iterator in resultTI:
            print(iterator)
        print("lista de dinero egresado")
        for iterator in resultTE:
            print(iterator)       
    elif selecion==6:
        #para obtener el total de la cuenta
        print(f"la cuenta tiene la cantida de ${result1}")

    elif selecion==0:
        #para finalizar 
        break



    
        

       

        
 


         
          




