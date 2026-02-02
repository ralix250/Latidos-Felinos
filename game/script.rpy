# Definición de la animación de la huella (se mueve de izq a der en 3 segundos y repite)
image paw_anim:
    "images/loading/loading_paw.png" with Dissolve(0.2)  # aparición suave
    xalign 0.2 yalign 0.75
    block:
        linear 1.5 xalign 0.3 yalign 0.70   # sube al centro
        linear 1.5 xalign 0.5 yalign 0.75   # baja al final
        linear 1.5 xalign 0.7 yalign 0.70   # sube al centro
        linear 1.5 xalign 0.9 yalign 0.75   # baja al final
    repeat

screen presplash_progress():
    add Solid("#000000")

    bar value StaticValue(store._presplash_progress or 0.0, 1.0):
        xalign 0.5 yalign 0.75
        xysize (1000, 100)
        left_bar "images/loading/loading_bar_fill.png"
        right_bar "images/loading/loading_bar_empty.png"
        thumb None

    # Huellitas saltando encima de la barra
    add "paw_anim"

    text "Cargando aventura gatuna..." size 40 xalign 0.5 yalign 0.92 color "#ffffff" outlines [(4, "#000000", 0, 0)]

# =============================================
# Label que se ejecuta automáticamente al iniciar
# =============================================
label splashscreen:
    scene black
    with None

    show screen presplash_progress

    python:
        _presplash_progress = 0.0
        renpy.pause(0.4, hard=True)   # pequeña pausa inicial
        _presplash_progress = 0.15
        renpy.pause(0.9, hard=True)
        _presplash_progress = 0.35
        renpy.pause(0.9, hard=True)
        _presplash_progress = 0.55
        renpy.pause(0.9, hard=True)
        _presplash_progress = 0.70
        renpy.pause(1.1, hard=True)
        _presplash_progress = 1.0
        renpy.pause(0.7, hard=True)   # tiempo final para que se vea la barra llena

    hide screen presplash_progress
    return

# =============================================
# El juego comienza aquí
# =============================================
label start:
    scene bg cita_1ra with dissolve
    
    show Ralix
    ralix "Mucho gusto mi nombre es Ralix, un placer el conocerte"
    
    show Zuky
    zuky "El placer es mio, mi nombre es Zuky"

    scene black with dissolve
    return