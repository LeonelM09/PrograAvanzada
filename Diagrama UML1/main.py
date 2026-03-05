from models import*
#1er módulo
#10 objetos (Usuario)
u1 = Usuario(201, "Carlos88", "carlos@mail.com", "2221234567", 150)
u2 = Usuario(202, "AnaGamer", "ana.g@mail.com", "2229876543", 50)
u3 = Usuario(203, "Luis_Cine", "luis.c@mail.com", "2223456789", 300)
u4 = Usuario(204, "MariaVIP", "maria.v@mail.com", "2225678901", 1200)
u5 = Usuario(205, "Jorge123", "jorge@mail.com", "2228901234", 10)
u6 = Usuario(206, "SofiaPop", "sofia.p@mail.com", "2224567890", 85)
u7 = Usuario(207, "DiegoGeek", "diego.g@mail.com", "2226789012", 210)
u8 = Usuario(208, "Laura_M", "laura.m@mail.com", "2229012345", 0)
u9 = Usuario(209, "Miguel_89", "miguel.o@mail.com", "2221122334", 450)
u10 = Usuario(210, "Elena_Fan", "elena.f@mail.com", "2225566778", 75)
lista_usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]

#10 objetos (Empleado)
e1 = Empleado(301, "Roberto Garcia", "roberto@cine.com", "2221112233", "EMP01", "ADMIN", "Matutino")
e2 = Empleado(302, "Fernanda Lopez", "fernanda@cine.com", "2222223344", "EMP02", "TAQUILLERO", "Vespertino")
e3 = Empleado(303, "Hugo Martinez", "hugo@cine.com", "2223334455", "EMP03", "LIMPIEZA", "Nocturno")
e4 = Empleado(304, "Carmen Ruiz", "carmen@cine.com", "2224445566", "EMP04", "TAQUILLERO", "Matutino")
e5 = Empleado(305, "Ricardo Silva", "ricardo@cine.com", "2225556677", "EMP05", "LIMPIEZA", "Vespertino")
e6 = Empleado(306, "Valeria Diaz", "valeria@cine.com", "2226667788", "EMP06", "ADMIN", "Vespertino")
e7 = Empleado(307, "Andres Morales", "andres@cine.com", "2227778899", "EMP07", "TAQUILLERO", "Nocturno")
e8 = Empleado(308, "Natalia Castro", "natalia@cine.com", "2228889900", "EMP08", "LIMPIEZA", "Matutino")
e9 = Empleado(309, "Oscar Vargas", "oscar@cine.com", "2229990011", "EMP09", "TAQUILLERO", "Vespertino")
e10 = Empleado(310, "Patricia Luna", "patricia@cine.com", "2220001122", "EMP10", "ADMIN", "Nocturno")
lista_empleados = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

#2do módulo 
#10 objetos (Sala)
s1 = Sala(401, "Sala 1", "Planta Baja", "2D", 50, False)
s2 = Sala(402, "Sala 2", "Planta Baja", "3D", 60, False)
s3 = Sala(403, "Sala 3", "Planta Baja", "2D", 50, False)
s4 = Sala(404, "Sala 4 IMAX", "Planta Alta", "IMAX", 120, False)
s5 = Sala(405, "Sala 5", "Planta Alta", "2D", 40, False)
s6 = Sala(406, "Sala 6", "Planta Alta", "3D", 60, False)
s7 = Sala(407, "Sala 7 VIP", "Zona Exclusiva", "2D", 30, True)
s8 = Sala(408, "Sala 8 VIP", "Zona Exclusiva", "3D", 30, True)
s9 = Sala(409, "Sala 9", "Planta Baja", "2D", 45, False)
s10 = Sala(410, "Sala 10 IMAX", "Planta Alta", "IMAX", 100, False)
lista_salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

