from backend.crear_productos import Creador_de_productos
from styles import Colores

# Categoría: Desarrollo
libro_python = Creador_de_productos(
    nombre="Python Crash Course",
    imagen="asset/Python Crash Course.jpg",
    descripcion="Un libro completo para principiantes en Python.",
    color=Colores.AZUL.value,
    width="full",
    height=300,
    expand=1,
    color_texto=Colores.BLANCO.value
)

arduino_kit = Creador_de_productos(
    nombre="Kit Arduino Uno",
    imagen="asset/Kit Arduino Uno.jpg",
    descripcion="Incluye una placa Arduino Uno y componentes esenciales.",
    color=Colores.AZUL.value,
    width="full",
    height=300,
    expand=1,
    color_texto=Colores.BLANCO.value
)

# Categoría: Monitores y Laptops
monitor_gaming = Creador_de_productos(
    nombre="Monitor ASUS TUF Gaming",
    imagen="asset/Monitor ASUS TUF Gaming.jpg",
    descripcion="Monitor Full HD de 27 pulgadas con 165 Hz.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Teclados
teclado_mecanico = Creador_de_productos(
    nombre="Logitech G Pro X",
    imagen="asset/Logitech G Pro X.jpg",
    descripcion="Teclado mecánico personalizable para gamers.",
    color=Colores.AZUL.value,
    width="full",
    height=300,
    expand=1,
    color_texto=Colores.BLANCO.value
)

teclado_ergonomico = Creador_de_productos(
    nombre="Microsoft Ergonomic Keyboard",
    imagen="asset/Microsoft Ergonomic Keyboard.jpg",
    descripcion="Teclado ergonómico diseñado para largas jornadas de trabajo.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Auriculares
auriculares_inalambricos = Creador_de_productos(
    nombre="Sony WH-1000XM5",
    imagen="asset/Sony WH-1000XM5.jpg",
    descripcion="Auriculares con cancelación de ruido líder en la industria.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

headset_gaming = Creador_de_productos(
    nombre="HyperX Cloud II",
    imagen="asset/HyperX Cloud II.jpg",
    descripcion="Auriculares para gamers con sonido envolvente 7.1.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Ratones
raton_gaming = Creador_de_productos(
    nombre="Razer DeathAdder V2",
    imagen="asset/Razer DeathAdder V2.jpg",
    descripcion="Ratón ergonómico para juegos con sensor óptico avanzado.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

raton_inalambrico = Creador_de_productos(
    nombre="Logitech MX Master 3",
    imagen="asset/Logitech MX Master 3.jpg",
    descripcion="Ratón inalámbrico avanzado para productividad.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Cámaras
camara_web = Creador_de_productos(
    nombre="Logitech C920",
    imagen="asset/Logitech C920.jpg",
    descripcion="Cámara web Full HD ideal para videollamadas.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

camara_deportiva = Creador_de_productos(
    nombre="GoPro HERO11",
    imagen="asset/GoPro HERO11.jpg",
    descripcion="Cámara deportiva de última generación con estabilización avanzada.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

productos_varios = [

    monitor_gaming,
    teclado_ergonomico,
    auriculares_inalambricos, headset_gaming,
    raton_gaming, raton_inalambrico,
    camara_web, camara_deportiva
]

productos_destacado = [libro_python, teclado_mecanico, arduino_kit,]