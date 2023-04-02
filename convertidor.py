def deci_to_bina(deci_number):
    """
    Convierte un número decimal en un número binario.

    Args:
        deci_number (int): Un número decimal entero.

    Returns:
        str: El valor binario correspondiente al número decimal.
    """
    binary_digits = []
    while deci_number > 0:
        remainder = deci_number % 2
        binary_digits.append(str(remainder))
        deci_number //= 2

    if not binary_digits:
        return "0"

    binary_digits.reverse()
    binary_number = ''.join(binary_digits)
    return binary_number


def dec_to_hex(dec_number):
    return print(f'El numero decimal es {dec_number} en hexadecimal es: {hex(dec_number)}')


def hex_to_dec(hex_number):
    dec_number = int(hex_number, base=16)
    return print(f"El numero hexadecimal {hex_number} convertido a decimal es: {dec_number}")


def bina_to_deci(bin_number):
    """
    Convierte un número binario en un número decimal.
    101
    Args:
        bin_number (str): Una cadena de dígitos binarios (0 y 1).

    Returns:
        int: El valor decimal correspondiente al número binario.

    Raises:
        ValueError: Si bin_number no contiene sólo dígitos binarios.
    """
    decimal_value = 0
    for i, bit in enumerate(reversed(bin_number)):
        if bit == '1':
            decimal_value += 2 ** i
    return decimal_value


def dec_to_bcd(decimal_number):
    """
    Convierte un número decimal en un código BCD.

    Args:
        decimal_number (int): Un número decimal.

    Returns:
        str: Una cadena que representa el código BCD correspondiente al número decimal de entrada.
    """
    # Convertir decimal a una lista de cadenas de dígitos decimales
    decimal_digits = list(str(decimal_number))

    # Transformar cada dígito decimal a un código BCD
    bcd_digits = []
    for digit in decimal_digits:
        # Convertir dígito decimal a binario de 4 bits
        binary_digit = bin(int(digit))[2:]
        # Agregar ceros a la izquierda si es necesario
        binary_digit = binary_digit.zfill(4)
        # Concatenar binario a la cadena de resultado
        bcd_digits.append(binary_digit)

    bcd_result = ''.join(bcd_digits)

    return bcd_result


def bcd_to_decimal(bcd_number):
    """
    Convierte un número en código BCD en su equivalente decimal.

    Args:
        bcd_number (str): Una cadena que representa un número en código BCD.

    Returns:
        int: El valor decimal correspondiente al número en código BCD de entrada.
    """
    decimal_value = 0
    for i in range(0, len(bcd_number), 4):
        # Extraer un dígito BCD de 4 bits
        bcd_digit = bcd_number[i:i+4]
        # Convertir el dígito BCD a su equivalente decimal
        decimal_digit = int(bcd_digit, 2)
        # Multiplicar el valor decimal del dígito por 10 elevado a la potencia correspondiente
        decimal_value += decimal_digit * (10 ** (len(bcd_number) - (i + 4)))

    return decimal_value


def menu():
    """
    Presenta las opciones del menú y solicita la selección del usuario.

    Returns:
        int: La opción seleccionada por el usuario.
    """
    print('1. Binario a decimal')
    print('2. Decimal a binario')
    print('3. Hexadecimal a decimal')
    print('4. Decimal a hexadecimal')
    print('5. Decimal a BCD')
    return int(input('Seleccione una opción: '))


def main():
    """
    Ejecuta el programa de conversión binaria y decimal.
    """
    option = menu()
    if option == 1:
        bin_number = input('Ingrese el número binario: ')
        deci_number = bina_to_deci(bin_number)
        print(f"El número decimal es: {deci_number}")

    elif option == 2:
        deci_number = int(input('Ingrese el número decimal: '))
        bin_number = deci_to_bina(deci_number)
        print(f"El número binario es: {bin_number}")

    elif option == 3:
        hexa_number = input("Ingrese el numero en hexadecimal: ")
        hex_to_dec(hexa_number)

    elif option == 4:
        deci_number = int(input("Ingresa el numero decimal: "))
        dec_to_hex(deci_number)

    elif option == 5:
        deci_number = input("Ingresa el numero decimal: ")
        print(f"El valor convertido es {dec_to_bcd(deci_number)}")

    elif option == 6:
        bcd_number = input("Ingresa el codigo bcd para transformar a decimal")
        print(f"El valor covertido a bcd es {bcd_to_decimal(bcd_number)}")
        
if __name__ == '__main__':
    main()
