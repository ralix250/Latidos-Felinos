#Escena : Casa de Ralix 
label apertura_ralix:
    #Acto : Ralix despierta y comienza con los preparativos para ir con sus amigos a la frikyplaza
    scene bg ralix_room
    show  Ralix alegria
    ralix 'vamos a limpiar rápido, tengo que llegar con los youuˋs'#(alegría)
    ralix 'ya quedó la cama, empezamos con el desayuno y el aseo personal'#(alegría)
    hide Ralix alegria
    narrator 'Ralix desayuna en familia y platican mientras comen'
    show  Ralix adoracion
    ralix 'Bueno pues ya me voy papis, nos vemos por la tarde'#(alegría)
    hide Ralix adoracion
    ralix_fm 'Nos vemos chaparrito te cuidas'#(alegría)
    show  Ralix adoracion
    ralix 'Hasta al ratito papis, los amo 😘'#(alegría)
    hide Ralix adoracion
    narrator 'Comienza el viaje mientras recuerda lo que le costó regresar a su casa '
    menu:
        "Escuchar radio?":
            jump aper_ralix_radio
        "Escuchar musica?":
            jump aper_ralix_music

label aper_ralix_radio:
    narrator 'Ralix comienza a buscar en las estaciones de radio que recibe en su celular'
    show  Ralix alegria
    ralix 'Super veamos que dicen las noticias'#(alegría)
    hide Ralix alegria
    narrator 'El locutor de radio comenta que en los dìas pasados se presento una marcha por temas políticos cerca de su casa y que espanto a muchas personas durante ese dìa'
    show  Ralix alegria
    ralix 'Estos vatos por su culpa tuve que esperar 3 horas el metrobus y al final el taxi salio muy caro'#(molestia)
    hide Ralix alegria
    narrator 'Durante el viaje al metro termino escuchando todas las llamadas donde mucha gente estaba espantada pero pareciera que nada fue real.
    La histeria colectiva es algo muy fácil de extender'

label aper_ralix_music:
    show  Ralix alegria
    ralix 'Muy bien vamos a escuchar buenas canciones'#(alegría)
    hide Ralix alegria
    narrator 'Durante todo el viaje escucho openings de anime. Todo esto antes de que fuera popular'
    show  Ralix alegria
    ralix 'Que buenas canciones, ojalá un dìa la música sea mas conocida'
    hide Ralix alegria

#Escena : Casa Zuky
label apertura_zuky:
    scene bg zuky_room
    show  Zuky alegria
    zuky 'Super, hoy toca día de chicas'#(alegría)
    menu:
        "Desayunar?":
            jump aper_zuky_desayuna
        "Mensaje a amigas?":
            jump aper_zuky_sms
    
label aper_zuky_desayuna:
    zuky 'Vamos a ver que hay en el refri, de paso le preparo algo a mi mamá'#(alegría)
    narrator'Zuky comienza a prepar el desayuno y al finalizar despierta a su mamá'
    zuky 'Vente má ya esta el desayuno '#(alegría)
    zuky_mama 'Gracias Osito de peluche'#(éxtasis)
    zuky 'Denada má provecho'#(alegría)
    narrator'Mientras desayunan hablan de una marcha relacionada con actos políticos la cual provoco miedo en los alrededores'
    zuky 'No tienes de que preocuparte, déjame hablo con mis amigas para que me digan como esta la situaciòn por sus casas'
    jump aper_zuky_metro
    
label aper_zuky_sms:
    narrator'Zuky envía varios mensajes para ponerse deacuerdo con sus amigas para ver como se encuentran luego de haber pasado algunos dìas de una marcha relacionada con actos políticos la cual provoco miedo en los alrededores'
    zuky 'Ufff, si que se fueron complicados los dìas pasados pero parece que ya se soluciono todo, me iré con cuidado'#(ansioso)
    zuky_mama 'Osito de peluche vamos a comer, ya esta el desayuno'#(alegría)
    zuky 'Me gano mi mamá a preparar el desayuno, bueno vamos a comer'#(alegría)
    narrator'Ambas desayunan y platican sobre lo acontecido en dìas pasados, al final se sienten tranquilas al ver que todo esta en calma por los alrededores, esto gracias a la platica de Zuky con sus amigas'
    jump aper_zuky_combi

#Escena : Ruta de transporte
label aper_zuky_metro:
    zuky  'Tomo un poco màs de tiempo del esperado el desayuno por lo cual tiene que usar el metro'
    zuky 'Bueno por el metro, es más rapido, me hubiera gustado ver como estaban las cosas por aca'#(calma)
    zuky 'Solo recordar lo que paso me pone de nervios'#(miedo)
    zuky 'Tranquila....'
    zuky 'Bueno andando '#(calma)
    narrator'Al llegar al metro se pone sus audífonos y disfruta del viaje hasta que llega con sus amigas'
    jump aper_zuky_amigas
    
label aper_zuky_combi:
    narrator 'Al finalizar el desayuno toma la combi que es más relajado el viaje y de esa forma validar como estan los alrededores'
    zuky 'vamos por la combi, espero no se tarde' #(calma)
    narrator 'Sube a la combi, al tomar asiento se pone sus audifonos para disfrutar el viaje y ver las casas'
    zuky 'pues llevo algunos minutos y no veo destrozos como decían en la radio'#(calma)
    jump aper_zuky_amigas

#Escena : Zuky llegó a la estación donde estarían sus amigas esperándola 
label aper_zuky_amigas:
    zuky_friends 'ya llegó Zuky'#(alegría)
    zuky 'hola que tal ¿Cómo están?'#(alegría)
    zuky_friends 'Bien, disfrutando del momento, vengan vamos a dar la vuelta'#(alegría)
    zuky '¿A donde vamos?'#(alegría)
    narrator 'Comienzan a caminar y se ponen deacuerdo a ir a la FrikyPlaza, para comer ramen y disfrutar de los productos que venden'

