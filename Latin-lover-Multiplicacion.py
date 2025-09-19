#Funcion de multiplicacion con dos numeros
def multiplicacion (a, b):
    return a*b
#Pedir al usuario los numeros
num1 = int (input("Ingresa el primer numero: "))
num2 = int (input("Ingresa el segundo numero"))
#Usar la funcion
resultado = multiplicacion (num1, num2)
print("El resultado de la multiplicacion es:", resultado)