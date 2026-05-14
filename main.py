invitados = []
list_negra = ["voldemort","joker","lex luthor"]
print("BIENVENIDO AL SISTEMA DE PORTERIA")
while True:
    user = input("ingrese su nombre o escribe salir para salir: ")
    if user.lower() == "salir":
        break
    elif user.lower() in list_negra:
        print("estas en la lista negra,no podras pasar")
        break
    elif user.lower() not in invitados:
        invitados.append(user)
        print("puedes pasar")
    else:
        print("ya estas en la lista\nno puedes pasar")
print("ADIOS")
