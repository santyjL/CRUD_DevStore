from enum import Enum


class Router(Enum):
    INICIO = "/"
    BUSQUEDA = "/Busqueda"
    CARRITO = "/Carrito"
    PRODUCTO = "/producto"
    VENDER = "/Vender"