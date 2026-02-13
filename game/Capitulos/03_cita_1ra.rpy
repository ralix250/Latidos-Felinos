label cita_1ra:
    
    menu:
        "Ralix O_O":
            scene black with dissolve
            jump cita_1ra_ralix
            scene black with dissolve
        "Zuky ^_^":
            scene black with dissolve
            jump cita_1ra_zuky
            scene black with dissolve

label cita_1ra_zuky:
    scene bg zuky_room
    show Zuky ansioso
    zuky "Llegó al fin el día. Es el momento en el que lo volveré a ver después de tanto tiempo" #(ansioso)
    hide Zuky ansioso
    zuky "¿Será realmente como en los mensajes?"
    show bg zuky_comedor
    show Zuky ansioso
    zuky "En el primer encuentro me pareció un buen Chico, pero no sé, aún no sé..." #(ansioso)
    hide Zuky ansioso
    narrator "Durante un tiempo estuvieron hablando por mensajes y en cada uno de ellos se conocieron."
    narrator "Supieron las vivencias del otro y sus momentos más dolorosos, por lo cual tenían empatía. Y aunque no lo sabían, comenzaba el amor a florecer."
    scene bg metro
    show Zuky ansioso
    zuky "Bueno, ya llegué. Espero que no tarde, me mandó un mensaje hace 10 minutos" #(ansioso)
    hide Zuky ansioso
    show Zuky anticipacion
    zuky "Han pasado 5. Si no llega en máximo 10 minutos, me voy" #(anticipación)
    hide Zuky anticipacion
    narrator "En ese momento se encuentra de espaldas mientras comienza a escuchar música."
    jump cita_1ra_zocalo

label cita_1ra_ralix:
    scene ralix_room
    show Ralix calma
    ralix "¡Hay, qué cosas! Qué buena desvelada."
    ralix "Mucho trabajo, pero bueno, llegó el día."
    ralix "Es momento de ver qué pasa, ojalá no lo arruine" #(calma)
    hide Ralix calma
    show Ralix ansioso
    ralix "Vamos, no te rindas. En las conversaciones has sido honesto, no lo arruines, no tengas miedo" #(ansioso)
    hide Ralix ansioso
    show Ralix calma
    ralix "Vamos a terminar de trabajar, dejamos arreglado y salimos corriendo" #(calma)
    hide Ralix calma
    scene bg metro
    narrator "El miedo a dar el siguiente paso es algo que no se puede evitar, pero siempre se debe enfrentar."
    narrator "Es momento de dar el salto... un salto de fe al corazón de la persona que quieres."
    show Ralix ansioso
    ralix "Ufff, ¡corre, corre! Vamos, 5 minutos tarde. Detesto llegar tarde" #(ansioso)
    ralix "Envié mensaje hace 10, espero no se moleste mucho" #(ansioso)
    hide Ralix ansioso
    show Ralix anticipacion
    ralix "Condenada combi haciendo base en cada esquina. Bueno, ya nomás a subir las escaleras" #(anticipación)
    hide Ralix anticipacion
    narrator "Cuando sube las escaleras, ve a lo lejos a una chica con la ropa que le había descrito Zuky."
    show Ralix adoracion
    ralix "Se ve mucho más hermosa que la última vez" #(adoración)
    ralix "Vamos, ten confianza, demos un pequeño salto de fe" #(adoración)
    hide Ralix adoracion
    show Zuky sorpresa
    show Ralix alegria
    zuky "Buenas tardes. Qué bien que ya estás aquí."
    zuky "(Hoy se ve más guapo que la última vez)" #(sorpresa)
    hide Zuky sorpresa
    ralix "Un placer, hermosa dama. Disculpa por llegar tarde. ¿Vamos a comer qué te parece?" #(optimismo)
    hide Ralix alegria
    show Ralix ansioso
    ralix "(Hay, no tengo mucho. Bueno, veamos qué podemos comprar)" #(ansioso)
    hide Ralix ansioso
    show Zuky alegria
    zuky "Claro. ¿A dónde vamos?" #(alegría)
    hide Zuky alegria
    show Ralix alegria
    ralix "Te daré una sorpresa, ven, acompáñame." #(alegría)
    hide Ralix alegria
    narrator "Ambos caminaron hacia los andenes y comenzaron a relatar su mañana."
    jump cita_1ra_zocalo

label cita_1ra_zocalo:
    scene bg zocalo_manana
    show Ralix ansioso
    ralix "(Uffff, ¿a dónde vamos?..., ¿a dónde vamos?...)" #(ansioso)
    hide Ralix ansioso
    show Ralix alegria
    ralix "Ven, conozco un lugar bueno y calmado al que podemos ir" #(alegría)
    hide Ralix alegria
    zuky "Claro."
    scene bg zocalo_comida_manana
    narrator "El comer un cuernito, un helado y una buena bebida fría es algo muy suculento."
    show Ralix alegria
    ralix "Estuvo llenador, sabes, me gustó el sabor" #(alegría)
    hide Ralix alegria
    show Zuky alegria
    zuky "También me gustó" #(alegría)
    hide Zuky alegria
    show Zuky alegria
    zuky "(Debí apoyarlo pero no me dejó pagar. Qué dulce es)" #(alegría)
    hide Zuky alegria
    narrator "Nota: Antes hubo una época donde no había problema que el hombre pagara y que la mujer aceptara una cita económica."
    narrator "Continuamos con la historia."
    show Ralix alegria
    ralix "¿Te propongo que vayamos al Zócalo? Hay un evento musical🎶" #(alegría)
    hide Ralix alegria
    show Ralix alegria
    ralix "(Se ve tan linda cuando sonríe. Espero en verdad que no le parezca mal el lugar)" #(alegría)
    hide Ralix alegria
    show Zuky alegria
    zuky "Sí, vamos. Escuché que sería con música de Michael Jackson👟" #(alegría)
    hide Zuky alegria
    scene bg zocalo_tarde
    narrator "Mientras caminaban, iban platicando locuras que imaginaban. Ralix hablando de anime y Yu-Gi-Oh, mientras que Zuky solo asentía. Aunque interesada en el tema, no sabía sobre el juego TCG."
    show Ralix alegria
    ralix "Mira, ya andan bailando" #(alegría)
    hide Ralix alegria
    show Zuky alegria
    zuky "Disfrutemos del momento" #(alegría)
    hide Zuky alegria
    scene bg zocalo_romantico
    narrator "Horas más tarde."
    narrator "Cuando terminó la cita, las risas no faltaron. Los momentos de alegría no terminaban, pero ambos tenían que ir a su respectivos hogares."
    show Ralix alegria
    ralix "Sabes, me pareció un lindo día. Gracias por ser una hermosa joya."
    ralix "¿Qué tipo de joyita eres?" #(alegría)
    hide Ralix alegria
    zuky "No lo sé, tú dime."
    show Ralix amor
    ralix "Eres jade ante mis ojos: suave al tacto, pero firme en el alma."
    ralix "Tu verde esperanza no se desvanece cuando la noche cae, ni se apaga bajo el sol de la mañana."
    ralix "En tu brillo encuentro fuerza, en tu luz camino, y en tu amor... un futuro que ya no temo, sino que abrazo." #(amor)
    hide Ralix amor
    return
