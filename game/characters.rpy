################################# Personajes ##################################

# Ralix - sprite y nombre a la IZQUIERDA
define ralix = Character(
    "{b}Ralix{b}",
    color="#000000",
    what_color="#000000",
    side_image = Transform("images/personajes/ralix.png", xzoom=0.4, yzoom=0.4),  # ajusta tamaño si es necesario
    side_images = { "left": "images/personajes/ralix.png" },
    namebox_xpos = 0.24,                          # nombre cerca del borde izquierdo
    namebox_ypos = 0.08,                         # arriba-izquierda
    what_xalign  = 0.45,                          # diálogo alineado a izquierda
    what_yalign  = 0.35                            # centrado vertical en el textbox
)

# Zuky/Mitzuky - sprite y nombre a la DERECHA
define zuky = Character(  # o zuky si lo llamas así
    "{b}Zuky{b}",
    color="#7e8891",
    what_color="#7e8891",
    side_image = Transform("images/personajes/zuky.png", xzoom=0.4, yzoom=0.4),
    side_images = { "right": "images/personajes/zuky.png" },
    namebox_xpos=0.69,                         # nombre cerca del borde derecho
    namebox_ypos=0.08,                         # arriba-derecha
    what_xalign=0.64,                          # diálogo alineado a derecha
    what_yalign=0.35                            # centrado vertical
)

# Personajes genéricos (sin sprite lateral)
define narrator = Character(None, what_xalign=0.5)  # centrado para narración