import flet as ft


def main(page: ft.Page):
    # Primera fila con fondo rojo
    first_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    width=80,
                    height=80,
                    bgcolor="gray",
                    border=ft.border.all(1, "black"),
                    alignment=ft.alignment.center
                ) for _ in range(5)
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        bgcolor="red",
        padding=10,
        height=150
    )

    # Segunda fila con dos columnas azules
    second_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Container(
                    width=150,
                    height=150,
                    bgcolor="blue",
                    alignment=ft.alignment.center
                ),
                bgcolor="blue",
                width=200,
                height=200,
                alignment=ft.alignment.center
            ) for _ in range(2)
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Tercera fila con un carrusel
    third_row = ft.Row(
        controls=[
            ft.Container(
                width=100,
                height=100,
                bgcolor="lightgray",
                alignment=ft.alignment.center,
                border=ft.border.all(1, "black")
            ) for _ in range(4)
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    # Agregar todo al layout principal
    page.add(
        first_row,
        ft.Container(height=10),  # Espaciado
        second_row,
        ft.Container(height=10),  # Espaciado
        third_row
    )

ft.app(target=main)
