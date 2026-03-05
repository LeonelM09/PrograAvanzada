#módulo 1 (Personas)

class Persona:
    def __init__(self,idPersona, nombre, email, telefono):
        self.idPersona=idPersona 
        self.nombre=nombre
        self.email=email
        self.tel=telefono

    def login(self):
        print(f"Bienvenido: {self.nombre}")

    def logout(self):
        print(f"Hasta pronto: {self.nombre}...")

    def actualizar_datos(self, nom,email):
        self.nombre=nom
        self.email=email
        print(f"Datos actualizados")

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono, pts_fi):
        super().__init__(idPersona, nombre, email, telefono)

        self.pts=pts_fi
        self.historial_r=[]

    def crear_R(self,reserva):
        self.historial_r.append(reserva)
        print(f"Reserva #{reserva.idReserva} agregada al historial de {self.nombre}.")

    def consultar_P(self):
        print(f"{self.nombre}, tienes {self.pts} puntos de fidelidad disponibles.")

    def cancelar_R(self,reserva):
        reserva.estado = "CANCELADA"
        print(f"La reserva #{reserva.idReserva} ha sido cancelada exitosamente.")

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, telefono, id_emp, cargo, horario):
        super().__init__(idPersona, nombre, email, telefono)

        self.id_emp=id_emp
        self.cargo=cargo
        self.horario=horario

    def marcar_entrada(self):
        print(f"Entrada registrada: {self.nombre} (Turno {self.horario})")

    def gestionar_fun(self):
        if self.cargo=="ADMIN":
            print(f"Acceso concedido {self.nombre}")
            return True
        else:
            print(f"Acceso denegado")
            return False
        
    def agregar_pelicula(self, titulo, duracion, clasificacion, genero):
            if self.gestionar_fun():
             print(f"[SISTEMA]: El admin {self.nombre} agregó la película '{titulo}'.")
             return Pelicula(titulo, duracion, clasificacion, genero)
            else:
             return None
            
    def agregar_funcion(self, id_Fun, pelicula, sala, horario_Inicio, precio_Base):
        if self.gestionar_fun():
            print(f"[SISTEMA]: Función {id_Fun} creada exitosamente.")
            return Funcion(id_Fun, pelicula, sala, horario_Inicio, precio_Base)
            
    def agregar_promo(self, codigo, descripcion, porcentaje_desc, fecha_exp):
        if self.gestionar_fun():
            print(f"[SISTEMA]: Promoción '{codigo}' dada de alta.")
            return Promo(codigo, descripcion, porcentaje_desc, fecha_exp)

#módulo 2 (Infraestructra)

class Espacio:
    def __init__(self, id_Espacio,nombre,ubi):
        self.id_Espacio=id_Espacio
        self.nombre=nombre
        self.ubi=ubi

    def verif_disp(self, esta_disponible=True): 
        if esta_disponible:
            print(f"[INFO]: El espacio {self.nombre} ({self.ubi}) SÍ está disponible.")
            return True
        else:
            print(f"[AVISO]: El espacio {self.nombre} ({self.ubi}) NO está disponible.")
            return False

    def limpiar_estado(self):
        print(f"El espacio {self.nombre} ha sido limpiado y está listo para usarse.")
        
class Sala(Espacio):
    def __init__(self, id_Espacio, nombre, ubi, tipo, capacidad_T, EsVip):
        super().__init__(id_Espacio, nombre, ubi)
        self.tipo=tipo
        self.capacidad_T=capacidad_T
        self.EsVip=EsVip

    def ajustar_afo(self,nueva_capacidad):
        self.capacidad_T = nueva_capacidad
        print(f"[ACTUALIZACIÓN]: El aforo de {self.nombre} se ajustó a {self.capacidad_T} personas.")

    def obt_tip_sala(self):
        if self.EsVip:
            print(f"{self.nombre} es una sala tipo: {self.tipo} (VIP).")
        else:
            print(f"{self.nombre} es una sala tipo: {self.tipo} (Estándar).")
        return self.tipo

class ZonaComida(Espacio):
    def __init__(self, id_Espacio, nombre, ubi, stock):
        super().__init__(id_Espacio, nombre, ubi)
        self.stock=stock
        self.lista_P=[]

    def vender_Producto(self, nombre_producto, cantidad):
        print(f"Procesando venta de {cantidad}x {nombre_producto} en {self.nombre}...")
        self.actualizar_invt(nombre_producto, -cantidad)

    def actualizar_invt(self,nombre_producto, cantidad):
        if nombre_producto in self.stock:
            if (self.stock[nombre_producto] + cantidad) < 0:
                print(f"[ERROR]: No hay suficiente stock de {nombre_producto}.")
            else:
                self.stock[nombre_producto] += cantidad
                print(f"[OK]: El nuevo stock de {nombre_producto} es {self.stock[nombre_producto]}.")
        else:
            print(f"[AVISO]: El producto '{nombre_producto}' no se vende en esta zona.")

