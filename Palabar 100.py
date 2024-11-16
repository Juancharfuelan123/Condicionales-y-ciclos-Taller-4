
def valorletra(letra):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  
    letra = letra.upper()  
    if letra in abecedario:
        return abecedario.index(letra) + 1  
    else:
        return 0  


def calculadora(palabra):
    puntos = 0
    for letra in palabra:
        puntos =puntos +valorletra(letra)  
    return puntos


while True:
    palabra = input("Ingresa tu palabra para calcular el puntaje: ")
    puntos = calculadora(palabra)  

    print(f"Su palabra '{palabra}' tiene '{puntos}' puntos")

    if puntos == 100:
        print("Su calificacion es igual a 100 ")
        break  