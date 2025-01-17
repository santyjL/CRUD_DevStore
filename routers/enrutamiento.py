from frontend.buscador import buscador_view
from frontend.inicio import inicio_view
from routers.routers import Router


def route_change(e):
    page = e.page
    page.controls.clear()  # Limpia los controles de la pantalla actual
    if page.route == Router.INICIO.value:
        inicio_view(page)  # Carga la vista de inicio
    elif page.route == Router.BUSQUEDA.value:
        buscador_view(page)  # Carga la vista del buscador
    page.update()  # Actualiza la pantalla
