print("Este programa solo admite cadenas de la misma longitud.")

def caracteresinfil(cadena1, cadena2):
    diferencias = []  
    for k in range(len(cadena1)):  
        if cadena1[k] != cadena2[k]:  
            diferencias.append(cadena2[k])  
    return diferencias


cadena1 = input("Ingresa su primera cadena : ")
cadena2 = input("Ingresa su segunda cadena : ")


if len(cadena1) == len(cadena2):
    resultado = caracteresinfil(cadena1, cadena2)  
    print("Los caracteres infiltrados son : ", resultado)  
else:
    print("EINGRESA CADENAS DE LA MISMA LONGITUD")