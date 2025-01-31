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

@dataclass
class modificador_de_productos:
    producto_base : Creador_de_productos

    def igualar_parametros(self, lista_de_productos:list[Creador_de_productos]):

        todos_los_productos:list = []

        (nombre,imagen,descripcion,color,
        width,height,expand,color_texto) = self.producto_base.elementos_retorno()

        for producto in lista_de_productos:
            if isinstance(producto, Creador_de_productos):
                producto.color = color
                producto.width = width
                producto.height = height
                producto.expand = expand
                producto.color_texto = color_texto

                todos_los_productos.append(producto)
            else:
                print(f"Advertencia: {producto} no es una instancia de Creador_de_productos")

        return todos_los_productos

def ajustar_productos(producto_base: Creador_de_productos, lista_de_productos: list[Creador_de_productos]):
    productos_ajustados = []

    modificador = modificador_de_productos(producto_base)
    todos_los_productos = modificador.igualar_parametros(lista_de_productos)

    for elemento1, elemento2 in zip(lista_de_productos, todos_los_productos):
        # elemento1 y elemento2 son del tipo Creador_de_productos
        elemento1.color = elemento2.color
        elemento1.width = elemento2.width
        elemento1.height = elemento2.height
        elemento1.expand = elemento2.expand
        elemento1.color_texto = elemento2.color_texto
        productos_ajustados.append(elemento1)

    return productos_ajustados
