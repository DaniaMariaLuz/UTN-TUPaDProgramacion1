usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
ingreso_exitoso = False

while intentos < 3 and not ingreso_exitoso:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        ingreso_exitoso = True
        print("Acceso concedido.\n")
    else:
        print("Error: credenciales inválidas.\n")

if not ingreso_exitoso:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.\n")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.\n")
        else:
            if opcion == "1":
                print("Estado: Inscripto\n")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.\n")
                else:
                    conf_clave = input("Confirmar clave: ")
                    if nueva_clave == conf_clave:
                        clave_correcta = nueva_clave
                        print("Clave cambiada con éxito.\n")
                    else:
                        print("Error: las claves no coinciden.\n")
            elif opcion == "3":
                print("Mensaje: ¡Sigue adelante, tú puedes!\n")
