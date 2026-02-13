# transitions.rpy - Todas las transiciones con ATL fade in/out suave

image trans_encuentro:
    "images/transitions/transition_encuentro.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.5
    linear 1.0 alpha 0.0

image trans_1ra_cita:
    "images/transitions/transition_1ra_cita.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.5
    linear 1.0 alpha 0.0

image trans_noviazgo:
    "images/transitions/transition_noviazgo.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.5
    linear 1.0 alpha 0.0

image trans_relacion_novios:
    "images/transitions/transition_relacion_novios.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.5
    linear 1.0 alpha 0.0

image trans_propuesta:
    "images/transitions/trans_propuesta.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0  # un poquito más para la emoción
    linear 1.0 alpha 0.0

image trans_boda:
    "images/transitions/trans_boda.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0

image trans_matrimonio:
    "images/transitions/trans_matrimonio.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0

image trans_embarazo:
    "images/transitions/trans_embarazo.jpg"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0

image trans_recuerdos:
    "images/transitions/trans_recuerdos.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0


label trans_encuentro:
    show trans_encuentro
    return

label trans_1ra_cita:
    show trans_1ra_cita
    return

label trans_noviazgo:
    show trans_noviazgo
    return

label trans_relacion_novios:
    show trans_relacion_novios
    return

label trans_propuesta:
    show trans_propuesta
    return

label trans_boda:
    show trans_boda
    return

label trans_matrimonio:
    show trans_matrimonio
    return

label trans_embarazo:
    show trans_embarazo
    return

label trans_recuerdos:
    show trans_recuerdos
    return