#10 objetos (ZonaComida)
zc1 = ZonaComida(501, "Dulcería Central", "Lobby Principal", {"Palomitas": 200, "Refresco": 150, "Nachos": 80})
zc2 = ZonaComida(502, "Café VIP", "Zona Exclusiva VIP", {"Café Americano": 50, "Crepas": 30, "Frappé": 40})
zc3 = ZonaComida(503, "Dulcería Express 1", "Pasillo Norte", {"Palomitas": 100, "Refresco": 100})
zc4 = ZonaComida(504, "Dulcería Express 2", "Pasillo Sur", {"Nachos": 50, "Icee": 60})
zc5 = ZonaComida(505, "Barra de Snacks", "Planta Baja", {"Chocolates": 120, "Gomitas": 150})
zc6 = ZonaComida(506, "Heladería", "Lobby Principal", {"Helado Sencillo": 80, "Malteada": 45})
zc7 = ZonaComida(507, "Lounge VIP", "Zona Exclusiva VIP", {"Cerveza Artesanal": 40, "Papas Gajo": 30})
zc8 = ZonaComida(508, "Carrito Dulces 1", "Entrada Salas 1-3", {"Papas Fritas": 60, "Agua Embotellada": 80})
zc9 = ZonaComida(509, "Carrito Dulces 2", "Entrada Salas 4-6", {"Papas Fritas": 60, "Agua Embotellada": 80})
zc10 = ZonaComida(510, "Dulcería IMAX", "Planta Alta", {"Palomitas Jumbo": 150, "Refresco Jumbo": 120})
lista_zonas = [zc1, zc2, zc3, zc4, zc5, zc6, zc7, zc8, zc9, zc10]

#3er módulo 
#10 objetos (Pelicula)
pel1 = Pelicula("Dune: Part Two", 166, "B15", "Ciencia Ficción")
pel2 = Pelicula("Deadpool & Wolverine", 127, "C", "Acción")
pel3 = Pelicula("Kung Fu Panda 4", 94, "A", "Animación")
pel4 = Pelicula("1984 (Edición Restaurada)", 113, "B15", "Ciencia Ficción")
pel5 = Pelicula("Joker: Folie à Deux", 138, "C", "Drama")
pel6 = Pelicula("IntensaMente 2", 100, "A", "Animación")
pel7 = Pelicula("Halo: The Fall of Reach", 65, "B", "Acción")
pel8 = Pelicula("Five Nights at Freddy's", 110, "B", "Terror")
pel9 = Pelicula("Gladiator II", 150, "B15", "Acción")
pel10 = Pelicula("Spider-Man: Beyond the Spider-Verse", 120, "A", "Animación")
lista_peliculas = [pel1, pel2, pel3, pel4, pel5, pel6, pel7, pel8, pel9, pel10]

#10 objetos (Funcion)
f1 = Funcion(601, pel1, s1, "14:00", 65.0)
f2 = Funcion(602, pel2, s4, "16:30", 120.0) 
f3 = Funcion(603, pel3, s2, "11:00", 80.0)  
f4 = Funcion(604, pel4, s7, "19:00", 150.0) 
f5 = Funcion(605, pel5, s5, "21:30", 65.0)
f6 = Funcion(606, pel6, s3, "13:15", 65.0)
f7 = Funcion(607, pel7, s6, "18:00", 80.0)
f8 = Funcion(608, pel8, s9, "22:00", 65.0)
f9 = Funcion(609, pel9, s10, "20:45", 120.0) 
f10 = Funcion(610, pel10, s8, "17:20", 150.0) 
lista_funciones = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

#4to módulo 
#10 objetos (Promocion)
pr1 = Promo("PROMO_ESTUDIANTE", "Descuento 20% general", 0.20, "2026-12-31")
pr2 = Promo("LUNES_2X1", "Dos por uno en entradas 2D", 0.50, "2026-12-31")
pr3 = Promo("MATINEE", "Descuento 30% antes de las 2 PM", 0.30, "2026-06-30")
pr4 = Promo("LOBOS_VIP", "15% descuento comunidad BUAP", 0.15, "2026-08-15")
pr5 = Promo("CUMPLEAÑOS", "Descuento 100% en tu entrada", 1.00, "2026-12-31")
pr6 = Promo("PAREJA_10", "10% de descuento en dulcería", 0.10, "2026-02-14")
pr7 = Promo("TARDES_LOCAS", "Descuento 25% de 4 PM a 6 PM", 0.25, "2026-10-31")
pr8 = Promo("CINEFILO_PRO", "12% de descuento clientes frecuentes", 0.12, "2026-12-31")
pr9 = Promo("PREVENTA_50", "50% de descuento en preventas", 0.50, "2026-05-01")
pr10 = Promo("NOCTURNO", "20% de descuento después de las 10 PM", 0.20, "2026-11-30")
lista_promos = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]

