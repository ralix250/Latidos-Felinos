########################### Personajes Principales ############################

# Ralix - sprite y nombre a la IZQUIERDA
define ralix = Character(
    "{b}Ralix{b}",
    color        = "#000000",
    what_color   = "#000000",
    side_image   = "Ralix base",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

# Zuky - sprite y nombre a la DERECHA
define zuky = Character(
    "{b}Zuky{b}",
    color        = "#9c9b9b",
    what_color   = "#9c9b9b",  # o el color que uses para texto
    side_image   = "Zuky base",
    namebox_xpos = 0.68,
    namebox_ypos = 0.08,
    what_xalign  = 0.01,          # alineación perfecta a la derecha (más limpio)
    what_xpos    = 0.30,           # empieza más a la izquierda para que quepa todo
    what_xsize   = 0.45,          # ← ¡esto es clave! Limita el ancho del texto a 55% del textbox
    what_yalign  = 0.43
)

########################### Personajes secundarios ############################
define ralix_fm = Character(
    "{b}Familia Ralix{b}",
    color        = "#000000",
    what_color   = "#000000",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

define ralix_sister = Character(
    "{b}Hermana Ralix{b}",
    color        = "#000000",
    what_color   = "#000000",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

define zuky_mama = Character(
    "{b}Mamá Zuky{b}",
    color        = "#ffffff",
    what_color   = "#acacac",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

########################### Personajes terciarios ###########################

define zuky_friends = Character(
    "{b}Amigas Zuky{b}",
    color        = "#ffffff",
    what_color   = "#acacac",
    side_image   = "Zuky Friends",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

define ralix_friends = Character(
    "{b}Amigos Ralix{b}",
    color        = "#ffffff",
    what_color   = "#acacac",
    side_image   = "Ralix Friends",
    namebox_xpos = 0.24,
    namebox_ypos = 0.08,
    what_xalign  = 0.45,
    what_yalign  = 0.35
)

########################### Personajes genéricos ############################
transform narrator_fade:
    alpha 0
    linear 0.5 alpha 1.0

define narrator = Character(
    None,
    what_xalign=0.5,
    what_color="#63b5fd",
    what_outlines=[(3, "#000000", 0, 0)],
    what_size=32,
    what_italic=True,               # opcional: itálica para pensamientos
    what_atl = narrator_fade        # ← aplica ATL directamente al diálogo
)

define multitud = Character(
    "{b}  {b}",
    what_xalign=0.5,
    what_color="#63b5fd",
    what_outlines=[(3, "#000000", 0, 0)],
    what_size=32,
    what_italic=True,               # opcional: itálica para pensamientos
    what_atl = narrator_fade        # ← aplica ATL directamente al diálogo
)