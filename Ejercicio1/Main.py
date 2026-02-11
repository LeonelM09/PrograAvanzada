from clases import*

cat_audio = Categoría("Audio")
cat_compu = Categoría("Computación")

prod1 = Producto("Audífonos Sony", 100.00, 10)
prod2 = Producto("Bocina JBL", 150.00, 5)
prod3 = Producto("MacBook Pro", 2500.00, 3)
prod4 = Producto("Mouse Logitech", 25.00, 20)

cat_audio.agregar_producto(prod1)
cat_audio.agregar_producto(prod2)
cat_compu.agregar_producto(prod3)
cat_compu.agregar_producto(prod4)

tienda = Tienda("TechStore")
tienda.registrar_categoria(cat_audio)
tienda.registrar_categoria(cat_compu)

pedido_carlos = Pedido("Carlos", [prod1, prod3])
tienda.pedidos_realizados.append(pedido_carlos) 


total_pedido = pedido_carlos.calcular_total()
print(f"Pedido de {pedido_carlos.cliente}: Total con IVA = ${total_pedido:,.2f}, Estado inicial: {pedido_carlos.estado}")
pedido_carlos.finalizar_pedido()
print(f"Estado tras finalizar: {pedido_carlos.estado}")

print("Reportes")

tienda.generar_reporte_ventas()
tienda.producto_mas_caro()
cat_audio.valor_total_categorias()