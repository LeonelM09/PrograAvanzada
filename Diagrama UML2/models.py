#Personas 
from enum import Enum

class RolEmpleado(Enum):
    BARISTA = "BARISTA"
    MESERO = "MESERO"
    GERENTE = "GERENTE"

class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email

    def login(self):
        print(f"El usuario {self.nombre} ({self.email}) ha iniciado sesión.")

    def actualizar_Perfil(self,nom,email):
        self.nombre=nom
        self.email=email
        print(f"Perfil de {self.nombre} actualizado correctamente.")

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email, puntosFide, historialPed):
        super().__init__(idPersona, nombre, email)
        self.pF=puntosFide
        self.hP=historialPed
        self.pedido=[]

    def realizar_Pedido(self,nuevo_pedido):
        self.hP.append(nuevo_pedido)
        self.pF += 10
        print(f"Pedido registrado para {self.nombre}. Puntos actuales: {self.pF}")

    def consultar_Historial(self):
        print(f"\n--- HISTORIAL DE COMPRAS: {self.nombre.upper()} ---")
        if not self.hP:
            print("No hay pedidos en el historial de este cliente.")
        else:
            for i, ped in enumerate(self.hP):
                print(f"{i + 1}. Pedido ID: {ped.id} | Total: ${ped.total} | Estado: {ped.estado.name}")

    def canjear_Puntos(self, puntos_necesarios):
        if self.pF >= puntos_necesarios:
            self.pF -= puntos_necesarios
            print(f"¡Descuento aplicado! {self.nombre} canjeó {puntos_necesarios} puntos. Restantes: {self.pF}.")
            return True
        else:
            print(f"Puntos insuficientes. {self.nombre} tiene {self.pF} y necesita {puntos_necesarios}.")
            return False

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado=idEmpleado
        self.rol=rol

    def actualizar_Invent(self, ingrediente, cantidad):
        print(f"[{self.rol.value} - {self.nombre}]: Actualizando inventario...")
        print(f"Se han registrado {cantidad} unidades nuevas de '{ingrediente}'.")

    def cambiarEstadoPedido(self, pedido, nuevo_estado):
        print(f"[{self.rol.value} - {self.nombre}]: Modificando estado del pedido #{pedido.id}...")
        pedido.estado = nuevo_estado
        print(f"El pedido #{pedido.id} se encuentra: {nuevo_estado.name}")

#Productos 

class TempBebida(Enum):
    FRIA = "FRÍA"
    CALIENTE = "CALIENTE"

class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.id=idProducto
        self.nombre=nombre
        self.pB=precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño=tamaño
        self.temp=temperatura
        self.modificadores=[]

    def agregar_Extra(self, extra):
        self.modificadores.append(extra)
        print(f"Se agregó {extra} a tu {self.nombre}.")

    def calcular_precioF(self, costo_por_extra=15.0):
        total_extras = len(self.modificadores) * costo_por_extra
        precio_final = self.pB + total_extras
        print(f"Cotización de {self.nombre} ({self.tamaño} - {self.temp.value}):")
        print(f"Precio Base: ${self.pB}")
        if self.modificadores:
            print(f"Extras ({len(self.modificadores)}): ${total_extras}")
        print(f"Total a pagar: ${precio_final}")
        
        return precio_final

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

#Lógistica y Ventas 

class EstadoPedido(Enum):
    PENDIENTE = "PENDIENTE"
    PREPARANDO = "PREPARANDO"
    ENTREGADO = "ENTREGADO"

class Pedido:
    def __init__(self, idPedido, estado, total=0.0):
        self.id=idPedido
        self.produc=[]
        self.estado=estado
        self.total=total

    def calcularTotal(self):
        self.total = 0.0
        print(f"CALCULANDO TOTAL DEL PEDIDO #{self.id} ---")
        for p in self.produc:
            if isinstance(p, Bebida):
                self.total += p.calcular_precioF() 
            else:
                print(f"Postre - {p.nombre} | ${p.pB}")
                self.total += p.pB
        
        print(f"El total a pagar es: ${self.total}")
        return self.total
    
    def validarStock(self, inventario, ingredientes_necesarios):
        for ing, cant in ingredientes_necesarios.items():
            if inventario.ingredientes.get(ing, 0) < cant:
                inventario.notificar_Faltante(ing)
                return False
        print(f"Stock validado correctamente para el pedido #{self.id}.")
        return True

class Inventario:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def reducirStock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            if self.ingredientes[ingrediente] >= cantidad:
                self.ingredientes[ingrediente] -= cantidad
                print(f"Se descontaron {cantidad} de '{ingrediente}'. Restan: {self.ingredientes[ingrediente]}.")
                return True
            else:
                self.notificar_Faltante(ingrediente)
                return False
        else:
            print(f" El ingrediente {ingrediente} no está registrado en el sistema.")
            return False

    def notificar_Faltante(self, ingrediente):
        print(f"No hay stock suficiente de {ingrediente}.")