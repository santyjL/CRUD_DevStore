import flet as ft

from styles import Colores


def item_de_barra(label, icon):
    return ft.NavigationDrawerDestination(
        label=label,
        icon=ft.Icon(name=icon, color=Colores.BLANCO.value),
        selected_icon=True,
    )

def barra_de_navegación(page: ft.Page):
    def handle_dismissal(e):
        page.add(ft.text("Drawer dismissed"))

    def handle_change(e):
        page.add(ft.text(f"Selected Index changed: {e.control.selected_index}"))
        # page.close(drawer)

    Barra = ft.NavigationDrawer(
        controls=[
            item_de_barra("Inicio", "home"),
            item_de_barra("Buscar", "store"),
            item_de_barra("Contacto", "contact_support"),
            item_de_barra("Acerca de", "info"),
        ],
        bgcolor=Colores.AZUL.value,
    )
    return Barra