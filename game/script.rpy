
# =============================================
# El juego comienza aquí
# =============================================
label start:

    scene black with dissolve
    menu:
        "Comencemos el viaje"
        "Ralix O_O":
            jump apertura_ralix
        "Zuky ^_^":
            jump apertura_zuky
    return