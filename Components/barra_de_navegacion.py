import flet as ft

from styles import Colores


def barra_de_navegación(page: ft.Page):
    def handle_dismissal(e):
        page.add(ft.Text("Drawer dismissed"))

    def handle_change(e):
        page.add(ft.Text(f"Selected Index changed: {e.control.selected_index}"))
        # page.close(drawer)

    Barra = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerItem(
                text="Inicio",
                icon="home",
                selected=True,
                on_click=handle_dismissal
            ),
            ft.NavigationDrawerItem(
                text="Productos",
                icon="store",
                on_click=handle_dismissal
            ),
            ft.NavigationDrawerItem(
                text="Contacto",
                icon="contact_support",
                on_click=handle_dismissal
            ),
            ft.NavigationDrawerItem(
                text="Acerca de",
                icon="info",
                on_click=handle_dismissal
            )
        ],
        on_change=handle_change
    )