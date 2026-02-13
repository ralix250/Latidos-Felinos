default camino_ralix = False

# =============================================
# El juego comienza aquí
# =============================================
label start:
    scene black with dissolve
    
    #Apertura
    menu:
        "Comencemos el viaje"
        "Ralix O_O":
            $ camino_ralix = True
            scene black with dissolve
            call apertura_ralix from _call_apertura_ralix
            scene black with dissolve
        "Zuky ^_^":
            scene black with dissolve
            call apertura_zuky from _call_apertura_zuky
            scene black with dissolve
    
    #"Encuentro"
    call trans_encuentro from _call_trans_encuentro
    pause 3.5
    call encuentro from _call_encuentro
    scene black with dissolve
    #"1ra Cita"
    call trans_1ra_cita from _call_trans_1ra_cita
    pause 3.5
    call cita_1ra from _call_cita_1ra
    scene black with dissolve
    #"Noviazgo"
    call trans_noviazgo from _call_trans_noviazgo
    pause 3.5
    call noviazgo from _call_noviazgo
    scene black with dissolve
    #"Relación Novios"
    call trans_relacion_novios from _call_trans_relacion_novios
    pause 3.5
    call relacion_novios from _call_relacion_novios
    scene black with dissolve
    #"Propuesta"
    call trans_propuesta from _call_trans_propuesta
    pause 3.5
    call propuesta from _call_propuesta
    scene black with dissolve
    #"Boda"
    call trans_boda from _call_trans_boda
    pause 3.5
    call boda from _call_boda
    scene black with dissolve
    #"Matrimonio"
    call trans_matrimonio from _call_trans_matrimonio
    pause 3.5
    call matrimonio from _call_matrimonio
    scene black with dissolve
    #"Hermosa Sorpresa"
    call trans_embarazo from _call_trans_embarazo
    pause 3.5
    call embarazo from _call_embarazo
    scene black with dissolve
    #"Dulces Recuerdos"
    call trans_recuerdos from _call_trans_recuerdos
    pause 3.5
    call dulces_recuerdos from _call_dulces_recuerdos
    # Fin del juego
    scene black with dissolve
    return