label matrimonio:
    scene black with dissolve
    centered "Comida en trabajo"
    scene black with dissolve
    jump matrimonio_comida

    scene black with dissolve
    centered "Visita al cine"
    scene black with dissolve
    jump matrimonio_cine

    scene black with dissolve
    centered "Visita al parque"
    scene black with dissolve
    jump matrimonio_parque

    return
    
label matrimonio_comida:
    menu:
        "Comida en área de mesas":
            jump matrimonio_comida_fuera_plaza
        "Comida dentro de plaza":
            jump matrimonio_comida_dentro_plaza
    return

label matrimonio_comida_fuera_plaza:
    scene bg plaza_comida_afuera
    show Zuky confianza
    zuky "Se me fue de volada el día. Apenas pude prepararle algo, espero que le guste❤️" #(confianza)
    hide Zuky confianza
    show Zuky confianza
    zuky "Tenemos sandwichitos y un refresco" #(confianza)
    hide Zuky confianza
    show Zuky confianza
    zuky "Es la primera vez que vengo a su trabajo" #(confianza)
    hide Zuky confianza
    narrator "5 minutos después, Ralix sale de su trabajo y se aproxima donde está Zuky."
    show Ralix amor
    ralix "Hola, mi amor. Muchas gracias por esperarme. Disculpa la tardanza, se alargó una junta" #(amor)
    hide Ralix amor
    show Ralix amor
    ralix "En verdad, gracias por venir. Me siento tan feliz. De verdad te lo agradezco" #(amor)
    hide Ralix amor
    show Zuky amor
    zuky "Discúlpame con los labores de la casa. Apenas pude preparar algo" #(amor)
    hide Zuky amor
    show Ralix amor
    ralix "Eres una gran cocinera y no sabes cómo adoro tu comida. Esas primeras sincronizadas que probé, me enamoraron 💕💕" #(amor)
    hide Ralix amor
    narrator "Juntos se sientan a degustar los alimentos, se miran a los ojos y se dicen hermosas palabras de amor el uno al otro."
    return

label matrimonio_comida_dentro_plaza:
    scene bg plaza_comida_dentro
    show Zuky amor
    zuky "Me dijo que lo esperara aquí adentro. Veamos, voy a buscar una mesita" #(amor)
    hide Zuky amor
    show Ralix amor
    ralix "Hola, mi princesa. Qué bueno que ya llegaste. ¿Te gustaría comer una ensalada o pizza?" #(amor)
    hide Ralix amor
    narrator "Dentro de esa plaza, al ser muy concurrida, había mucha gente. Esperando poder comer, había helados, pizza, de todo un deleite para todos los paladares."
    show Zuky amor
    zuky "Se me antoja una ensalada y unas papitas" #(amor)
    hide Zuky amor
    show Ralix amor
    ralix "Me comentaron que había un lugar de hamburguesas. Yo creo que puedo pedir una y nos sentamos a las mesitas del centro" #(amor)
    hide Ralix amor
    narrator "Ambos obtuvieron su comida y disfrutaron el momento. Zuky le contó su día y lo difícil que fue llegar usando el metro."
    return

label matrimonio_cine:
    scene bg metro
    show Ralix aburrimiento
    ralix "Sí que estuvo muy complicado el camino en el metro" #(aburrimiento)
    hide Ralix aburrimiento
    show Zuky aburrimiento
    zuky "Sí fue demasiado tedioso. Me estaban aplastando mucho" #(aburrimiento)
    hide Zuky aburrimiento
    show Ralix confianza
    ralix "Quien te aplastaba, era yo. Abrazarte y estar cerca de ti para ver tus dulces ojos" #(confianza)
    hide Ralix confianza
    show Zuky amor
    zuky "Ay, mi amor. Qué tierno ❤️" #(amor)
    hide Zuky amor
    ralix "Mi dulce princesa. Dame la mano, sígueme."
    menu:
        "Vayamos a comer antes de la película":
            jump matrimonio_cine_comida
        "Vamos al cine, ya no tarda en empezar la película":
            jump matrimonio_cine_pelicula
        "Comida dentro de plaza":
            jump matrimonio_cine_plaza
    return

