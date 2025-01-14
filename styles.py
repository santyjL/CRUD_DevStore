from enum import Enum

import flet as ft


class Colores (Enum):
    BLANCO = "#FFFFFF"
    AZUL = "#1C5F88"
    ROJO = "#D1171A"
    GRIS = "#989F9C"
    NEGRO = "#000000"

class Estilos (Enum):
    Margin = 10
    BORDER_RADIUS_1 = ft.border_radius.all(75)
    BORDER_RADIUS_2 = ft.border_radius.only(75 , 75 , 50 , 150),