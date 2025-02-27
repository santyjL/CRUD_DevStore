import flet as ft

from backend.crear_productos import Creador_de_productos
from backend.productos import categorias
from Components.barra_comprimida import barra_comprimida
from styles import Colores


def abrir_modal_agregar_producto(page: ft.Page):
    # Definir campos del formulario
    nombre_input = ft.TextField(label="Nombre", width=300)
    imagen_input = ft.TextField(label="URL de la imagen", width=300)
    descripcion_input = ft.TextField(label="Descripción", width=300)
    categoria_input = ft.Dropdown(options=[ft.dropdown.Option(f"{i}") for i in categorias],
                                  label="Categoría",
                                  width=300,)
    precio_input = ft.TextField(label="Precio", width=300)

    def submit(e):
        # Aquí se procesarían los datos ingresados
        print("Producto a agregar:")
        print("Nombre:", nombre_input.value)
        print("Imagen:", imagen_input.value)
        print("Descripción:", descripcion_input.value)
        print("Categoría:", categoria_input.value)
        print("Precio:", precio_input.value)

        # nuevo_producto = Creador_de_productos(
        #     nombre=nombre_input.value,
        #     imagen=imagen_input.value,
        #     descripcion=descripcion_input.value,
        #     categoria=categoria_input.value,
        #     precio=precio_input.value
        # )
        dialog.open = False
        page.update()

    dialog_content = ft.Column(
        controls=[
            ft.Text("Añadir Nuevo Producto", weight=ft.FontWeight.BOLD, size=20),
            nombre_input,
            imagen_input,
            descripcion_input,
            categoria_input,
            precio_input,
            ft.Row(
                controls=[
                    ft.ElevatedButton("Agregar", on_click=submit),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: close_dialog())
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ],
        spacing=10
    )

    def close_dialog():
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        title=ft.Text("Nuevo Producto"),
        content=dialog_content,
        actions_alignment=ft.MainAxisAlignment.END,
        actions=[ft.TextButton("Cerrar", on_click=lambda e: close_dialog())]
    )
    page.dialog = dialog
    dialog.open = True
    page.update()

def vender_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Botón para abrir el modal de agregar producto
    btn_agregar = ft.ElevatedButton(
        "Agregar Producto",
        on_click=lambda e: abrir_modal_agregar_producto(page)
    )

    page.controls.append(barra_comprimida(page.drawer))
    # Mostrar el botón en la pantalla de vender
    page.controls.append(
        ft.Column(
            controls=[
                btn_agregar,
                ft.Container(
                    content=ft.Text("Formulario de venta de productos", size=18),
                    alignment=ft.alignment.center,
                    padding=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
