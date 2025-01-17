import flet as ft

from routers.enrutamiento import route_change
from routers.routers import Router
from styles import Colores

BGFONDO = Colores.AZUL.value



def item_de_barra(label, icon,page:ft.Page=None, router = "/"):
    def clikeo(e):
        page.on_route_change = route_change
        page.go(router)

        return True


    return ft.ListTile(
        title=ft.Text(label),
        leading=ft.Icon(icon),
        icon_color=Colores.BLANCO.value,
        text_color=Colores.BLANCO.value,
        bgcolor=BGFONDO,
        url_target=router,
        on_click=clikeo   # Cambiar la ruta
        )

def barra_de_navegacion(page: ft.Page):
    categoria = ft.Dropdown(
                options=[
                    ft.dropdown.Option("Monitores y Laptops"),
                    ft.dropdown.Option("Teléfonos"),
                    ft.dropdown.Option("Accesorios"),
                    ft.dropdown.Option("Cámaras"),
                ],
                bgcolor=BGFONDO,
                on_change=lambda e: print(f"Selected: {e.control.value}")
            )

    categoria.label = "Categorias"
    barra_principal = ft.NavigationDrawer(
        controls=[
            item_de_barra("Inicio", "home", page,Router.BUSQUEDA.value),
            item_de_barra("Buscar", "store",page, Router.BUSQUEDA.value),
            item_de_barra("Carrito", "shopping_cart"),
            categoria,
            item_de_barra("vender", "shopping_bag_rounded"),
        ],
        bgcolor=BGFONDO,
    )

    return barra_principal