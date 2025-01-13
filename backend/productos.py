from backend.crear_productos import Creador_de_productos
from styles import Colores

# Categoría: Desarrollo
libro_python = Creador_de_productos(
    nombre="Python Crash Course",
    imagen="https://via.placeholder.com/150",
    descripcion="Un libro completo para principiantes en Python.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

arduino_kit = Creador_de_productos(
    nombre="Kit Arduino Uno",
    imagen="https://via.placeholder.com/150",
    descripcion="Incluye una placa Arduino Uno y componentes esenciales.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Monitores y Laptops
monitor_gaming = Creador_de_productos(
    nombre="Monitor ASUS TUF Gaming",
    imagen="https://via.placeholder.com/150",
    descripcion="Monitor Full HD de 27 pulgadas con 165 Hz.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

laptop_dell = Creador_de_productos(
    nombre="Dell XPS 13",
    imagen="https://via.placeholder.com/150",
    descripcion="Laptop ultrafina con pantalla InfinityEdge.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Teclados
teclado_mecanico = Creador_de_productos(
    nombre="Logitech G Pro X",
    imagen="https://via.placeholder.com/150",
    descripcion="Teclado mecánico personalizable para gamers.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

teclado_ergonomico = Creador_de_productos(
    nombre="Microsoft Ergonomic Keyboard",
    imagen="https://via.placeholder.com/150",
    descripcion="Teclado ergonómico diseñado para largas jornadas de trabajo.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Auriculares
auriculares_inalambricos = Creador_de_productos(
    nombre="Sony WH-1000XM5",
    imagen="https://via.placeholder.com/150",
    descripcion="Auriculares con cancelación de ruido líder en la industria.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

headset_gaming = Creador_de_productos(
    nombre="HyperX Cloud II",
    imagen="https://via.placeholder.com/150",
    descripcion="Auriculares para gamers con sonido envolvente 7.1.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Ratones
raton_gaming = Creador_de_productos(
    nombre="Razer DeathAdder V2",
    imagen="https://via.placeholder.com/150",
    descripcion="Ratón ergonómico para juegos con sensor óptico avanzado.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

raton_inalambrico = Creador_de_productos(
    nombre="Logitech MX Master 3",
    imagen="https://via.placeholder.com/150",
    descripcion="Ratón inalámbrico avanzado para productividad.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

# Categoría: Cámaras
camara_web = Creador_de_productos(
    nombre="Logitech C920",
    imagen="https://via.placeholder.com/150",
    descripcion="Cámara web Full HD ideal para videollamadas.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

camara_deportiva = Creador_de_productos(
    nombre="GoPro HERO11",
    imagen="https://via.placeholder.com/150",
    descripcion="Cámara deportiva de última generación con estabilización avanzada.",
    color=Colores.BLANCO.value,
    width="full",
    height=200,
    expand=1
)

productos_varios = [
    libro_python, arduino_kit,
    monitor_gaming, laptop_dell,
    teclado_mecanico, teclado_ergonomico,
    auriculares_inalambricos, headset_gaming,
    raton_gaming, raton_inalambrico,
    camara_web, camara_deportiva
]
