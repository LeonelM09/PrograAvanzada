#Cafetería 
from models import*

#Personas 

emp1 = Empleado(201, "Carlos Rivera", "carlos.r@cafeteria.com", "E-001", RolEmpleado.GERENTE)
emp2 = Empleado(202, "Ana Gómez", "ana.g@cafeteria.com", "E-002", RolEmpleado.BARISTA)
emp3 = Empleado(203, "Luis Martínez", "luis.m@cafeteria.com", "E-003", RolEmpleado.BARISTA)
emp4 = Empleado(204, "María López", "maria.l@cafeteria.com", "E-004", RolEmpleado.MESERO)
emp5 = Empleado(205, "Jorge Pérez", "jorge.p@cafeteria.com", "E-005", RolEmpleado.MESERO)
emp6 = Empleado(206, "Sofía Castro", "sofia.c@cafeteria.com", "E-006", RolEmpleado.BARISTA)
emp7 = Empleado(207, "Diego Torres", "diego.t@cafeteria.com", "E-007", RolEmpleado.MESERO)
emp8 = Empleado(208, "Laura Méndez", "laura.m@cafeteria.com", "E-008", RolEmpleado.MESERO)
emp9 = Empleado(209, "Miguel Ortiz", "miguel.o@cafeteria.com", "E-009", RolEmpleado.BARISTA)
emp10 = Empleado(210, "Elena Ruiz", "elena.r@cafeteria.com", "E-010", RolEmpleado.GERENTE)

lista_empleados = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]

cli1 = Cliente(301, "Roberto Sánchez", "roberto.s@gmail.com", 120, [])
cli2 = Cliente(302, "Lucía Fernández", "lucia.f@hotmail.com", 50, [])
cli3 = Cliente(303, "Mario Vargas", "mario.v@yahoo.com", 300, [])
cli4 = Cliente(304, "Fernanda Castillo", "fer.castillo@gmail.com", 0, [])
cli5 = Cliente(305, "Hugo Domínguez", "hugo.d@empresa.com", 450, [])
cli6 = Cliente(306, "Valeria Luna", "val.luna@gmail.com", 80, [])
cli7 = Cliente(307, "Andrés Moreno", "andres.m@outlook.com", 15, [])
cli8 = Cliente(308, "Paola Núñez", "paola.n@gmail.com", 210, [])
cli9 = Cliente(309, "Ricardo Reyes", "ricardo.r@yahoo.com", 90, [])
cli10 = Cliente(310, "Gabriela Silva", "gaby.silva@hotmail.com", 5, [])

lista_clientes = [cli1, cli2, cli3, cli4, cli5, cli6, cli7, cli8, cli9, cli10]

#Productos 

beb1 = Bebida(401, "Café Americano", 35.0, "Mediano", TempBebida.CALIENTE)
beb2 = Bebida(402, "Cappuccino", 55.0, "Grande", TempBebida.CALIENTE)
beb3 = Bebida(403, "Latte Vainilla", 60.0, "Grande", TempBebida.CALIENTE)
beb4 = Bebida(404, "Frappé Mocha", 75.0, "Mediano", TempBebida.FRIA)
beb5 = Bebida(405, "Té Verde Matcha", 50.0, "Chico", TempBebida.CALIENTE)
beb6 = Bebida(406, "Smoothie de Fresa", 65.0, "Grande", TempBebida.FRIA)
beb7 = Bebida(407, "Espresso Doble", 40.0, "Chico", TempBebida.CALIENTE)
beb8 = Bebida(408, "Limonada Mineral", 45.0, "Mediano", TempBebida.FRIA)
beb9 = Bebida(409, "Caramel Macchiato", 65.0, "Mediano", TempBebida.CALIENTE)
beb10 = Bebida(410, "Cold Brew", 70.0, "Grande", TempBebida.FRIA)

lista_bebidas = [beb1, beb2, beb3, beb4, beb5, beb6, beb7, beb8, beb9, beb10]

