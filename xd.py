boletas = []
for i in range(0, 3):
    boleta = str(input('Introduce el numero de boleta: '))
    boletas.append(boleta)

print(boletas)
boletas[2] = input('Cual es el nombre que estara en la tercera posicion: ')
print(boletas)
boletas.clear()