#módulo 3 (Lógica y funciones)

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion
        self.genero=genero

    def obt_sinop(self):
        mensaje = f"Sinopsis de {self.titulo}: Una emocionante historia de {self.genero} con {self.duracion} minutos de duración."
        print(mensaje)
        return mensaje

    def es_apta_todo_publi(self):
        if self.clasificacion == "A" or self.clasificacion == "AA":
            print(f"[INFO]: '{self.titulo}' (Clasificación {self.clasificacion}) SÍ es apta para todo público.")
            return True
        else:
            print(f"[INFO]: '{self.titulo}' (Clasificación {self.clasificacion}) requiere supervisión o es para adultos.")
            return False
        
class Funcion:
    def __init__(self, id_Fun, pelicula, sala, horario_Inicio, precio_Base):
        self.id_Fun=id_Fun
        self.pelicula=pelicula
        self.sala=sala
        self.horario_Inicio=horario_Inicio
        self.precio_Base=precio_Base
        self.asientos_ocupados = []

    def calc_asient_libres(self):
        libres = self.sala.capacidad_T - len(self.asientos_ocupados)
        return libres

    def obt_detall_func(self):
        print(f"\n--- DETALLES DE FUNCIÓN {self.id_Fun} ---")
        print(f"Película: {self.pelicula.titulo}")
        print(f"Sala: {self.sala.nombre} | Horario: {self.horario_Inicio}")
        print(f"Precio Base: ${self.precio_Base} | Asientos Libres: {self.calc_asient_libres()}")

    def verificar_y_ocupar_asientos(self, asientos_solicitados):
        if len(asientos_solicitados) > self.calc_asient_libres():
            print(f"[ERROR]: No hay suficientes asientos libres en la función {self.id_Fun}.")
            return False
        for asiento in asientos_solicitados:
            if asiento in self.asientos_ocupados:
                print(f"[RECHAZADO]: El asiento '{asiento}' ya está ocupado. Elige otro.")
                return False 
        self.asientos_ocupados.extend(asientos_solicitados)
        print(f"[ÉXITO]: Asientos {asientos_solicitados} apartados correctamente.")
        return True
    
#módulo 4 (gestión comercial)
 
class Promo:
    def __init__(self, codigo, descripcion, porcentaje_desc, fecha_exp):
        self.codigo=codigo
        self.descripcion=descripcion
        self.porcentaje_desc=porcentaje_desc
        self.fecha_exp=fecha_exp

    def esValida(self, usuario):
        print(f"Validando el código {self.codigo} para el cliente {usuario.nombre}...")
        print(f"[Aprobado]: La promoción {self.descripcion} es válida.")
        return True
    
    def aplicarDescuento(self, monto):
        descuento = monto * self.porcentaje_desc
        porcentaje_entero = int(self.porcentaje_desc * 100)
        print(f"Aplicando {porcentaje_entero}% de descuento. Se restarán ${descuento} del total.")
        return descuento 

class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos, montoTotal, estado):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = montoTotal
        self.estado = estado
        
        print(f"Reserva #{self.idReserva} creada con estado {self.estado}.")

    def confirmar_pago(self):
        self.estado = "PAGADA"
        print(f"El pago de la reserva #{self.idReserva} ha sido confirmado.")

    def generar_ticket(self):
        if self.estado == "PAGADA":
            print("\n--- TICKET DE ENTRADA ---")
            print(f"Cliente: {self.usuario.nombre}")
            print(f"Película: {self.funcion.pelicula.titulo}")
            print(f"Sala: {self.funcion.sala.nombre}")
            print(f"Asientos: {self.asientos}")
            print(f"Total Pagado: ${self.montoTotal}")
            print("-------------------------\n")
        else:
            print("[ERROR]: No se puede generar ticket de una reserva PENDIENTE o CANCELADA.")

    def aplicar_promo(self, promo):
        if promo.esValida(self.usuario):
            descuento = promo.aplicarDescuento(self.montoTotal)
            self.montoTotal = self.montoTotal - descuento
            
            print(f"¡ÉXITO! Promoción {promo.codigo} aplicada a la reserva #{self.idReserva}.")
            print(f"Nuevo total a pagar: ${self.montoTotal}")
            return descuento
        else:
            print("La promoción no es válida.")
            return 0