pos1 = Postre(501, "Rebanada Pastel de Chocolate", 65.0, False, False)
pos2 = Postre(502, "Galleta de Avena y Pasas", 25.0, True, False)
pos3 = Postre(503, "Brownie Especial", 45.0, False, True)
pos4 = Postre(504, "Cheesecake de Frambuesa", 75.0, False, False)
pos5 = Postre(505, "Muffin de Arándanos", 35.0, False, False)
pos6 = Postre(506, "Tartaleta de Manzana", 50.0, True, True)
pos7 = Postre(507, "Croissant de Mantequilla", 30.0, False, False)
pos8 = Postre(508, "Macaron de Pistache", 20.0, False, True)
pos9 = Postre(509, "Dona Glaseada Clásica", 25.0, False, False)
pos10 = Postre(510, "Pudín de Chía y Mango", 55.0, True, True)  

lista_postres = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10]

#Logística y Ventas

stock_inicial = {
    "Cafe_Grano": 5000,
    "Leche_Entera": 10000,
    "Leche_Almendra": 3000,
    "Azucar": 2000,
    "Matcha_Polvo": 500,
    "Jarabe_Vainilla": 1000,
    "Chocolate": 1500,
    "Masa_Pastel": 4000
}

inventario_central = Inventario(stock_inicial)

pedidos_globales = [] 
contador_pedidos = 1

catalogo_extras = [
    "Leche de Almendra", 
    "Leche de Soya", 
    "Extra Shot de Espresso", 
    "Jarabe de Vainilla", 
    "Crema Batida", 
    "Sin Azúcar"
]

