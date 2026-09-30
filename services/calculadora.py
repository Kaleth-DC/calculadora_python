def menu ():
    print("===calculadora===")
    print("suma")
    print("resta")
    print("multiplicacion")
    print("divicion")
    print("salir")

def numero ():
    while True :
        try:
            numero1 = float(input("ingresa el primer numero:"))
            numero2 = float(input("ingresa el segundo numero:"))
            return numero1 ,numero2
        except ValueError:
            print("Ese no es un numero, intentalo de nuevo.")

def suma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado 
def resta (numero1, numero2):
    return numero1 - numero2
def multiplicacion (numero1, numero2):
    return numero1 * numero2
def divicion (numero1, numero2):
    if numero2 == 0 :
        return "no se puede dividir sobre cero"
    resultado = numero1 / numero2
    return resultado