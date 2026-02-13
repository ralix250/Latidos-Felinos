label encuentro:
    menu:
        "Zuky ^_^":
            jump encuentro_zuky_friends
        "Ralix O_O":
            jump encuentro_ralix_friends

label encuentro_ralix_friends:
    scene bg frikyplaza
    show Ralix extasis
    ralix "Muy bien, ya estamos todos. ¿Qué tal les fue el día de la marcha?" #(extasis)
    hide Ralix extasis
    show Ralix alegria
    show Ralix Friends
    ralix_friends "Todo en calma, por nuestras casas no se presentaron problemas" #(alegría)
    hide Ralix Friends
    hide Ralix alegria
    show Ralix extasis
    ralix "Pues no se diga más, vamos por las cartas" #(extasis)
    hide Ralix extasis
    narrator "Durante un tiempo estuvieron revisando cartas para mejorar su deck y, como buenos carpeteros, encontraron lo que necesitaban."
    show Ralix alegria
    ralix "Oigan, ¿quieren ir a comer o vamos a dar la vuelta?" #(alegría)
    hide Ralix alegria
    menu:
        "¿Ir a comer?":
            jump encuentro_ralix_comida
        "¿Explorar edificio?":
            jump encuentro_ralix_caminar

label encuentro_ralix_comida:
    scene bg friky_int:
        zoom 1.0
        linear 8.0 zoom 1.05
    show Ralix alegria
    ralix "¿Qué les parecen unas tortas? En el último piso venden" #(alegría)
    hide Ralix alegria
    show Ralix Friends
    ralix_friends "A mí me gustaría una maruchan"
    ralix_friends "Yo quisiera unas quesadillas" #(alegría)
    ralix "¿Les parece bien si voy hasta arriba y ahorita les mando mensaje si encuentro maruchan?" #(alegría)
    ralix_friends "Va, nos avisas" #(alegría)
    hide Ralix Friends
    hide Ralix alegria
    jump encuentro_ralix_comprar_comida

label encuentro_ralix_caminar:
    scene bg friky_int:
        zoom 1.0
        linear 8.0 zoom 1.05
    show Ralix Friends
    ralix_friends "En lo que estábamos revisando carpetas, dicen que hay torneo de peleas. Vamos y ahorita vamos a comer" #(alegría)
    show Ralix alegria
    ralix "Ando muy oxidado en eso, pero me gusta la idea" #(alegría)
    hide Ralix alegria
    hide Ralix Friends
    narrator "Durante unos minutos estuvieron jugando hasta que pagaron para entrar al torneo."
    show Ralix interes
    ralix "En un momento regreso, voy a comprar algo, unas papas o algo para botanear" #(interés)
    hide Ralix interes
    jump encuentro_ralix_comprar_comida

label encuentro_ralix_comprar_comida:
    scene bg friky_comida:
        xzoom -1
    narrator "En ese momento, Ralix comenzó a olfatear un aroma muy dulce. Algo que no era comida, pero le interesó mucho."
    show Ralix interes
    ralix "¿Qué dulce perfume? Me pregunto de quién sería" #(interés)
    ralix "Bueno, si lo vuelvo a oler, estaré al pendiente mientras vamos por mis papitas" #(interés)
    hide Ralix interes
    narrator "Ralix siguió caminando, se acercó a preguntar en varios locales hasta que subió al piso de comida y olfateaba un gran aroma."
    jump encuentro_escuchar

label encuentro_zuky_friends:
    scene bg frikyplaza:
        zoom 1.0
        linear 8.0 zoom 1.05
    show Zuky alegria
    show Zuky Friends
    zuky "En el segundo piso están los animes, vamos" #(alegría)
    zuky_friends "Sí, vamos. Acá tengo la lista de los que me faltan" #(alegría)
    hide Zuky alegria
    hide Zuky Friends
    scene bg friky_int:
        zoom 1.0
        linear 8.0 zoom 1.05
    narrator "La cantidad de gente que había en ese momento fue algo que se esperaban, pero aun así no estaban felices por haber tanta concurrencia."
    show Zuky Friends
    zuky_friends "Oigan, ¿qué tal si vamos a comer? Ya me muero de hambre."
    zuky_friends "Yo también."
    zuky_friends "Secundo la moción" #(interés)
    hide Zuky Friends
    scene bg friky_comida
    show Zuky alegria
    zuky "Vamos a donde están los juegos, ahí está el ramen" #(alegría)
    hide Zuky alegria
    narrator "Cada una pidió su platillo favorito en el restaurante que se encontraba junto donde se estaba haciendo el torneo de peleas."
    narrator "Durante la espera comenzaron a platicar y nuevamente salió la platica de la marcha."

label encuentro_escuchar:
    scene bg friky_ramen:
        zoom 1.0
        linear 8.0 zoom 1.05
    narrator "Sin percatarse el uno del otro, ambos estaban tan cerca que el inicio de algo glorioso comenzaría por la curiosidad."
    show Ralix interes
    ralix "Hola, buenas tardes. Perdonen que las interrumpa, pero ¿también pasaron por lo de la marcha?" #(interés)
    hide Ralix interes
    show Zuky interes
    show Zuky Friends
    zuky_friends "Sí, fue algo que nos asustó al inicio, pero ya sabes, nada de qué preocuparse" #(interés)
    zuky "Cuando salí de la uni y vi negocios cerrados, me asusté un poco. Esperaba que mi mamá llegara bien" #(interés)
    ralix "Sabes, me pasó algo parecido. Yo igual estaba en la universidad y no pasaba mi transporte, esperé por 3 horas más o menos" #(interés)
    hide Zuky Friends
    hide Ralix interes
    hide Zuky interes
    narrator "Ambos, al momento de hablarse el uno al otro, sintieron algo particular, pero no prestaban atención."
    narrator "Conforme fueron platicando, llegaron al punto en que intercambiaron números de teléfono y correos para continuar con la charla."
    narrator "En ese momento, el torneo de juegos y el ramen pasaron a segundo plano."
    return
