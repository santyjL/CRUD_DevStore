from dataclasses import dataclass

from styles import Colores


@dataclass
class Creador_de_productos:
    """
    Clase que define un contenedor de productos.
    """
    nombre: str
    imagen: str
    descripcion: str
    color: str
    width: str
    height: int
    expand: int
    color_texto: str = Colores.NEGRO.value

    def elementos_retorno(self):
        return (self.nombre, self.imagen,
                self.descripcion, self.color,
                self.width, self.height, self.expand,
                self.color_texto)
