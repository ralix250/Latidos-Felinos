label noviazgo:
    "Un gran paso para dos tiernos corazones"
    menu:
        "Ralix O_O":
            jump noviazgo_ralix_destino
        "Zuky ^_^":
            jump noviazgo_zuky_destino
    return

label noviazgo_ralix_destino:
    scene bg ralix_room
    show Ralix ansioso
    ralix "Repasemos el plan."
    ralix "Paso 1: alcanzarla en el metro."
    ralix "Paso 2: ir a comer en la Friky."
    ralix "Paso 3: pasar por la Torre Latinoamericana y pasar a la Alameda."
    ralix "Último paso: abrazarla, mirarla a los ojos y abrir mi corazón." #(ansioso)
    hide Ralix ansioso
    scene bg ralix_comedor
    show Ralix ansioso
    ralix "Vamos a desayunar antes y cumplamos el plan" #(ansioso)
    hide Ralix alegria
    narrator "En su mente, el imaginar el primer beso era algo que lo distraía mucho, pero no dejaba de sonreír."
    show Ralix alegria
    ralix "Nos vemos, papis, por la tarde. Bye" #(alegría)
    hide Ralix alegria
    ralix_fm "Nos vemos" #(alegría)
    jump noviazgo_abrazo
    return

label noviazgo_zuky_destino:
    scene bg zuky_room
    show Zuky ansioso
    zuky "Hoy me dijo Ralix que me dará una gran sorpresa. Me pregunto qué será" #(ansioso)
    zuky "Bueno, termino los deberes y vamos al metro para ver a ese muchachón" #(ansioso)
    hide Zuky ansioso
    show Zuky anticipacion
    zuky "¿Mensaje de las chicas?" #(anticipación)
    hide Zuky anticipacion
    zuky_friends "¿Qué tal te ha ido? Ya no nos vemos como antes" #(vigilancia)
    narrator "Durante unos minutos se pusieron al corriente y todas"
    show Zuky ansioso
    zuky "Bueno, chicas, las dejaré un rato, voy de salida" #(ansioso)
    hide Zuky ansioso
    jump noviazgo_abrazo
    return

label noviazgo_abrazo:
    scene bg metro
    show Ralix alegria
    ralix "¡Uff! Hoy sí llegué temprano" #(alegría)
    ralix "Escuchemos un poco de música en lo que llega" #(alegría)
    hide Ralix alegria
    show Zuky tristeza
    zuky "No puede ser, esta vez me ganó. Llevo 10 minutos de retraso" #(tristeza)
    hide Zuky tristeza
    show Zuky molestia
    zuky "Por qué justo y el metro se está tardando tanto" #(molestia)
    hide Zuky molestia
    show Zuky ansioso
    zuky "Ya no tardo, Ralix llegó en un momento. Bueno, con este mensaje espero que me espere" #(ansioso)
    hide Zuky ansioso
    show Ralix alegria
    ralix "Un mensaje, veamos qué dice" #(alegría)
    ralix "O qué tiene Zuky, el metro no ayuda mucho" #(alegría)
    hide Ralix alegria
    narrator "A los pocos minutos, Zuky llegó y Ralix le dio un ramo de rosas."
    narrator "Ambos, después de poner al corriente de lo que había pasado el día, se dirigieron a la Torre Latinoamericana."
    jump noviazgo_torre
    return

