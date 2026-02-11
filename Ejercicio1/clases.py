class Producto:
    def __init__ (self,nombre,precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock


    def aplicar_descuento(self, porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"El nuevo precio del producto {self.nombre} es {self.precio_base}")


    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("No hay suficiente stock")
        else:
            self.stock+=cantidad
            print(f"El nuevo stock de {self.nombre} es {self.stock}")


class Categoría:
    def __init__(self, nombre_categoria):
        self.nombre_categoria=nombre_categoria
        self.lista_de_productos=[]


    def agregar_producto(self,producto):
        self.lista_de_productos.append(producto)
        print(f"El producto {producto.nombre} se agregar a la lista")


    def valor_total_categorias(self):
        suma=0
        for m in self.lista_de_productos:
            suma+= m.precio_base*m.stock
        print(f"El precio total de la categoria {self.nombre_categoria} es {suma}")

class Pedido:
    def __init__(self, cliente, productos_comprados):
        self.cliente = cliente
        self.productos_comprados = productos_comprados  
        self.estado = "Pendiente"

    def calcular_total(self):
        subtotal = sum(p.precio_base for p in self.productos_comprados)
        total_con_iva = subtotal * 1.16  
        return total_con_iva

    def finalizar_pedido(self):
        self.estado = "Completado"
        for producto in self.productos_comprados:
            producto.actualizar_stock(-1)  


class Tienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.categorias = []
        self.pedidos_realizados = []

    def registrar_categoria(self, categoria):
        self.categorias.append(categoria)

    def generar_reporte_ventas(self):
        total_ingresos = 0
        for pedido in self.pedidos_realizados:
            if pedido.estado == "Completado":
                total_ingresos += pedido.calcular_total()
        print(f"Reporte {self.nombre_tienda}: Total de ingresos por pedidos completados = ${total_ingresos:,.2f}")

    def producto_mas_caro(self):
        precio_maximo = 0
        producto_caro = None
        
        for categoria in self.categorias:
            for producto in categoria.lista_de_productos:
                if producto.precio_base > precio_maximo:
                    precio_maximo = producto.precio_base
                    producto_caro = producto
                    
        if producto_caro:
            print(f"El producto más caro en inventario es: {producto_caro.nombre} (${producto_caro.precio_base:,.2f})")