import flet as ft

from styles import Colores


def barra_de_navegación(page: ft.Page):
    def handle_dismissal(e):
        page.add(ft.text("Drawer dismissed"))

    def handle_change(e):
        page.add(ft.text(f"Selected Index changed: {e.control.selected_index}"))
        # page.close(drawer)

    Barra = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                label="Inicio",
                icon=ft.Icon(name=ft.Icons.HOME, color=Colores.BLANCO.value),
                selected_icon=True,
            ),
            ft.NavigationDrawerDestination(
                label="Buscar",
                icon="store",
            ),
            ft.NavigationDrawerDestination(
                label="Contacto",
                icon="contact_support",
            ),
            ft.NavigationDrawerDestination(
                label="Acerca de",
                icon="info",
            )
        ],

    )
    return Barra