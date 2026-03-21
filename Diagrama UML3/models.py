import datetime
#   1. MÓDULO DE MATERIALES (HERENCIA)

class Material:
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible=True):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            print(f"El material: {self.titulo} no está disponible.")
            return False

    def devolver(self):
        self.disponible = True
        print(f"'{self.titulo} ha sido devuelto y está disponible.")

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, autor, isbn, genero, disponible=True):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, edicion, periodicidad, disponible=True):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, tipoArchivo, urlDescarga, tamañoMB, disponible=True):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = float(tamañoMB)

#   2. MÓDULO DE USUARIOS Y SEDES

class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, limitePrestamos=3):
        super().__init__(idPersona, nombre, email)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []
        self.bloqueado = False  

    def puede_pedir(self):
        if self.bloqueado:
            print(f"{self.nombre} está bloqueado por adeudos.")
            return False
        if len(self.listaActiva) < self.limitePrestamos:
            return True
        else:
            print(f"{self.nombre} alcanzó su límite de préstamos.")
            return False

class Sucursal:
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

    def agregar_material(self, material):
        self.catalogoLocal.append(material)

    def quitar_material(self, material):
        if material in self.catalogoLocal:
            self.catalogoLocal.remove(material)
            return True
        return False

class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre, email, sucursal_asignada=None):
        super().__init__(idPersona, nombre, email)
        self.sucursal_asignada = sucursal_asignada

    def gestionarPrestamo(self, usuario, material, fecha_inicio, fecha_fin):
        if usuario.puede_pedir() and material.disponible:
            material.prestar()
            nuevo_prestamo = Prestamo(len(usuario.listaActiva) + 1, fecha_inicio, fecha_fin, usuario, material)
            usuario.listaActiva.append(nuevo_prestamo)
            print(f"[BIBLIOTECARIO {self.nombre}]: Préstamo exitoso de '{material.titulo}' a {usuario.nombre}.")
            return nuevo_prestamo
        else:
            print(f"[BIBLIOTECARIO {self.nombre}]: No se pudo concretar el préstamo.")
            return None

    def transferirMaterial(self, material, sucursalDestino):
        if self.sucursal_asignada and self.sucursal_asignada.quitar_material(material):
            sucursalDestino.agregar_material(material)
            print(f"{material.titulo} transferido a la sucursal {sucursalDestino.nombre}.")
        else:
            print(f"El material no se encuentra en la sucursal actual.")

#   3. GESTIÓN DE PRÉSTAMOS Y PENALIZACIONES

class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto, motivo, usuario):
        self.monto = float(monto)
        self.motivo = motivo
        self.pagada = False
        self.usuario = usuario

    def calcularMulta(self, dias_retraso):
        if dias_retraso > 0:
            self.monto = float(dias_retraso * 15.0)
            print(f"[Multa calculada. Total a pagar: ${self.monto}")
        return self.monto

    def bloquearUsuario(self):
        self.usuario.bloqueado = True
        print(f"El usuario: {self.usuario.nombre} ha sido bloqueado. Motivo: {self.motivo}.")

class Catalogo:
    def __init__(self, lista_sucursales):
        self.lista_sucursales = lista_sucursales

    def buscarPorAutor(self, autor):
        print(f"\n--- Búsqueda global por autor: '{autor}' ---")
        encontrados = False
        for sucursal in self.lista_sucursales:
            for material in sucursal.catalogoLocal:
                if type(material).__name__ == 'Libro' and material.autor.lower() == autor.lower():
                    print(f"Encontrado: '{material.titulo}' en {sucursal.nombre}")
                    encontrados = True
        if not encontrados:
            print("No se encontraron resultados.")

    def buscarEnTodasSucursales(self, titulo):
        print(f"\n--- Búsqueda global por título: '{titulo}' ---")
        encontrados = False
        for sucursal in self.lista_sucursales:
            for material in sucursal.catalogoLocal:
                if material.titulo.lower() == titulo.lower():
                    print(f"Encontrado: '{material.titulo}' en {sucursal.nombre}")
                    encontrados = True
        if not encontrados:
            print("No se encontraron resultados.")
