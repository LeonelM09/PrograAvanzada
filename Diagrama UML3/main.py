from models import*

# Sedes
sede_central = Sucursal(1, "Biblioteca Central BUAP")
sede_computacion = Sucursal(2, "Facultad de Ciencias de la Computación")

# Catálogo Global
catalogo_global = Catalogo([sede_central, sede_computacion])

# Bibliotecarios
biblio1 = Bibliotecario(901, "Roberto", "roberto@buap.mx", sucursal_asignada=sede_central)
biblio2 = Bibliotecario(902, "Laura", "laura@buap.mx", sucursal_asignada=sede_computacion)

# 10 Materiales
m1 = Libro(101, "1984", 1949, "George Orwell", "978-01", "Ficción Distópica")
m2 = Libro(102, "El proceso", 1925, "Franz Kafka", "978-02", "Novela Filosófica")
m3 = Libro(103, "Rayuela", 1963, "Julio Cortázar", "978-03", "Novela")
m4 = Libro(104, "Cien años de soledad", 1967, "Gabriel García Márquez", "978-04", "Realismo Mágico")
m5 = Libro(105, "Pedro Páramo", 1955, "Juan Rulfo", "978-05", "Novela")
m6 = Libro(106, "Don Quijote de la Mancha", 1605, "Miguel de Cervantes", "978-06", "Novela de Aventuras")
m7 = Revista(201, "Gaceta BUAP", 2026, 45, "Mensual")
m8 = Revista(202, "PC Gamer LATAM", 2026, 12, "Semanal")
m9 = MaterialDigital(301, "The Art of NieR: Automata", 2017, "PDF", "biblioteca.buap/nier", 150.5)
m10 = MaterialDigital(302, "Halo: The Fall of Reach", 2001, "EPUB", "biblioteca.buap/halo", 3.2)

lista_materiales = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

# Asignamos materiales a las sucursales
for mat in [m1, m3, m5, m7, m9]: sede_central.agregar_material(mat)
for mat in [m2, m4, m6, m8, m10]: sede_computacion.agregar_material(mat)

# 10 Usuarios
u1 = Usuario(1, "Leonel Matos", "leonel@email.com")
u2 = Usuario(2, "Annie", "annie@email.com")
u3 = Usuario(3, "Carlos Rivera", "carlos@email.com")
u4 = Usuario(4, "Sofia Castro", "sofia@email.com")
u5 = Usuario(5, "Luis Martinez", "luis@email.com")
u6 = Usuario(6, "Maria Lopez", "maria@email.com")
u7 = Usuario(7, "Diego Torres", "diego@email.com")
u8 = Usuario(8, "Jorge Perez", "jorge@email.com")
u9 = Usuario(9, "Miguel Ortiz", "miguel@email.com")
u10 = Usuario(10, "Elena Ruiz", "elena@email.com")

lista_usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]

