
label dulces_recuerdos:
    scene bg casa_ideal
    narrator "Una noche, Ralix comenzó a escribir código para un juego."
    show Ralix calma
    ralix "Ha pasado tiempo. Me he sentido muy feliz y, aunque en ocasiones estoy cansado, ver este pequeño niño vale la pena" #(calma)
    hide Ralix calma
    show Ralix calma
    ralix "Ver descansar a mi familia, a mi dulce esposa y a mi pequeño bebé no tiene comparación" #(calma)
    hide Ralix calma
    show Ralix calma
    ralix "Ha sido tan dulce cada momento al lado de los dos. Quién lo diría, incluso tuvimos un gato" #(calma)
    hide Ralix calma
    narrator "Ralix, después de tantos años, quiso dejar un registro de lo que ha vivido. Aunque ha sido pequeño hasta el momento, quiere que sepas"
    narrator "Que cada día de su vida ha sido una alegría infinita."
    show Ralix amor
    ralix "Gracias por acompañarme en mis locuras. Gracias por darme un gran regalo. Y ahora te pregunto" #(amor)
    hide Ralix amor
    menu (screen="final_sanvalentin_menu"):
        "¡SÍ! 🐾💕":
            jump ruta_feliz
        "No... 😿":
            jump ruta_triste
    
label ruta_triste:
    show Ralix amor
    ralix "¿Y si te compro unos Cheetos? ó ¿Palomitas con queso? ¿Qué dices?" #(amor)
    menu (screen="final_sanvalentin_menu"):
        "¡SÍ! 🐾💕":
            jump ruta_feliz
        "No... 😿":
            jump ruta_triste
    hide Ralix amor
    return

label ruta_feliz:
    show Ralix amor
    ralix "El amor que siempre te voy a tener no va a terminar jamás. Junto con nuestro hijo, te amaremos toda la vida" #(amor)
    hide Ralix amor
    return