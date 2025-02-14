from frontend.buscador import buscador_view
from frontend.carrito import carrito_view
from frontend.inicio import inicio_view
from frontend.productos import productos_view
from frontend.vender import vender_view
from routers.routers import Router


def route_change(e):
    page = e.page
    page.controls.clear()  # Limpia los controles de la pantalla actual
    if page.route == Router.INICIO.value:
        inicio_view(page)  # Carga la vista de inicio
    elif page.route == Router.BUSQUEDA.value:
        buscador_view(page)  # Carga la vista del buscador
    elif Router.PRODUCTO.value in page.route:
        productos_view(page)
    elif page.route == Router.CARRITO.value:
        carrito_view(page)
    elif page.route == Router.VENDER.value:
        vender_view(page)
    page.update()  # Actualiza la pantalla
