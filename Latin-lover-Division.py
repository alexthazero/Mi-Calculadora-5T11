#Funcion de division con dos numeros
def division (a, b):
    return a/b
#Pedir al usuario los numeros
num1 = int (input("Ingresa el primer numero: "))
num2 = int (input("Ingresa el segundo numero"))
#Usar la funcion
resultado = division (num1, num2)
print("El resultado de la division es:", resultado)