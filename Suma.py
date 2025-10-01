def sumar_tres_digitos():
    """
    Suma tres números ingresados por el usuario.
    """
    print("Ingresa tres números para sumarlos.")
    
    # Pedir el primer número
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            
    # Pedir el segundo número
    while True:
        try:
            num2 = float(input("Ingresa el segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    # Pedir el tercer número
    while True:
        try:
            num3 = float(input("Ingresa el tercer número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
    
    # Calcular la suma
    suma_total = num1 + num2 + num3
    
    # Imprimir el resultado
    print(f"\nLa suma de los tres números es: {suma_total}")

# Llamar a la función para ejecutar el código
sumar_tres_digitos()
