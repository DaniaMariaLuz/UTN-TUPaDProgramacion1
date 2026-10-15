operador = ""
while not operador.isalpha():
    operador = input("Nombre del operador: ")

l1, l2, l3, l4 = "", "", "", ""
m1, m2, m3 = "", "", ""

opcion = ""
while opcion != "5":
    print("\n--- Menú Agenda ---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    opcion = input("Opción: ")
    
    if opcion == "1":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ")
        if dia in ["1", "2"]:
            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente: ")
            
            if dia == "1":
                if paciente in [l1, l2, l3, l4]:
                    print("Error: Paciente ya registrado el Lunes.")
                elif l1 == "": l1 = paciente; print("Turno Lunes 1 asignado.")
                elif l2 == "": l2 = paciente; print("Turno Lunes 2 asignado.")
                elif l3 == "": l3 = paciente; print("Turno Lunes 3 asignado.")
                elif l4 == "": l4 = paciente; print("Turno Lunes 4 asignado.")
                else: print("Lunes sin cupos.")
            else:
                if paciente in [m1, m2, m3]:
                    print("Error: Paciente ya registrado el Martes.")
                elif m1 == "": m1 = paciente; print("Turno Martes 1 asignado.")
                elif m2 == "": m2 = paciente; print("Turno Martes 2 asignado.")
                elif m3 == "": m3 = paciente; print("Turno Martes 3 asignado.")
                else: print("Martes sin cupos.")
        else:
            print("Día inválido.")
            
    elif opcion == "2":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ")
        if dia in ["1", "2"]:
            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente a cancelar: ")
                
            if dia == "1":
                if l1 == paciente: l1 = ""; print("Cancelado Lunes 1.")
                elif l2 == paciente: l2 = ""; print("Cancelado Lunes 2.")
                elif l3 == paciente: l3 = ""; print("Cancelado Lunes 3.")
                elif l4 == paciente: l4 = ""; print("Cancelado Lunes 4.")
                else: print("No se encontró al paciente.")
            else:
                if m1 == paciente: m1 = ""; print("Cancelado Martes 1.")
                elif m2 == paciente: m2 = ""; print("Cancelado Martes 2.")
                elif m3 == paciente: m3 = ""; print("Cancelado Martes 3.")
                else: print("No se encontró al paciente.")
        else:
            print("Día inválido.")

    elif opcion == "3":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ")
        if dia == "1":
            print(f"Turno 1: {l1 if l1 else '(libre)'}\nTurno 2: {l2 if l2 else '(libre)'}\nTurno 3: {l3 if l3 else '(libre)'}\nTurno 4: {l4 if l4 else '(libre)'}")
        elif dia == "2":
            print(f"Turno 1: {m1 if m1 else '(libre)'}\nTurno 2: {m2 if m2 else '(libre)'}\nTurno 3: {m3 if m3 else '(libre)'}")
            
    elif opcion == "4":
        ocupados_l = (1 if l1 else 0) + (1 if l2 else 0) + (1 if l3 else 0) + (1 if l4 else 0)
        ocupados_m = (1 if m1 else 0) + (1 if m2 else 0) + (1 if m3 else 0)
        print(f"Lunes: {ocupados_l} ocupados, {4 - ocupados_l} disponibles.")
        print(f"Martes: {ocupados_m} ocupados, {3 - ocupados_m} disponibles.")
        if ocupados_l > ocupados_m: print("Día con más turnos: Lunes")
        elif ocupados_m > ocupados_l: print("Día con más turnos: Martes")
        else: print("Empate en turnos.")
