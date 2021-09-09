menu = """
Bienvenido al conversor de monedas 

1- Pesos COlombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opcion :
"""
opcion = input(menu)

if opcion == '1':
    pesos = input("INgrese sus pesos colombianos: ")
    pesos = float(pesos)
    valor_dolar=45.15
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("Sus pesos a dolares son $ " +dolares +" dolares")

elif opcion == '2':
    pesos = input("INgrese sus pesos argentinos: ")
    pesos = float(pesos)
    valor_dolar=160
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("Sus pesos a dolares son $ " +dolares +" dolares")
elif opcion == '3':
    pesos = input("INgrese sus pesos Mexicanos: ")
    pesos = float(pesos)
    valor_dolar=20.15
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("Sus pesos a dolares son $ " +dolares +" dolares")
else:
    print("Ingresa un opcion correcta")



# dolares = input("INgrese sus dolares: ")
# dolares = float(pesos)
# valor_pesos=0.050
# pesos = dolares*valor_pesos
# pesos = round(pesos,2)
# pesos= str(pesos)
# print("Sus dolares a pesos son $ " +pesos +" dolares")
