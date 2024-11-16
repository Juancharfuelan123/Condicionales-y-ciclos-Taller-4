def simuladorclima(dias, tempini, probabilidadlluviaini):
    temp = tempini
    probabilidadlluvia = probabilidadlluviaini
    diasdelluvia = 0
    temps = []  
    random = 0.45  
    
    for dia in range(1, dias + 1):
        temps.append(temp)
        random = (random * 3.7) % 1  
        lluviahoy = random < (probabilidadlluvia / 100)
        if lluviahoy:
            diasdelluvia = diasdelluvia+ 1
            
            temp =temp- 1
        
        print(f"Dia {dia}: temperatura = {temp}°C, {'Llovio' if lluviahoy else 'No llovio'}")
        
        if temp > 25:
            probabilidadlluvia = min(100, probabilidadlluvia * 1.2)  
        elif temp < 5:
            probabilidadlluvia = max(0, probabilidadlluvia * 0.8) 
        
        random = (random * 3.7) % 1  
        if random < 0.1:
            temp += -2 if random < 0.05 else 2
    
    
    print("Resumen:")
    print(f"temp máxima: {max(temps)}°C")
    print(f"temp mínima: {min(temps)}°C")
    print(f"Días con lluvia: {diasdelluvia}")


dias = int(input("Ingresa el numero de dias que quieres predecir: "))
tempini = float(input("Ingresa la temp inicial (°C): "))
probabilidadlluviaini = float(input("Ingresa la probabilidad inicial de lluvia (%): "))


simuladorclima(dias, tempini, probabilidadlluviaini)
