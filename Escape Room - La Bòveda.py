agente = ""
while not agente.isalpha():
    agente = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("¡El sistema de seguridad se ha bloqueado de forma definitiva!")
        break
        
    print(f"\n--- ESTADO --- Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {'ON' if alarma else 'OFF'}")
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar")
    
    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Acción (1-3): ")
    
    if opcion == "1":
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        if forzar_seguidas >= 3:
            print("Regla Anti-Spam: La cerradura se trabó. Alarma activada.")
            alarma = True
        else:
            if energia < 40 and not alarma:
                riesgo = ""
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    riesgo = input("¡Riesgo de alarma! Elija un cable (1-3): ")
                if riesgo == "3":
                    alarma = True
                    print("¡Cortaste el cable equivocado! Alarma activada.")
            
            if not alarma and forzar_seguidas < 3:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta exitosamente!")
    else:
        forzar_seguidas = 0
        if opcion == "2":
            energia -= 10
            tiempo -= 3
            print("Hackeando...")
            for i in range(4):
                codigo_parcial += "A"
                print(f"Progreso: {codigo_parcial}")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""
                print("Panel hackeado. Cerradura abierta.")
        elif opcion == "3":
            energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1
            if alarma:
                energia -= 10
            print("Has descansado.")

if cerraduras_abiertas == 3:
    print("\n¡VICTORIA! Has abierto la bóveda.")
else:
    print("\nDERROTA. Misión fallida.")
