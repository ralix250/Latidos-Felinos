label embarazo:
    menu:
        "Lágrimas de felicidad":
            jump embarazo_lagrimas
        "Sorpresa silenciosa":
            jump embarazo_sorpresa
    return

label embarazo_lagrimas:
    scene bg plaza_comida_afuera
    narrator "Ha pasado tiempo desde el primer día de campo. Lo que no ha pasado es el amor que"
    show Zuky ansioso
    zuky "Ay, qué nervios. Me siento ansiosa" #(ansioso)
    hide Zuky ansioso
    show Zuky ansioso
    zuky "También tengo hambre. Estos antojos" #(ansioso)
    hide Zuky ansioso
    show Ralix amor
    ralix "Hola, mi amor. Muchas gracias por esperarme." #(amor)
    hide Ralix amor
    show Zuky sorpresa
    zuky "Mi amor, antes de que podamos comer, quisiera contarte algo" #(sorpresa)
    hide Zuky sorpresa
    show Ralix amor
    ralix "Claro que sí, mi amor. ¿Qué pasó?" #(amor)
    hide Ralix amor
    show Zuky ansioso
    zuky "¿Me puedes pasar mi mochila, por favor?" #(ansioso)
    hide Zuky ansioso
    narrator "Ralix, al momento de pasársela y levantarla, descubre un pequeño sobre debajo de su mochila."
    show Ralix amor
    ralix "¿Te doy también tu sobre? 💌" #(amor)
    hide Ralix amor
    show Zuky ansioso
    zuky "Es tuyo. Lee lo que dice" #(ansioso)
    hide Zuky ansioso
    narrator "Con cada palabra, la expresión de Ralix cambia. Una felicidad inmensa y no pudo contener sus lágrimas. Será padre."
    return

label embarazo_sorpresa:
    scene bg plaza_comida_afuera
    show Zuky ansioso
    zuky "Ay, ay, qué nervios" #(ansioso)
    hide Zuky ansioso
    show Ralix amor
    ralix "Hola, mi amor" #(amor)
    hide Ralix amor
    show Zuky ansioso
    zuky "Sabes, no puedo esperar. Necesito decírtelo" #(ansioso)
    hide Zuky ansioso
    show Ralix amor
    ralix "¿Cuéntame qué pasó?" #(amor)
    hide Ralix amor
    narrator "Con esas palabras, la semilla de un nuevo latido ya crecía en ellos."
    narrator "Ralix, sin decir nada, solo pudo abrazarla fuerte y dejar que su amor floreciera en un beso que sellaba su futuro juntos. 👼👼"
    return
