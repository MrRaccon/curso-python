# def imprimir_mensaje():
#     print("mensaje espécial :")
#     print("estoy aprendiendo funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
def impresion_datos(opcion):
     print("hola")
     print("hola como estas")
     print(opcion)
     print('adios')


opcion = input("Elige una opcion(1,2,3): ")

if opcion == '1':
    impresion_datos("Eligiste la opcion 1")
elif opcion == '2':
    impresion_datos("Eligiste la opcion 2")
elif opcion == '3':
    impresion_datos("Eligiste la opcion 3")
else:
    print("eliga la opcion correcta")




