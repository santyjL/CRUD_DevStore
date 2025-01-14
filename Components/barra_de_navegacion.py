import flet as ft

from styles import Colores

BGFONDO = Colores.AZUL.value

def barra_comprimida(barra_completa: ft.NavigationDrawer):
    def abrir_barra(e):
        barra_completa.open = True
        barra_completa.update()

    barra = ft.Container(
        ft.Row(
        controls=[
            ft.IconButton(icon="menu",
                          on_click=abrir_barra,
                          icon_color=Colores.BLANCO.value
                    ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alineación al inicio
        ),
        expand=True,  # ¡Asegúrate de que este contenedor se expanda!
        width="full",
        bgcolor=BGFONDO,
        margin=0
    )
    return barra

def item_de_barra(label, icon):
    return ft.ListTile(
        title=ft.Text(label),
        leading=ft.Icon(icon),
        icon_color=Colores.BLANCO.value,
        text_color=Colores.BLANCO.value,
        bgcolor=BGFONDO,
        on_click=lambda e: print(f"{label} clicked")
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
            item_de_barra("Inicio", "home"),
            item_de_barra("Buscar", "store"),
            item_de_barra("Carrito", "shopping_cart"),
            categoria,
            item_de_barra("vender", "shopping_bag_rounded"),
        ],
        bgcolor=BGFONDO,
    )

    return barra_principal