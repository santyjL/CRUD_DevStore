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