#############################   Escena: Casa de Ralix   #######################
label apertura_ralix:
    scene bg ralix_room
    show Ralix alegria
    ralix "Vamos a limpiar rápido, tengo que llegar con los chavos" #(alegría)
    ralix "Ya quedó la cama, empezamos con el desayuno y el aseo personal" #(alegría)
    scene bg ralix_comedor
    hide Ralix alegria
    narrator "Ralix desayuna en familia y platican mientras comen."
    show Ralix adoracion
    ralix "Bueno, pues ya me voy, papis, nos vemos por la tarde" #(alegría)
    ralix_fm "Nos vemos, chaparrito, te cuidas" #(alegría)
    ralix "Hasta ahorita, papis, los amo 😘" #(alegría)
    hide Ralix adoracion
    narrator "Comienza el viaje mientras recuerda lo que le costó regresar a su casa."
    scene bg camion
    menu:
        "¿Escuchar radio?":
            jump aper_ralix_radio
        "¿Escuchar música?":
            jump aper_ralix_music

label aper_ralix_radio:
    narrator "Ralix comienza a buscar en las estaciones de radio que recibe en su celular."
    show Ralix alegria
    ralix "Super, veamos qué dicen las noticias" #(alegría)
    hide Ralix alegria
    narrator "El locutor comenta que en los días pasados se presentó una marcha por temas políticos cerca de su casa y que asustó a muchas personas durante ese día."
    show Ralix molestia
    ralix "Estos vatos, por su culpa tuve que esperar 3 horas el metrobús y al final el taxi salió muy caro" #(molestia)
    hide Ralix molestia
    narrator "Durante el viaje al metro terminó escuchando llamadas de personas asustadas, pero pareciera que nada fue real.\n\nLa histeria colectiva es algo muy fácil de extender."
    jump aper_ralix_sal

label aper_ralix_music:
    show Ralix alegria
    ralix "Muy bien, vamos a escuchar buenas canciones" #(alegría)
    hide Ralix alegria
    narrator "Durante todo el viaje escuchó openings de anime. Todo esto antes de que fuera popular."
    show Ralix alegria
    ralix "Qué buenas canciones, ojalá un día la música sea más conocida."
    hide Ralix alegria
    jump aper_ralix_sal

label aper_ralix_sal:
    if camino_ralix == True:
        scene black with dissolve
        centered "{b}ZUKY{/b}"
        scene black with dissolve
        jump apertura_zuky
    return

############################   Escena: Casa de Zuky   ############################
label apertura_zuky:
    scene bg zuky_room
    show Zuky alegria
    zuky "¡Super! Hoy toca día de chicas" #(alegría)
    hide Zuky alegria
    menu:
        "¿Desayunar?":
            jump aper_zuky_desayuna
        "¿Mensaje a amigas?":
            jump aper_zuky_sms
    
label aper_zuky_desayuna:
    scene bg zuky_comedor
    show Zuky alegria
    zuky "Vamos a ver qué hay en el refri, de paso le preparo algo a mi mamá" #(alegría)
    hide Zuky alegria
    narrator "Zuky comienza a preparar el desayuno y, al finalizar, despierta a su mamá."
    show Zuky alegria
    zuky "¡Vente, ma', ya está el desayuno!" #(alegría)
    zuky_mama "Gracias, osito de peluche" #(extasis)
    zuky "De nada, ma', provecho" #(alegría)
    hide Zuky alegria
    narrator "Mientras desayunan, hablan de una marcha relacionada con actos políticos, la cual provocó miedo en los alrededores."
    show Zuky alegria
    zuky "No tienes de qué preocuparte, déjame hablo con mis amigas para que me digan cómo está la situación por sus casas" #(alegría)
    hide Zuky alegria
    jump aper_zuky_metro
    
label aper_zuky_sms:
    narrator "Zuky tomó su teléfono con las patitas temblorosas y abrió el chat con sus amigas."
    narrator "No podía dejar de pensar en ellas... en cómo habrían salido de esa marcha que puso a toda la ciudad patas arriba."
    narrator "El miedo aún flotaba en el aire, pero también la esperanza de que todas estuvieran bien."
    show Zuky ansioso
    zuky "Ufff, sí que se fueron complicados los días pasados, pero parece que ya se solucionó todo, me iré con cuidado" #(ansioso)
    hide Zuky ansioso
    scene bg zuky_comedor
    zuky_mama "Osito de peluche, vamos a comer, ya está el desayuno" #(alegría)
    scene bg zuky_room
    show Zuky alegria
    zuky "Me gana mi mamá preparando el desayuno, bueno, vamos a comer" #(alegría)
    hide Zuky alegria
    narrator "Ambas desayunan y platican sobre lo acontecido en días pasados. Al final se sienten tranquilas al ver que todo está en calma por los alrededores, esto gracias a la platica de Zuky con sus amigas."
    jump aper_zuky_combi

label aper_zuky_metro:
    scene bg camion
    show Zuky calma
    zuky "Tomo un poco más de tiempo del esperado el desayuno, por lo cual tendré que usar el metro" #(calma)
    zuky "Bueno, por el metro es más rápido. Me hubiera gustado ver cómo estaban las cosas por aquí" #(calma)
    hide Zuky calma
    show Zuky miedo
    zuky "Solo recordar lo que pasó me pone nerviosa" #(miedo)
    hide Zuky miedo
    show Zuky calma
    zuky "Tranquila..."
    zuky "Bueno, andando" #(calma)
    scene bg metro
    hide Zuky calma
    narrator "Al llegar al metro, se pone sus audífonos y disfruta del viaje hasta que llega con sus amigas."
    jump aper_zuky_amigas
    
label aper_zuky_combi:
    scene bg camion
    narrator "Al finalizar el desayuno, toma la combi. Es más relajado el viaje y de esa forma validar cómo están los alrededores."
    show Zuky calma
    zuky "Vamos por la combi, espero no se tarde" #(calma)
    hide Zuky calma
    narrator "Sube a la combi, toma asiento y se pone sus audífonos para disfrutar del viaje y ver las casas."
    show Zuky calma
    zuky "Llevo algunos minutos y no veo destrozos como decían en la radio" #(calma)
    hide Zuky calma
    jump aper_zuky_amigas

label aper_zuky_amigas:
    scene bg frikyplaza:
        zoom 1.0
        linear 8.0 zoom 1.05
    show Zuky alegria
    zuky "Hola, ¿qué tal? ¿Cómo están?" #(alegría)
    show Zuky Friends
    zuky_friends "Ya llegó Zuky" #(alegría)
    zuky_friends "Bien, disfrutando del momento. Vengan, vamos a dar la vuelta" #(alegría)
    zuky "¿A dónde vamos?" #(alegría)
    hide Zuky alegria
    hide Zuky Friends
    narrator "Comienzan a caminar y se ponen de acuerdo para ir a la FrikyPlaza, para comer ramen y disfrutar de los productos que venden."
    if camino_ralix == False:
        scene black with dissolve
        centered "{b}RALIX{/b}"
        scene black with dissolve
        jump apertura_ralix
    return
