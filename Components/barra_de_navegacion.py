import flet as ft

from routers.routers import Router
from styles import Colores

BGFONDO = Colores.AZUL.value

def item_de_barra(label, icon, page: ft.Page = None, router="/"):
    def clikeo(e):
        page.go(router)
        return True

    return ft.ListTile(
        title=ft.Text(label),
        leading=ft.Icon(icon),
        icon_color=Colores.BLANCO.value,
        text_color=Colores.BLANCO.value,
        bgcolor=BGFONDO,
        url_target=router,
        on_click=clikeo  # Cambiar la ruta
    )

def barra_de_navegacion(page: ft.Page):
    def on_categoria_change(e):
        print(f"Selected: {e.control.value}")
        page.client_storage.set("categoria_seleccionada", e.control.value)
        return e.control.value

    categoria = ft.Dropdown(
        options=[
            ft.dropdown.Option("Monitores y Laptops"),
            ft.dropdown.Option("Desarrollo"),
            ft.dropdown.Option("Cámaras"),
            ft.dropdown.Option("Teclados"),
            ft.dropdown.Option("Ratones"),
            ft.dropdown.Option("Auriculares"),
            ft.dropdown.Option("Todo"),
        ],
        bgcolor=BGFONDO,
        on_change=on_categoria_change
    )

    categoria.label = "Categorias"
    categoria.value = "Todo"
    barra_principal = ft.NavigationDrawer(
        controls=[
            item_de_barra("Inicio", "home", page, Router.INICIO.value),
            item_de_barra("Buscar", "store", page, Router.BUSQUEDA.value),
            item_de_barra("Carrito", "shopping_cart", page, Router.CARRITO.value),
            categoria,
            item_de_barra("Vender", "shopping_bag_rounded"),
        ],
        bgcolor=BGFONDO,
    )

    return barra_principal