while True:
    print("SISTEMA DE BIBLIOTECA MULTI-SEDE")
    print("1.Portal de Usuario (Búsquedas)")
    print("2.Panel de Bibliotecario (Préstamos y Multas)")
    print("3.Ver Registros (Evidencia de Instanciación)")
    print("4.Salir del Sistema")
    
    op = input("\nSelecciona tu perfil de acceso (1-4):")

    if op == "1":
        # --- MENÚ DE USUARIO ---
        while True:
            print("\n--- PORTAL DE USUARIO ---")
            print("1. Buscar material por Título")
            print("2. Buscar libro por Autor")
            print("3. Volver al menú principal")
            op_usr = input("Elige (1-3): ")
            
            if op_usr == "1":
                tit = input("Ingresa el título a buscar: ")
                catalogo_global.buscarEnTodasSucursales(tit)
            elif op_usr == "2":
                aut = input("Ingresa el nombre del autor: ")
                catalogo_global.buscarPorAutor(aut)
            elif op_usr == "3":
                break
            else:
                print("Opción inválida.")

    elif op == "2":
        # --- SELECCIÓN DE BIBLIOTECARIO ---
        print("\n--- INGRESO DE PERSONAL ---")
        print(f"1. {biblio1.nombre} (Sede: {biblio1.sucursal_asignada.nombre})")
        print(f"2. {biblio2.nombre} (Sede: {biblio2.sucursal_asignada.nombre})")
        op_emp = input("Selecciona tu usuario (1-2): ")
        
        if op_emp == "1":
            bibliotecario_activo = biblio1
        elif op_emp == "2":
            bibliotecario_activo = biblio2
        else:
            print("Selección inválida. Regresando al menú principal...")
            continue # Regresa al bucle principal

        # --- MENÚ DE BIBLIOTECARIO ---
        while True:
            print(f"\n--- PANEL DE LOGÍSTICA ({bibliotecario_activo.nombre} - {bibliotecario_activo.sucursal_asignada.nombre}) ---")
            print("1. Gestionar Préstamo Nuevo")
            print("2. Recibir Devolución de Material")
            print("3. Transferir Material a otra Sede")
            print("4. Aplicar Penalización (Bloquear Usuario)")
            print("5. Cerrar sesión y volver al menú principal")
            op_bib = input("Elige una acción (1-5): ")

            if op_bib == "1":
                print("\n[Usuarios Disponibles]:")
                for u in lista_usuarios: print(f"ID:{u.idPersona} - {u.nombre}")
                try:
                    id_u = int(input("Ingresa el ID del usuario: "))
                    usr = next((u for u in lista_usuarios if u.idPersona == id_u), None)
                    if usr:
                        id_m = int(input("Ingresa el ID del material a prestar: "))
                        mat = next((m for m in lista_materiales if m.idMaterial == id_m), None)
                        if mat:
                            hoy = datetime.date.today()
                            entrega = hoy + datetime.timedelta(days=7)
                            bibliotecario_activo.gestionarPrestamo(usr, mat, hoy, entrega)
                        else:
                            print("Material no encontrado.")
                    else:
                        print("Usuario no encontrado.")
                except ValueError:
                    print("Entrada inválida. Usa solo números.")

            elif op_bib == "2":
                try:
                    id_m = int(input("\nIngresa el ID del material devuelto:"))
                    mat = next((m for m in lista_materiales if m.idMaterial == id_m), None)
                    if mat and not mat.disponible:
                        mat.devolver()
                    elif mat and mat.disponible:
                        print("Ese material ya consta como disponible en el sistema.")
                    else:
                        print("Material no encontrado.")
                except ValueError:
                    print("Entrada inválida.")

            elif op_bib == "3":
                try:
                    id_m = int(input("\nIngresa el ID del material a enviar:"))
                    mat = next((m for m in lista_materiales if m.idMaterial == id_m), None)
                    if mat:
                        print("Selecciona destino: 1. Sede Central | 2. Ciencias de la Computación")
                        dest = input("Elige (1-2): ")
                        sede_dest = sede_central if dest == "1" else sede_computacion
                        bibliotecario_activo.transferirMaterial(mat, sede_dest)
                    else:
                        print("Material no encontrado.")
                except ValueError:
                    print("Entrada inválida.")

            elif op_bib == "4":
                try:
                    id_u = int(input("\nIngresa el ID del usuario a penalizar: "))
                    usr = next((u for u in lista_usuarios if u.idPersona == id_u), None)
                    if usr:
                        dias = int(input("¿Cuántos días de retraso tiene?: "))
                        motivo = input("Escribe el motivo de la multa: ")
                        multa = Penalizacion(0, motivo, usr)
                        multa.calcularMulta(dias)
                        multa.bloquearUsuario()
                    else:
                        print("Usuario no encontrado.")
                except ValueError:
                    print("Entrada inválida.")

            elif op_bib == "5":
                print(f"Cerrando sesión de {bibliotecario_activo.nombre}...")
                break
            else:
                print("Opción inválida.")

    # --- OPCIÓN 3: VER EVIDENCIA DE INSTANCIAS ---
    elif op == "3":
        print("REGISTRO DE OBJETOS EN MEMORIA")
        
        print("\nSUCURSALES INSTANCIADAS:")
        print(f"- {sede_central.nombre} (ID: {sede_central.idSucursal}) | Inventario: {len(sede_central.catalogoLocal)} materiales")
        print(f"- {sede_computacion.nombre} (ID: {sede_computacion.idSucursal}) | Inventario: {len(sede_computacion.catalogoLocal)} materiales")
        
        print("\nBIBLIOTECARIOS INSTANCIADOS:")
        print(f"- {biblio1.nombre} (ID: {biblio1.idPersona}) | Sede: {biblio1.sucursal_asignada.nombre}")
        print(f"- {biblio2.nombre} (ID: {biblio2.idPersona}) | Sede: {biblio2.sucursal_asignada.nombre}")
        
        print("\nUSUARIOS REGISTRADOS (Muestra de los primeros 5):")
        for u in lista_usuarios[:5]:
            estado = "Bloqueado" if u.bloqueado else " Activo"
            print(f"- [ID: {u.idPersona}] {u.nombre} | Estado: {estado} | Préstamos activos: {len(u.listaActiva)}")
            
        print("\nMATERIALES EN EL SISTEMA:")
        for m in lista_materiales:
            tipo_clase = type(m).__name__
            disponibilidad = "Disponible" if m.disponible else "Prestado"
            print(f"- [ID: {m.idMaterial}] {m.titulo} ({tipo_clase}) -> {disponibilidad}")
        
        input("\nPresiona ENTER para volver al menú principal...")

    # --- OPCIÓN 4: SALIR ---
    elif op == "4":
        print("\nApagando sistema de biblioteca... ¡Hasta pronto!")
        break
    else:
        print("Por favor, selecciona del 1 al 4.")