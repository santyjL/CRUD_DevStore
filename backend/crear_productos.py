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
    categoria: str = None

    def elementos_retorno(self):
        return (self.nombre, self.imagen,
                self.descripcion, self.color,
                self.width, self.height, self.expand,
                self.color_texto, self.categoria)

@dataclass
class modificador_de_productos:
    producto_base: Creador_de_productos

    def igualar_parametros(self, lista_de_productos: list[Creador_de_productos]):
        todos_los_productos: list = []

        (nombre, imagen, descripcion, color,
         width, height, expand, color_texto, categoria) = self.producto_base.elementos_retorno()

        for producto in lista_de_productos:
            if isinstance(producto, Creador_de_productos):
                nuevo_producto = Creador_de_productos(
                    nombre=producto.nombre,
                    imagen=producto.imagen,
                    descripcion=producto.descripcion,
                    color=color,
                    width=width,
                    height=height,
                    expand=expand,
                    color_texto=color_texto,
                    categoria=producto.categoria
                )
                todos_los_productos.append(nuevo_producto)
            else:
                print(f"Advertencia: {producto} no es una instancia de Creador_de_productos")

        return todos_los_productos

def ajustar_productos(producto_base: Creador_de_productos,
                      lista_de_productos: list[Creador_de_productos]) -> list[Creador_de_productos]:
    modificador = modificador_de_productos(producto_base)
    todos_los_productos: list[Creador_de_productos] = modificador.igualar_parametros(lista_de_productos)
    return todos_los_productos
