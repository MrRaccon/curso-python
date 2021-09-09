pesos = input("INgrese sus pesos colombianos: ")
pesos = float(pesos)
valor_dolar=20.15
dolares = pesos/valor_dolar
dolares = round(dolares,2)
dolares= str(dolares)
print("Sus pesos a dolares son $ " +dolares +" dolares")


dolares = input("INgrese sus dolares: ")
dolares = float(pesos)
valor_pesos=0.050
pesos = dolares*valor_pesos
pesos = round(pesos,2)
pesos= str(pesos)
print("Sus dolares a pesos son $ " +pesos +" dolares")
