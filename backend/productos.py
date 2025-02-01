from backend.crear_productos import Creador_de_productos, ajustar_productos
from styles import Colores

# Productos bases
producto_nuevo = Creador_de_productos(
    nombre="",
    imagen="",
    descripcion="",
    color=Colores.ROJO.value,
    width="full",
    height=600,
    expand=1,
    color_texto=Colores.BLANCO.value
)

producto_destacado = Creador_de_productos(
    nombre="",
    imagen="",
    descripcion="",
    color=Colores.AZUL.value,
    width="full",
    height=300,
    expand=1,
    color_texto=Colores.BLANCO.value
)

producto_normal = Creador_de_productos(
    nombre="",
    imagen="",
    descripcion="",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Desarrollo
libro_python = Creador_de_productos(
    nombre="Python Crash Course",
    imagen="asset/Python Crash Course.jpg",
    descripcion="Un libro completo para principiantes en Python.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

arduino_kit = Creador_de_productos(
    nombre="Kit Arduino Uno",
    imagen="asset/Kit Arduino Uno.jpg",
    descripcion="Incluye una placa Arduino Uno y componentes esenciales.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

# Categoría: Monitores y Laptops
monitor_gaming = Creador_de_productos(
    nombre="Monitor ASUS TUF Gaming",
    imagen="asset/Monitor ASUS TUF Gaming.jpg",
    descripcion="Monitor Full HD de 27 pulgadas con 165 Hz.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

# Categoría: Teclados
teclado_mecanico = Creador_de_productos(
    nombre="Logitech G Pro X",
    imagen="asset/Logitech G Pro X.jpg",
    descripcion="Teclado mecánico personalizable para gamers.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

teclado_ergonomico = Creador_de_productos(
    nombre="Microsoft Ergonomic Keyboard",
    imagen="asset/Microsoft Ergonomic Keyboard.jpg",
    descripcion="Teclado ergonómico diseñado para largas jornadas de trabajo.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

# Categoría: Auriculares
auriculares_inalambricos = Creador_de_productos(
    nombre="Sony WH-1000XM5",
    imagen="asset/Sony WH-1000XM5.jpg",
    descripcion="Auriculares con cancelación de ruido líder en la industria.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

headset_gaming = Creador_de_productos(
    nombre="HyperX Cloud II",
    imagen="asset/HyperX Cloud II.jpg",
    descripcion="Auriculares para gamers con sonido envolvente 7.1.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

# Categoría: Ratones
raton_gaming = Creador_de_productos(
    nombre="Razer DeathAdder V2",
    imagen="asset/Razer DeathAdder V2.jpg",
    descripcion="Ratón ergonómico para juegos con sensor óptico avanzado.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

raton_inalambrico = Creador_de_productos(
    nombre="Logitech MX Master 3",
    imagen="asset/Logitech MX Master 3.jpg",
    descripcion="Ratón inalámbrico avanzado para productividad.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

# Categoría: Cámaras
camara_web = Creador_de_productos(
    nombre="Logitech C920",
    imagen="asset/Logitech C920.jpg",
    descripcion="Cámara web Full HD ideal para videollamadas.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

camara_deportiva = Creador_de_productos(
    nombre="GoPro HERO11",
    imagen="asset/GoPro HERO11.jpg",
    descripcion="Cámara deportiva de última generación con estabilización avanzada.",
    color=None,
    width=None,
    height=None,
    expand=None,
    color_texto=None
)

pato_de_goma = Creador_de_productos(
    nombre="Super pato de Goma",
    imagen="asset/Super Pato de Goma.jpg",
    descripcion="El pato de goma que siempre te salvara.",
    color=Colores.ROJO.value,
    width="full",
    height=600,
    expand=1,
    color_texto=Colores.BLANCO.value
)

productos_varios_lista: list[Creador_de_productos] = [
    monitor_gaming,
    teclado_ergonomico,
    auriculares_inalambricos, headset_gaming,
    raton_gaming, raton_inalambrico,
    camara_web, camara_deportiva
]

productos_destacado_lista: list[Creador_de_productos] = [libro_python, teclado_mecanico, arduino_kit]
productos_totales: list[Creador_de_productos] = productos_destacado_lista + productos_varios_lista + [pato_de_goma]

def productos_buscador():
    todos_los_productos = ajustar_productos(producto_normal, productos_totales)
    return todos_los_productos

def productos_inicio():
    productos_varios = ajustar_productos(producto_normal, productos_varios_lista)
    productos_destacado = ajustar_productos(producto_destacado, productos_destacado_lista)
    Productos_nuevos = ajustar_productos(producto_nuevo, [pato_de_goma])

    return Productos_nuevos, productos_destacado, productos_varios