label noviazgo_torre:
    scene bg torre_entrada
    show Ralix alegria
    ralix "¡Ya llegamos a la Torre Latinoamericana! ¿Subimos al mirador?" #(alegría)
    hide Ralix alegria
    show Zuky alegria
    zuky "Nunca he subido. Me gustaría ver qué tal se ve" #(alegría)
    hide Zuky alegria
    show Ralix alegria
    ralix "Me contaron que si te bajas un piso antes sale más barato."
    ralix "Discúlpame si no puedo pagar por el momento, pero aprovechamos y vamos a comer" #(alegría)
    hide Ralix alegria
    show Zuky alegria
    zuky "No es necesario que gastes tanto. Con algo sencillo basta" #(alegría)
    hide Zuky alegria
    show Ralix alegria
    ralix "Créeme, para mí no es molestia. Al contrario, te agradezco mucho tu comprensión" #(alegría)
    hide Ralix alegria
    scene bg torre_comedor
    narrator "El deleite de la comida fue tan épico que ambos quedaron satisfechos."
    narrator "Fue tan dulce el momento de la plática que olvidaron que estaban en un punto demasiado elevado."
    narrator "De reojo pudieron ver un helicóptero pasando. Ambos se acercaron al mirador y pudieron apreciar una gran vista."
    scene bg torre_mirador
    show Ralix alegria
    ralix "Si me permites, podemos ir al piso superior. Ahí podemos tener una vista mucho mejor" #(alegría)
    hide Ralix alegria
    narrator "Ambos subieron al piso siguiente y pudieron aprovechar esa hermosa vista de toda la ciudad."
    show Ralix alegria
    ralix "Mira qué vista... ¿Qué te parece? Es encantadora, así como tú 😊" #(alegría)
    ralix "Zuky, este es el lugar perfecto para decirte algo importante..."
    ralix "Yo quisiera......" #(alegría)
    hide Ralix alegria
    show Ralix miedo
    ralix "Quisiera, en verdad... agradecerte por todo." #(miedo)
    hide Ralix miedo
    show Zuky alegria
    zuky "No tienes que agradecer. Las pláticas que tenemos son muy amenas y al pasar tiempo contigo me parece muy agradable" #(alegría)
    hide Zuky alegria
    jump noviazgo_beso
    return

label noviazgo_beso:
    scene bg alameda_minimalista
    narrator "Posterior a la Torre Latinoamericana, ambos fueron a caminar a la Alameda Central. Disfrutaron de un show, platicaron, se vieron a los ojos y, en el momento más crucial, Ralix no tuvo el valor de besarla."
    show Ralix ansioso
    ralix "(Caray, la pena y el miedo son bastante grandes. En verdad que quiero tomarla en mis brazos y besarla, pero me cuesta tanto)" #(ansioso)
    hide Ralix ansioso
    show Zuky alegria
    zuky "¿Y dime qué estás pensando?" #(alegría)
    hide Zuky alegria
    show Ralix adoracion
    ralix "Simplemente deleitándome la vista con tu dulce sonrisa" #(adoración)
    hide Ralix adoracion
    narrator "En ese momento, una sensación en el pecho de Zuky comienza a emerger y, al ver los ojos, el anhelo y el deseo por besarlo es incomparable, pero tampoco se atreve a besarlo."
    narrator "Continuaron caminando uno al lado del otro, riendo y dejando florecer la semilla del amor hasta que fue demasiado tarde y tuvieron que emprender el camino a casa."
    show Ralix alegria
    ralix "Te agradezco infinitamente este hermoso día. No sabes lo feliz que me has hecho" #(alegría)
    hide Ralix alegria
    show Zuky ansioso
    zuky "En verdad me he sentido muy feliz, gracias. Y te agradezco también por acompañarme a la última estación" #(ansioso)
    hide Zuky ansioso
    show Ralix miedo
    ralix "(Tengo miedo, en verdad tengo miedo. No quiero arruinarlo, pero si no lo hago en este momento me arrepentiré el resto de mi vida)" #(miedo)
    hide Ralix miedo
    narrator "Justo en ese momento, Ralix se acercó lentamente, la tomó de sus mejillas y, de una manera delicada pero firme, le robó su primer beso."
    show Zuky alegria
    zuky "{cps=25}💓💞💕😱🥹🥰😍{/cps}" #(alegría)
    hide Zuky alegria
    show Zuky alegria
    zuky "{cps=25}💓😍🥰😱🥹🥰😍💕💞💓{/cps}" #(alegría)
    hide Zuky alegria
    show Zuky alegria
    zuky "{cps=25}🥰😍🥰😍💕💞🥹😱😍💕💞💞{/cps}" #(alegría)
    hide Zuky alegria
    narrator "Con ese beso, las huellitas que llevaban grabadas en el corazón desde el primer encuentro por fin se unieron en un latido compartido."
    return
