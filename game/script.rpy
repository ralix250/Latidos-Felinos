
# =============================================
# El juego comienza aquí
# =============================================
label start:
    scene bg cita_1ra with dissolve
    
    show Ralix
    ralix "Mucho gusto mi nombre es Ralix, un placer el conocerte"

    show Zuky
    zuky "El placer es mio, mi nombre es Zuky"
    ralix "¿Tienes novio?             "
    zuky "No...."
    ralix "Pues ahora ya lo tienes"

    $ renpy.notify("¡Ahora son novios!💕")

    "Esperando"
    scene black with dissolve
    return