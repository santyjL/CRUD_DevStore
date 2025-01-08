import flet as ft

from styles import Colores


def item_de_barra(label, icon):
    return ft.NavigationDrawerDestination(
        label=label,
        icon=ft.Icon(name=icon, color=Colores.BLANCO.value),
        selected_icon=True,
    )


def barra_de_navegación(page: ft.Page):
    # Contenedor dinámico para la barra anidada
    barra_anidada = ft.Column(visible=False)

    def handle_change(e):
        selected_label = e.control.controls[e.control.selected_index].label

        if selected_label == "Categorías":
            # Muestra la barra anidada
            barra_anidada.controls = [
                item_de_barra("Monitores y Laptops", "desktop_mac"),
                item_de_barra("Teléfonos", "phone_android"),
                item_de_barra("Accesorios", "headset"),
                item_de_barra("Cámaras", "photo_camera"),
            ]
            barra_anidada.visible = True
        else:
            # Oculta la barra anidada
            barra_anidada.visible = False

        # Redibuja la página
        page.update()

    # Barra principal
    barra_principal = ft.NavigationDrawer(
        controls=[
            item_de_barra("Inicio", "home"),
            item_de_barra("Buscar", "store"),
            item_de_barra("Categorías", "category"),
            item_de_barra("Acerca de", "info"),
        ],
        on_change=handle_change,
        bgcolor=Colores.AZUL.value,
    )

    # Contenedor principal con barra de navegación y barra anidada
    layout = ft.Column(
        controls=[
            barra_principal,
            barra_anidada,  # La barra anidada aparece aquí cuando se selecciona "Categorías"
        ]
    )

    return layout
