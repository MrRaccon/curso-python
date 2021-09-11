def conversor(tipo_pesos,valor_dolar):
    pesos = input("INgrese sus pesos " + tipo_pesos + " ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("Tienes $ " +dolares +" dolares")

menu = """
Bienvenido al conversor de monedas 

1- Pesos COlombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opcion :
"""

opcion = input(menu)

if opcion == '1':
    conversor("Colombianos",123.12)

elif opcion == '2':
    conversor("Argentinos",160)

elif opcion == '3':
    conversor("Mexicanos",20.21)

else:
    print("Ingresa un opcion correcta")



# dolares = input("INgrese sus dolares: ")
# dolares = float(pesos)
# valor_pesos=0.050
# pesos = dolares*valor_pesos
# pesos = round(pesos,2)
# pesos= str(pesos)
# print("Sus dolares a pesos son $ " +pesos +" dolares")
