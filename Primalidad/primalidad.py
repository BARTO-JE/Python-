def factorial(n):
    fact = 1
    if n < 0:
        return 0
    elif n == 0:
        return 1
    while (n > 1):
        fact *= n
        n -= 1
    return fact


def main():
    numero = int(input("Escriba un numero: "))
    wilson = factorial(numero - 1) + 1
   
    if wilson % numero == 0:
        print("El numero es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    main()