while True:
    print("SISTEMA DE CAFETERÍA INTERACTIVO")
    print("1.Simular Compra (Interacción Cliente)")
    print("2.Panel de Empleados (Gestionar Pedidos)")
    print("3.Consultar Inventario Central")
    print("4.Consultar Objetos")
    print("5.Cambiar datos")
    print("6.Salir")
    
    opcion = input("Selecciona una opción (1-6):")

    if opcion == "1":
        print("\n--- SELECCIÓN DE CLIENTE ---")
        for i, c in enumerate(lista_clientes):
            print(f"{i + 1}. {c.nombre} (Puntos: {c.pF})")
        
        try:
            indice_cliente = int(input("\nIngresa el número de tu cliente: ")) - 1
            cliente_actual = lista_clientes[indice_cliente]
        except (ValueError, IndexError):
            print("Selección no válida. Volviendo al menú principal")
            continue

        print(f"¡Bienvenido, {cliente_actual.nombre}! Iniciando orden #{contador_pedidos}...")
        nuevo_pedido = Pedido(contador_pedidos, EstadoPedido.PENDIENTE)
        
        while True:
            print("MENÚ DE PRODUCTOS")
            print("1.Ver y agregar Bebidas")
            print("2.Ver y agregar Postres")
            print("3.Finalizar pedido y Pagar")
            prod_op = input("Elige una categoría: ")
            
            if prod_op == "1":
                print("\n--- CATÁLOGO DE BEBIDAS ---")
                for i, b in enumerate(lista_bebidas):
                    print(f"{i + 1}. {b.nombre} ({b.tamaño}) - ${b.pB}")
                
                try:
                    idx_b = int(input("Elige el número de la bebida: ")) - 1
                    bebida_elegida = lista_bebidas[idx_b]
                    
                    bebida_elegida.modificadores = [] 
                    
                    while True:
                        print(f"\n¿Deseas agregar extras a tu {bebida_elegida.nombre}? ($15 c/u)")
                        for i, ext in enumerate(catalogo_extras):
                            print(f"  {i + 1}. {ext}")
                        print("  0. No, gracias / Terminar de agregar extras")
                        
                        op_extra = input("Elige una opción (0-6): ")
                        if op_extra == "0":
                            break 
                        try:
                            idx_e = int(op_extra) - 1
                            if 0 <= idx_e < len(catalogo_extras):
                                bebida_elegida.agregar_Extra(catalogo_extras[idx_e])
                            else:
                                print("Opción de extra inválida.")
                        except ValueError:
                            print("Ingresa un número válido.")
                    
                    nuevo_pedido.produc.append(bebida_elegida)
                    print(f"{bebida_elegida.nombre} agregado al pedido.")
                except:
                    print("Selección inválida.")

            elif prod_op == "2":
                print("\n--- CATÁLOGO DE POSTRES ---")
                for i, p in enumerate(lista_postres):
                    print(f"{i + 1}. {p.nombre} - ${p.pB}")
                
                try:
                    idx_p = int(input("Elige el número del postre: ")) - 1
                    postre_elegido = lista_postres[idx_p]
                    nuevo_pedido.produc.append(postre_elegido)
                    print(f"{postre_elegido.nombre} agregado al pedido.")
                except:
                    print("Selección inválida.")
            
            elif prod_op == "3":
                break
            else:
                print("Categoría no válida.")
        
        if len(nuevo_pedido.produc) > 0:
            total = nuevo_pedido.calcularTotal()
            
            cant_bebidas = len([p for p in nuevo_pedido.produc if isinstance(p, Bebida)])
            ingredientes_gastados = {
                "Cafe_Grano": 20 * cant_bebidas,
                "Leche_Entera": 50 * cant_bebidas
            }
            
            print("Validando existencias en inventario...")
            if nuevo_pedido.validarStock(inventario_central, ingredientes_gastados):
                for ing, cant in ingredientes_gastados.items():
                    inventario_central.reducirStock(ing, cant)
        
                cliente_actual.realizar_Pedido(nuevo_pedido)
                pedidos_globales.append(nuevo_pedido)
                contador_pedidos += 1
                print(f"Venta concretada. El pedido #{nuevo_pedido.id} está: {nuevo_pedido.estado.value}.")
            else:
                print("Venta detenida por falta de stock.")
        else:
            print("Pedido cancelado, el carrito quedó vacío.")

    elif opcion == "2":
        print("INGRESO DE EMPLEADOS")
        for i, emp in enumerate(lista_empleados):
            print(f"{i + 1}. {emp.nombre} ({emp.rol.value})")
        
        try:
            idx_emp = int(input("\nSelecciona tu usuario de empleado: ")) - 1
            empleado_actual = lista_empleados[idx_emp]
            print(f"Acceso concedido a {empleado_actual.nombre} ({empleado_actual.rol.value}).")
            
            print("¿Qué acción deseas realizar?")
            print("1. Cambiar estado de un pedido")
            print("2. Resurtir inventario (Solo Gerentes)")
            acc_emp = input("Elige (1-2): ")
            
            if acc_emp == "1":
                if not pedidos_globales:
                    print("No hay pedidos registrados en el sistema todavía.")
                else:
                    print("PEDIDOS ACTIVOS")
                    for ped in pedidos_globales:
                        print(f"Pedido #{ped.id} | Estado: {ped.estado.value} | Total: ${ped.total}")
                    
                    id_mod = int(input("Ingresa el ID del pedido a actualizar (0 para salir):"))
                    if id_mod != 0:
                        pedido_mod = next((p for p in pedidos_globales if p.id == id_mod), None)
                        if pedido_mod:
                            print("1. PENDIENTE  |  2. PREPARANDO  |  3. ENTREGADO")
                            op_estado = input("Elige el nuevo estado (1-3): ")
                            if op_estado == "1": empleado_actual.cambiarEstadoPedido(pedido_mod, EstadoPedido.PENDIENTE)
                            elif op_estado == "2": empleado_actual.cambiarEstadoPedido(pedido_mod, EstadoPedido.PREPARANDO)
                            elif op_estado == "3": empleado_actual.cambiarEstadoPedido(pedido_mod, EstadoPedido.ENTREGADO)
                        else:
                            print("Pedido no encontrado.")
                            
            elif acc_emp == "2":
                if empleado_actual.rol == RolEmpleado.GERENTE:
                    print("INVENTARIO ACTUAL")
                    for ing, cant in inventario_central.ingredientes.items():
                        print(f"- {ing}: {cant}")
                        
                    ing_nuevo = input("\nEscribe el nombre EXACTO del ingrediente a resurtir: ")
                    if ing_nuevo in inventario_central.ingredientes:
                        cant_nueva = int(input(f"¿Cuántas unidades sumarás a '{ing_nuevo}'?: "))
                        empleado_actual.actualizar_Invent(ing_nuevo, cant_nueva)
                        inventario_central.ingredientes[ing_nuevo] += cant_nueva
                        print(f"Nuevo stock de {ing_nuevo} -> {inventario_central.ingredientes[ing_nuevo]}")
                    else:
                        print("El ingrediente no existe en el catálogo.")
                else:
                    print(f"Tu rol es {empleado_actual.rol.value}. Solo los GERENTES pueden abastecer.")
            else:
                print("Acción no válida.")
                
        except (ValueError, IndexError):
            print("Entrada inválida.")

    elif opcion == "3":
        print("ESTADO DEL INVENTARIO CENTRAL")
        for ing, cant in inventario_central.ingredientes.items():
            print(f"- {ing}: {cant} unidades")

    elif opcion == "4":
        print("REGISTROS DEL SISTEMA (INSTANCIAS)"                  )
        print("1. Ver Empleados")
        print("2. Ver Clientes")
        print("3. Ver Bebidas")
        print("4. Ver Postres")
        op_reg = input("Elige qué catálogo deseas consultar (1-4): ")

        if op_reg == "1":
            print("EMPLEADOS REGISTRADOS:")
            for e in lista_empleados:
                print(f"ID: {e.idEmpleado} | Nombre: {e.nombre} | Rol: {e.rol.value}")
        elif op_reg == "2":
            print("CLIENTES REGISTRADOS:")
            for c in lista_clientes:
                print(f"ID: {c.idPersona} | Nombre: {c.nombre} | Puntos: {c.pF} | Compras: {len(c.hP)}")
        elif op_reg == "3":
            print("BEBIDAS REGISTRADAS:")
            for b in lista_bebidas:
                print(f"ID: {b.id} | {b.nombre} ({b.tamaño}) | Temp: {b.temp.value} | Precio Base: ${b.pB}")
        elif op_reg == "4":
            print("POSTRES REGISTRADOS:")
            for p in lista_postres:
                v = "Sí" if p.esVegano else "No"
                g = "Sí" if p.sinGluten else "No"
                print(f"ID: {p.id} | {p.nombre} | Vegano: {v} | Sin Gluten: {g} | Precio: ${p.pB}")
        else:
            print("Opción de registro no válida.")

    elif opcion == "5":
        print("ACTUALIZACIÓN DE PERFIL")
        print("¿De qué tipo de usuario deseas actualizar los datos?")
        print("1. Cliente")
        print("2. Empleado")
        tipo_perfil = input("Elige una opción (1-2): ")

        usuario_modificar = None

        if tipo_perfil == "1":
            print("\n>> CATÁLOGO DE CLIENTES:")
            for i, c in enumerate(lista_clientes):
                print(f"{i + 1}. {c.nombre} - Correo: {c.email}")
            try:
                idx = int(input("\nSelecciona el número del cliente a modificar: ")) - 1
                usuario_modificar = lista_clientes[idx]
            except (ValueError, IndexError):
                print(" Selección inválida.")
                
        elif tipo_perfil == "2":
            print("CATÁLOGO DE EMPLEADOS:")
            for i, e in enumerate(lista_empleados):
                print(f"{i + 1}. {e.nombre} - Correo: {e.email}")
            try:
                idx = int(input("\nSelecciona el número del empleado a modificar: ")) - 1
                usuario_modificar = lista_empleados[idx]
            except (ValueError, IndexError):
                print("Selección inválida.")
        else:
            print("Opción no válida.")

        if usuario_modificar:
            print(f"Editando el perfil de: {usuario_modificar.nombre}")
            
            nuevo_nom = input(f"Ingresa el nuevo nombre (Actual: {usuario_modificar.nombre}): ")
            nuevo_correo = input(f"Ingresa el nuevo email (Actual: {usuario_modificar.email}): ")
            
            nom_final = nuevo_nom if nuevo_nom.strip() != "" else usuario_modificar.nombre
            correo_final = nuevo_correo if nuevo_correo.strip() != "" else usuario_modificar.email
            
            usuario_modificar.actualizar_Perfil(nom_final, correo_final)
      
    elif opcion == "6":
        print("¡Hasta pronto!")
        break
        
    else:
        print("Opción no válida. Intenta de nuevo.")
