nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dmg_pesado = 15
dmg_enemigo = 12

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 3:
            print("Error: Fuera de rango.")
            
    if opcion == "1":
        dmg_final = float(dmg_pesado)
        if vida_enemigo < 20:
            dmg_final *= 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(dmg_final)
        print(f"¡Atacaste al enemigo por {int(dmg_final)} puntos de daño!")
    
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100
            pociones -= 1
            print(f"Te curaste. Vida actual: {vida_jugador}.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            
    if vida_enemigo > 0:
        vida_jugador -= dmg_enemigo
        print(f">> ¡El enemigo te atacó por {dmg_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dmg_pesado = 15
dmg_enemigo = 12

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 3:
            print("Error: Fuera de rango.")
            
    if opcion == "1":
        dmg_final = float(dmg_pesado)
        if vida_enemigo < 20:
            dmg_final *= 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(dmg_final)
        print(f"¡Atacaste al enemigo por {int(dmg_final)} puntos de daño!")
    
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100
            pociones -= 1
            print(f"Te curaste. Vida actual: {vida_jugador}.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            
    if vida_enemigo > 0:
        vida_jugador -= dmg_enemigo
        print(f">> ¡El enemigo te atacó por {dmg_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dmg_pesado = 15
dmg_enemigo = 12

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 3:
            print("Error: Fuera de rango.")
            
    if opcion == "1":
        dmg_final = float(dmg_pesado)
        if vida_enemigo < 20:
            dmg_final *= 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(dmg_final)
        print(f"¡Atacaste al enemigo por {int(dmg_final)} puntos de daño!")
    
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100
            pociones -= 1
            print(f"Te curaste. Vida actual: {vida_jugador}.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            
    if vida_enemigo > 0:
        vida_jugador -= dmg_enemigo
        print(f">> ¡El enemigo te atacó por {dmg_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dmg_pesado = 15
dmg_enemigo = 12

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 3:
            print("Error: Fuera de rango.")
            
    if opcion == "1":
        dmg_final = float(dmg_pesado)
        if vida_enemigo < 20:
            dmg_final *= 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(dmg_final)
        print(f"¡Atacaste al enemigo por {int(dmg_final)} puntos de daño!")
    
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100
            pociones -= 1
            print(f"Te curaste. Vida actual: {vida_jugador}.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            
    if vida_enemigo > 0:
        vida_jugador -= dmg_enemigo
        print(f">> ¡El enemigo te atacó por {dmg_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
