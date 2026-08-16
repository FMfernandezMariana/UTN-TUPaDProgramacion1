#TP_Integrador - Repetitivas - Condicionales y Secuenciales

#Ejercicio_1: “Caja del Kiosco”

# 1. Solicitamos y validamos el nombre del cliente
nombre = input("Cliente: ").strip()
while not (nombre.isalpha() and len(nombre) > 0):
    print("Atención: el nombre solo debe contener letras y no puede estar vacío.")
    nombre = input("Cliente: ").strip()

# 2. Pedimos y validamos la cantidad de productos
cantidad_str = input("Cantidad de productos: ").strip()
while not (cantidad_str.isdigit() and int(cantidad_str) > 0):
    print("Error: Ingrese un entero mayor a 0.")
    cantidad_str = input("Cantidad de productos: ").strip()

cantidad_productos = int(cantidad_str)

# Establecemos variables para acumular totales
total_sin_descuentos = 0
total_con_descuentos = 0.0

# 3. Procesamos cada producto
for i in range(1, cantidad_productos + 1):
    # Validar precio del producto
    precio_str = input(f"Producto {i} - Precio: ").strip()
    while not (precio_str.isdigit() and int(precio_str) > 0):
        print("Error: Ingrese un precio válido (entero mayor a 0).")
        precio_str = input(f"Producto {i} - Precio: ").strip()
    
    precio = int(precio_str)
    
    # Validamos descuento S/N
    descuento_opcion = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
    while descuento_opcion not in ["s", "n"]:
        print("Error: Responda únicamente 'S' o 'N'.")
        descuento_opcion = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
    
    # Establecemos la acumulación precio sin descuento
    total_sin_descuentos += precio
    
    # Aplicamos o no el 10% de descuento
    if descuento_opcion == "s":
        total_con_descuentos += precio * 0.90
    else:
        total_con_descuentos += precio

# Realizamos los cálculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad_productos

