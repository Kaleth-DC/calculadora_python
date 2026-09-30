from services.calculadora import menu, numero, suma, resta, multiplicacion, divicion


while True :
    menu()
    opcion = int(input(" Elije una opcion:"))
    
    if opcion == 1 :
        numero1, numero2 = numero()
        print("El resultado es :", suma (numero1, numero2))
    elif opcion == 2 :
        numero1, numero2 = numero()
        print("El resultado es :", resta (numero1, numero2))
    elif opcion == 3 :
        numero1, numero2 = numero()
        print("El resultado es :", multiplicacion (numero1, numero2))
    elif opcion == 4 :
        numero1, numero2 = numero()
        print("El resultado es :", divicion (numero1, numero2))
    elif opcion == 5 :
        print("Gracias por usar la calculadora")
        break
    else:
        print("operacion no valida")