#10 objetos (Reserva)
r1 = Reserva(1001, u1, f1, ["A1", "A2"], 130.0, "PAGADA")
r2 = Reserva(1002, u2, f2, ["C4", "C5", "C6"], 360.0, "PENDIENTE")
r3 = Reserva(1003, u3, f3, ["B1"], 80.0, "PAGADA")
r4 = Reserva(1004, u4, f4, ["VIP1", "VIP2"], 300.0, "PAGADA")
r5 = Reserva(1005, u5, f5, ["D8"], 65.0, "CANCELADA")
r6 = Reserva(1006, u6, f6, ["E1", "E2", "E3"], 195.0, "PAGADA")
r7 = Reserva(1007, u7, f7, ["F4", "F5"], 160.0, "PENDIENTE")
r8 = Reserva(1008, u8, f8, ["A8"], 65.0, "PAGADA")
r9 = Reserva(1009, u9, f9, ["G10", "G11"], 240.0, "PAGADA")
r10 = Reserva(1010, u10, f10, ["VIP5"], 150.0, "CANCELADA")
lista_reservas = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]


while True:
    print("\n" + "="*50)
    print("SISTEMA DE CINE BUAP")
    print("="*50)
    print("1. Consultar Instancias (Ver listas)")
    print("2. Gestión de Infraestructura (Limpiar Salas)")
    print("3. Gestión Comercial (Aplicar Descuentos)")
    print("4. Proceso de Reserva")
    print("5. Panel Administrativo")
    print("6. Salir")
    
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        while True:
            print("\n--- CONSULTA DE INSTANCIAS ---")
            print("a) Usuarios   b) Empleados   c) Salas   d) Películas")
            print("e) Funciones  f) Promos      g) Comida  h) Volver")
            sub_op = input("\nSeleccione categoría: ").lower()
            if sub_op == "a":
                for u in lista_usuarios: print(f"ID: {u.idPersona} | {u.nombre} | Puntos: {u.pts}")
            elif sub_op == "b":
                for e in lista_empleados: print(f"Clave: {e.id_emp} | {e.nombre} | Rol: {e.cargo}")
            elif sub_op == "c":
                for s in lista_salas: print(f"ID: {s.id_Espacio} | {s.nombre} | Cap: {s.capacidad_T}")
            elif sub_op == "d":
                for p in lista_peliculas: print(f"Título: {p.titulo} | Clasif: {p.clasificacion}")
            elif sub_op == "e":
                for f in lista_funciones: print(f"ID: {f.id_Fun} | {f.pelicula.titulo} | {f.horario_Inicio}")
            elif sub_op == "f":
                for pr in lista_promos: print(f"Código: {pr.codigo} | Desc: {int(pr.porcentaje_desc*100)}%")
            elif sub_op == "g":
                for zc in lista_zonas: print(f"ID: {zc.id_Espacio} | {zc.nombre} | Stock: {list(zc.stock.keys())}")
            elif sub_op == "h": break

    elif opcion == "2":
        print("\n--- GESTIÓN DE INFRAESTRUCTURA ---")
        for i, s in enumerate(lista_salas): print(f"{i}. {s.nombre} ({s.obt_tip_sala()})")
        idx = int(input("Seleccione sala: "))
        if 0 <= idx < len(lista_salas):
            sala_sel = lista_salas[idx]
            print("1. Limpiar Sala  2. Ajustar Aforo  3. Verificar Disponibilidad")
            acc = input("Acción: ")
            if acc == "1": sala_sel.limpiar_estado()
            elif acc == "2":
                nuevo = int(input(f"Capacidad actual {sala_sel.capacidad_T}. Nueva capacidad: "))
                sala_sel.ajustar_afo(nuevo)
            elif acc == "3":
                print(f"¿Está disponible?: {'Sí' if sala_sel.verif_disp(True) else 'No'}")

    elif opcion == "3":
        print("\n--- GESTIÓN COMERCIAL Y CONTENIDO ---")
        print("1. Ver Sinopsis y Clasificación  2. Consultar Asientos Libres  3. Vender en Dulcería")
        acc = input("Seleccione: ")
        
        if acc == "1":
            for i, p in enumerate(lista_peliculas): print(f"{i}. {p.titulo}")
            p_sel = lista_peliculas[int(input("Película: "))]
            print(f"\nSinopsis: {p_sel.obt_sinop()}")
            print(f"¿Apta para todo público?: {'Sí' if p_sel.es_apta_todo_publi() else 'No'}")
            
        elif acc == "2":
            for i, f in enumerate(lista_funciones): print(f"{i}. {f.pelicula.titulo} ({f.horario_Inicio})")
            f_sel = lista_funciones[int(input("Función: "))]
            f_sel.obt_detall_func()
            print(f"Asientos libres: {f_sel.calc_asient_libres()}")
            
        elif acc == "3":
            for i, z in enumerate(lista_zonas): print(f"{i}. {z.nombre}")
            z_sel = lista_zonas[int(input("Zona de comida: "))]
            print(f"Inventario: {z_sel.stock}")
            prod = input("Producto a vender: ")
            cant = int(input("Cantidad: "))
            z_sel.vender_Producto(prod, cant)

    elif opcion == "4":
        print("\n>>> INICIANDO PROCESO DE RESERVA INTERACTIVA")
        for i, u in enumerate(lista_usuarios): print(f"{i}. {u.nombre}")
        u_sel = lista_usuarios[int(input("Seleccione el índice del usuario: "))]
        
        for i, f in enumerate(lista_funciones): print(f"{i}. {f.pelicula.titulo} ({f.horario_Inicio})")
        f_sel = lista_funciones[int(input("Seleccione el índice de la función: "))]
        
        while True:
            print(f"\nAsientos ocupados: {f_sel.asientos_ocupados}")
            entrada = input("Seleccione asientos (ej: A1, A2): ")
          
            asientos_brutos = entrada.split(",")
            asientos = []
            for a in asientos_brutos:
                asientos.append(a.strip())
            
            if f_sel.verificar_y_ocupar_asientos(asientos): break
            else: print("[SISTEMA]: Intente de nuevo.")

        monto_b = len(asientos) * f_sel.precio_Base
        reserva = Reserva(999, u_sel, f_sel, asientos, monto_b, "PENDIENTE")
        
        if input("¿Tiene código de promo? (s/n): ").lower() == 's':
            cod = input("Código: ")
            p_obj = None
            for p in lista_promos:
                if p.codigo == cod:
                    p_obj = p
                    break
            if p_obj: reserva.aplicar_promo(p_obj)
        
        reserva.confirmar_pago()
        reserva.generar_ticket()

    elif opcion == "5":
            print("\n--- PANEL ADMINISTRATIVO Y EMPLEADOS ---")
            for i, e in enumerate(lista_empleados): print(f"{i}. {e.nombre} ({e.cargo})")
            e_sel = lista_empleados[int(input("¿Quién realiza la acción?: "))]
            
            print("\n1. Marcar Entrada  2. Agregar Contenido (Admin)")
            acc = input("Seleccione: ")
            
            if acc == "1":
                e_sel.marcar_entrada()
            elif acc == "2":
                print("\n1. Película  2. Función  3. Promo")
                tipo = input("Tipo: ")
    
                if tipo == "1":
                    t = input("Título: "); d = int(input("Duración: ")); c = input("Clasif: "); g = input("Género: ")
                    nueva_p = e_sel.agregar_pelicula(t, d, c, g)
                    if nueva_p: lista_peliculas.append(nueva_p)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break