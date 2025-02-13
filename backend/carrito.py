import flet as ft

from backend.crear_productos import Creador_de_productos, ajustar_productos
from backend.productos import productos_totales
from styles import Colores

producto_carrito_base = Creador_de_productos(
    nombre="",
    imagen="",
    descripcion="",
    color=Colores.ROJO.value,
    width="full",
    height=300,
    expand=1,
    color_texto=Colores.BLANCO.value,
    categoria="",
    marca="",
    precio=0.99,
    id=None
)

productos_carrito:list[Creador_de_productos] = []

def productos_del_carrito():
    productos = ajustar_productos(producto_carrito_base,productos_carrito)

    return productos

def agregar_producto_carrito(id_producto:int,page:ft.Page):
    for producto in productos_totales:
        if producto.id == id_producto:
            productos_carrito.append(producto)
            page.update()
            break


