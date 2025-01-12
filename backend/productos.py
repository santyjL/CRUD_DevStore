from backend.crear_productos import Creador_de_productos
from styles import Colores

teclado = Creador_de_productos(
    nombre="Teclado",
    imagen="https://via.placeholder.com/150",
    descripcion="Descripción del producto",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

raton = Creador_de_productos(
    nombre="Ratón",
    imagen="https://via.placeholder.com/150",
    descripcion="Descripción del producto",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

productos_varios = [teclado , raton]