label matrimonio_cine_comida:
    scene bg plaza_comida_dentro
    show Zuky anticipacion
    zuky "¿Podemos ir por comida? Mira, está cerca" #(anticipación)
    hide Zuky anticipacion
    show Ralix alegria
    ralix "Claro que sí, mi princesa. De hecho, me recomendaron un lugar que vende ramen" #(alegría)
    hide Ralix alegria
    show Zuky alu
    zuky "Uy, ese me gusta mucho" #(alegría)
    hide Zuky alu
    show Ralix alu
    ralix "Andando, no se diga más" #(alegría)
    hide Ralix alu
    narrator "Pronto fueron los dos a comer ramen mientras esperaban que la película comenzara."
    narrator "El estar tomados de la mano permitía que sus corazones seguían unidos."
    return

label matrimonio_cine_pelicula:
    scene bg cine
    show Ralix extasis
    ralix "Vamos, princesa. El cine está en el último piso. Ya no tarda la película" #(extasis)
    hide Ralix extasis
    show Zuky extasis
    zuky "Sí, vamos" #(extasis)
    hide Zuky extasis
    show Ralix extasis
    ralix "¿Qué te gustaría que compremos de comer?" #(extasis)
    hide Ralix extasis
    show Zuky extasis
    zuky "Mis palomitas con bastante salsa. Unos nachos con queso" #(extasis)
    hide Zuky extasis
    show Ralix extasis
    ralix "¿Y para tomar, princesa?" #(extasis)
    hide Ralix extasis
    show Zuky extasis
    zuky "¿Me compras un ice? 🥰🥰🥰🥰🥰" #(extasis)
    hide Zuky extasis
    show Ralix extasis
    ralix "Lo que pida mi niña hermosa 💕" #(extasis)
    hide Ralix extasis
    narrator "Una vez pedido sus golosinas, entraron al cine a disfrutar de esa hermosa película."
    narrator "Desde su primera cita no han olvidado lo que es verse a los ojos."
    narrator "Al inicio y al final de cada película, el saber que está el uno para el otro es algo que no tiene precio."
    return

label matrimonio_cine_plaza:
    scene bg friky_int:
        xzoom -1
    show Ralix asombro
    ralix "¡Es más grande de lo que pensé esta plaza!" #(asombro)
    hide Ralix asombro
    show Zuky sorpresa
    zuky "Mira, hay un evento de adopción de gatos 🐈‍⬛" #(sorpresa)
    hide Zuky sorpresa
    show Ralix asombro
    ralix "Es cierto, vamos. La película de todos modos empezará por la tarde" #(asombro)
    hide Ralix asombro
    narrator "En ese momento se acercaron al estante donde daban información y juntos fueron a ver a los gatitos."
    show Ralix alu
    ralix "Mira, este se ve bonito. Todo negro" #(alegría)
    hide Ralix alu
    show Zuky alu
    zuky "¿Te imaginas que algún día podamos tener un gatito de ese color?" #(alegría)
    hide Zuky alu
    show Ralix alu
    ralix "¿Cómo te gustaría que se llame?" #(alegría)
    hide Ralix alu
    show Zuky alu
    zuky "No lo sé, lo dejaría el destino" #(alegría)
    hide Zuky alu
    narrator "El disfrute y deleite de esos hermosos ronroneos hicieron que se les fuera muy rápido el tiempo, que incluso olvidaron comer. Disfrutarían su hambre en el cine."
    return

label matrimonio_parque:
    scene bg alameda_diurna
    show Zuky amor
    zuky "Mira, mi amor. Abajo de ese árbol hay una bonita sombra" #(amor)
    hide Zuky amor
    show Ralix amor
    ralix "Claro, vamos" #(amor)
    hide Ralix amor
    narrator "Ambos se prepararon para estar debajo del árbol, sacaron su comida y comenzaron a comer mientras veían a los niños jugar."
    multitud "Algo se apoderó de ellos. Como siempre, nunca se han dejado de mirarse."
    multitud "En la mirada tienen una ventana al alma y supieron que era momento de dar un paso más a su historia."
    show Ralix amor
    ralix "¿Es lindo ver a los niños jugar, no lo creés?" #(amor)
    hide Ralix amor
    show Zuky amor
    zuky "Sería muy lindo estar junto con ellos" #(amor)
    hide Zuky amor
    return
