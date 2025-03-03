import flet as ft

from backend.crear_productos import Creador_de_productos
from backend.productos import categorias, productos_totales
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
    # Añadimos un campo de error visual para el precio
    precio_input.error_text = ""

    def submit(e):
        try:
            # Convertir a float para validar el número
            precio_valido = float(precio_input.value)
            precio_input.error_text = ""  # Limpiar error si es válido
        except ValueError:
            precio_input.error_text = "Precio debe ser un número."  # Mostrar mensaje de error
            page.update()
            return

        nuevo_producto = Creador_de_productos(
            nombre=nombre_input.value,
            imagen=imagen_input.value,
            descripcion=descripcion_input.value,
            color=Colores.BLANCO.value,
            width="full",
            height=200,
            expand=1,
            categoria=categoria_input.value,
            marca="",
            precio=precio_valido,
            id= len(productos_totales) + 2
        )
        productos_totales.append(nuevo_producto)
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