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



def bina_to_deci(bin_number):
    """
    Convierte un número binario en un número decimal.

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

def menu():
    """
    Presenta las opciones del menú y solicita la selección del usuario.

    Returns:
        int: La opción seleccionada por el usuario.
    """
    print('1. Binario a decimal')
    print('2. Decimal a binario')
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


if __name__ == '__main__':
    main()