# 4. Imprimimos los resultados
print("\n--- RESUMEN DE COMPRA ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



# Ejercicio_2: “Acceso al Campus y Menú Seguro”

# Establecemos credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

# Configuramos un máximo de 3 intentos para el ingreso al sistema
intentos = 1
acceso_concedido = False

while intentos <= 3 and not acceso_concedido:
    print(f"\nIntento {intentos}/3")
    usuario_ingresado = input("Usuario: ").strip()
    clave_ingresada = input("Clave: ").strip()

    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

# Al intentar las 3 veces bloqueamos la cuenta
if not acceso_concedido:
    print("\nCuenta bloqueada.")
else:
    # Al ingresar al sistema se muestra un "Menú repetitivo"
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ DE OPCIONES ---")
        print("1) Estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        
        opcion_input = input("Opción: ").strip()

        # Validamos el ingreso: debe ser número (.isdigit()) y estar entre 1 y 4
        if not opcion_input.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion_input) < 1 or int(opcion_input) > 4:
            print("Error: opción fuera de rango.")
        else:
            opcion = opcion_input

            # Ejecución de la opción seleccionada
            if opcion == "1":
                print("\nEstado: Inscripto")
                
            elif opcion == "2":
                # Cambio de clave
                nueva_clave = input("Nueva clave: ").strip()
                
                # Validamos: mínimo 6 caracteres
                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ").strip()

                confirmacion_clave = input("Confirmar nueva clave: ").strip()
                
                # Validamos: coincidencia de claves
                if nueva_clave == confirmacion_clave:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden. No se realizó el cambio.")

            elif opcion == "3":
                print("\n«El éxito es la suma de pequeños esfuerzos repetidos día tras día.»")

            elif opcion == "4":
                print("\nSesión cerrada. ¡Nos vemos pronto!")


#Ejercicio_3: “Agenda de Turnos con Nombres (sin listas)”

# Se inicia turnos para Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Se inicia turnos para Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""

# Se valida el operador (donde se debe colocar solo letras)
operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Nombre inválido. Debe contener solo letras.")
    operador = input("Ingrese el nombre del operador: ")

opcion = ""

while opcion != "5":
    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- RESERVAR TURNO ---")
        dia = input("Seleccione el día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Opción inválida. Ingrese 1 para Lunes o 2 para Martes: ")

        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese solo letras: ")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno reservado el día Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado con éxito en Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado con éxito en Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado con éxito en Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado con éxito en Lunes (Turno 4).")
            else:
                print("No hay cupos disponibles para el día Lunes.")

        elif dia == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno reservado el día Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado con éxito en Martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado con éxito en Martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado con éxito en Martes (Turno 3).")
            else:
                print("No hay cupos disponibles para el día Martes.")

    elif opcion == "2":
        print("\n--- CANCELAR TURNO ---")
        dia = input("Seleccione el día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Opción inválida. Ingrese 1 para Lunes o 2 para Martes: ")

        paciente = input("Ingrese el nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese solo letras: ")

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno 1 del Lunes cancelado.")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno 2 del Lunes cancelado.")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno 3 del Lunes cancelado.")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno 4 del Lunes cancelado.")
            else:
                print("El paciente no fue encontrado en los turnos del Lunes.")

        elif dia == "2":
            if martes1 == paciente:
                martes1 = ""
                print("Turno 1 del Martes cancelado.")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno 2 del Martes cancelado.")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno 3 del Martes cancelado.")
            else:
                print("El paciente no fue encontrado en los turnos del Martes.")

    elif opcion == "3":
        print("\n--- VER AGENDA DEL DÍA ---")
        dia = input("Seleccione el día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Opción inválida. Ingrese 1 para Lunes o 2 para Martes: ")

        if dia == "1":
            print("Agenda Lunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        elif dia == "2":
            print("Agenda Martes:")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == "4":
        print("\n--- RESUMEN GENERAL ---")
        
        # Conteo Lunes
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        # Conteo Martes
        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print(f"Lunes: {ocupados_lunes} ocupados, {libres_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {libres_martes} disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados (Empate).")

    elif opcion == "5":
        print(f"\nCerrando sistema. ¡Hasta luego, {operador}!")

    else:
        print("Opción inválida. Por favor, seleccione un número del 1 al 5.")

#Ejercicio_4: " “Escape Room: La Bóveda”"
# Variables iniciales (NO se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

# Validamos el nombre del agente
agente = input("Ingrese el nombre del agente: ")
while not agente.isalpha():
    agente = input("Nombre inválido. Ingrese solo letras: ")

print(f"\nBienvenido Agente {agente}. Tu misión para abrir la bóveda comienza ahora.")

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Verificación de bloqueo por alarma
    if alarma and tiempo <= 3:
        break

    # Estado actual
    print("\n----------------------------------------")
    print(f"Estado -> Energía: {energia} | Tiempo: {tiempo}h | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Inactiva'} | Código Parcial: '{codigo_parcial}'")
    print("----------------------------------------")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Elija una acción (1-3): ")
    while not (opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3")):
        opcion = input("Opción inválida. Ingrese 1, 2 o 3: ")

    if opcion == "1":
        # Se actualizan recursos
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        print("\nIntentando forzar la cerradura...")

        # Aplicación de la regla anti spam (3ra vez seguida)
        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabó por forzar repetidamente. ¡Se ha activado la alarma!")
        else:
            # Riesgo de alarma si energía es menor a 40
            if energia < 40:
                print("Riesgo de alarma por baja energía. Elija una vía de escape:")
                print("1. Vía A")
                print("2. Vía B")
                print("3. Vía C")

                via = input("Seleccione vía (1-3): ")
                while not (via.isdigit() and (via == "1" or via == "2" or via == "3")):
                    via = input("Entrada inválida. Ingrese 1, 2 o 3: ")

                if via == "3":
                    alarma = True
                    print("Elegiste la vía incorrecta. ¡Se activó la alarma!")

            # Si no se activó la alarma, se abre la cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")

    elif opcion == "2":
        forzar_seguidas = 0  # Corta la racha de forzar seguidas
        energia -= 10
        tiempo -= 3

        print("\nHackeando el panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 completado... Código actual: {codigo_parcial}")

        # Si el código tiene 8 o más letras y aún faltan cerraduras, se abre 1
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El panel se ha desvelado completamente! Se abrió 1 cerradura.")

    elif opcion == "3":
        forzar_seguidas = 0  # Corta la racha de forzar seguidas
        
        # Recuperación de energía (máximo 100)
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        print("\nTomando un descanso...")
        # Penalización si la alarma está encendida
        if alarma:
            energia -= 10
            print("Alarma activa: perdiste 10 de energía extra por la tensión del momento.")

# Mensajes de Fin de Juego
print("\n================ FIN DEL JUEGO ================")

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! Felicitaciones Agente {agente}, lograste abrir las 3 cerraduras y vulnerar la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA (Bloqueo por Alarma): El sistema detectó la amenaza con poco tiempo restante y bloqueó el acceso.")
elif energia <= 0:
    print("DERROTA: Te has quedado sin energía antes de abrir la bóveda.")
elif tiempo <= 0:
    print("DERROTA: Te has quedado sin tiempo antes de abrir la bóveda.")

#Ejercicio_5: “Escape Room:"La Arena del Gladiador"

# ==========================================
# PASO 1: CONFIGURACIÓN DEL PERSONAJE
# ==========================================
print("--- BIENVENIDO A LA ARENA ---")

nombre_jugador = input("Nombre del Gladiador: ")
while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_jugador = input("Nombre del Gladiador: ")

# ==========================================
# PASO 2: INICIALIZACIÓN DE ESTADÍSTICAS
# ==========================================
vida_jugador = 100               # int
vida_enemigo = 100               # int
pociones = 3                     # int
dano_pesado_base = 15            # int
dano_enemigo = 12                # int
turno_gladiador = True           # boolean
juego_activo = True              # boolean

print("\n=== INICIO DEL COMBATE ===")

# ==========================================
# PASO 3: EL CICLO DE COMBATE
# ==========================================
while vida_jugador > 0 and vida_enemigo > 0 and juego_activo:
    print(f"\n{nombre_jugador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Validación estricta del menú
    opcion = input("Opción: ")
    while not (opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3")):
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    # Lógica del turno del jugador
    if opcion == "1":
        # Acción A: ataque Pesado
        if vida_enemigo < 20:
            dano_final = dano_pesado_base * 1.5  # Cálculo float (22.5)
            print("⚡ ¡Golpe Crítico desatado!")
        else:
            dano_final = float(dano_pesado_base)

        vida_enemigo -= dano_final
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    elif opcion == "2":
        # Acción B: ráfaga veloz (Teniendo en cuento el: uso obligatorio de ciclo for)
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == "3":
        # Acción C: Curar
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"¡Te has curado 30 HP! Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones! Has perdido la oportunidad de curarte.")

    # Turno del Enemigo (solo ataca si aún tiene vida)
    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")

# ==========================================
# PASO 4: FIN DEL JUEGO
# ==========================================
print("\n=== FIN DE LA BATALLA ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
