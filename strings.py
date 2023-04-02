name = input('Introduce tu nombre para saber el largo de tu nombre: ')
print(len(name))
str(name)
print(name.upper())
for i in name:
    if ord(i) < 90:
        print(f'La mayuscula son: {i}')
        

string = str(input('Introduce el la cadena de texto para saber el maximo y el minmo en asci: '))
maximo = max([ord(caracter) for caracter in string])
print("El valor ASCII máximo de la string es: {}".format(maximo))

minimo = min([ord(caracter) for caracter in string])
print("El valor ASCII mínimo de la string es: {}".format(minimo))
