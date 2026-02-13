################################################################################
## Inicialización
################################################################################

# Define el desplazamiento de inicialización para que este código se ejecute antes que otros bloques init
init offset = -1


################################################################################
## Estilos
################################################################################

# Define el estilo por defecto para todo el texto usando las propiedades de la GUI
style default:
    properties gui.text_properties()  # Aplica propiedades de texto predefinidas
    language gui.language               # Establece el idioma del texto

# Define el estilo para campos de entrada de texto
style input:
    properties gui.text_properties("input", accent=True)  # Usa propiedades de entrada con acento
    adjust_spacing False                                      # No ajusta el espaciado automáticamente

# Define el estilo para enlaces de hipertexto
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)  # Usa propiedades de hipervínculo con acento
    hover_underline True                                        # Subraya al pasar el cursor

# Define el estilo base para texto de la interfaz gráfica
style gui_text:
    properties gui.text_properties("interface")  # Aplica propiedades de interfaz

# Define el estilo para botones
style button:
    properties gui.button_properties("button")  # Usa propiedades predefinidas para botones

# Define el estilo para texto dentro de botones, heredando de gui_text
style button_text is gui_text:
    properties gui.text_properties("button")  # Aplica propiedades de texto de botón
    yalign 0.5                                # Centra verticalmente el texto

# Define el estilo para etiquetas (labels), heredando de gui_text
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)  # Usa propiedades de etiqueta con acento

# Define el estilo para texto de prompts, heredando de gui_text
style prompt_text is gui_text:
    properties gui.text_properties("prompt")  # Usa propiedades de texto de prompt


# Define el estilo para barras de progreso horizontales
style bar:
    ysize gui.bar_size                                                                          # Define el alto de la barra
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)                      # Imagen para el lado izquierdo
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)                    # Imagen para el lado derecho

# Define el estilo para barras de progreso verticales
style vbar:
    xsize gui.bar_size                                                                          # Define el ancho de la barra
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)                       # Imagen para la parte superior
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)                 # Imagen para la parte inferior

# Define el estilo para barras de desplazamiento horizontales
style scrollbar:
    ysize gui.scrollbar_size                                                                    # Define el alto de la barra de scroll
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)  # Imagen base
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)  # Imagen del pulgar

# Define el estilo para barras de desplazamiento verticales
style vscrollbar:
    xsize gui.scrollbar_size                                                                    # Define el ancho de la barra de scroll
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)    # Imagen base
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)    # Imagen del pulgar

# Define el estilo para controles deslizantes horizontales
style slider:
    ysize gui.slider_size                                                                        # Define el alto del slider
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)            # Imagen base
    thumb "gui/slider/horizontal_[prefix_]thumb.png"                                            # Imagen del control deslizante

# Define el estilo para controles deslizantes verticales
style vslider:
    xsize gui.slider_size                                                                        # Define el ancho del slider
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)              # Imagen base
    thumb "gui/slider/vertical_[prefix_]thumb.png"                                              # Imagen del control deslizante

# Define el estilo para marcos (frames) contenedores
style frame:
    padding gui.frame_borders.padding                                                            # Define el espaciado interior del marco
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)                   # Imagen de fondo del marco



################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

# Define la pantalla de diálogo que muestra conversaciones entre personajes
screen say(who, what):

    # Crea una ventana principal para contener el diálogo
    window:
        id "window"                     # Identificador único para la ventana

        # Si hay un nombre de personaje (who no es None), muestra el nombre
        if who is not None:

            # Crea una ventana secundaria para el nombre del personaje
            window:
                id "namebox"            # Identificador para la caja de nombre
                style "namebox"         # Aplica el estilo de caja de nombre
                text who id "who"       # Muestra el nombre del personaje

        # Muestra el texto del diálogo con el identificador requerido "what"
        text what id "what"


    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):     # Verifica si no es la variante móvil pequeña
        add SideImage() xalign 0.0 yalign 1.0    # Añade la imagen lateral alineada a la izquierda


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')  # Añade 'namebox' como prefijo de ID para estilización

# Define estilos relacionados con el diálogo
style window is default          # El estilo de ventana hereda del estilo default
style say_label is default       # El estilo de etiqueta de diálogo hereda del estilo default
style say_dialogue is default    # El estilo de texto de diálogo hereda del estilo default
style say_thought is say_dialogue  # El estilo de pensamientos hereda del diálogo

# Define estilos para la caja de nombre
style namebox is default          # El estilo de caja de nombre hereda del estilo default
style namebox_label is say_label  # La etiqueta de la caja de nombre usa el estilo say_label


# Configura el estilo de la ventana de diálogo
style window:
    xalign 0.5                                            # Centra horizontalmente
    xfill True                                             # Ocupa todo el ancho disponible
    yalign gui.textbox_yalign                              # Alineación vertical predefinida
    ysize gui.textbox_height                               # Altura predefinida de la caja de texto

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)  # Imagen de fondo alineada abajo y centrada

# Configura el estilo de la caja de nombre
style namebox:
    xpos gui.name_xpos                                     # Posición X predefinida
    xanchor gui.name_xalign                                # Anclaje horizontal predefinido
    xsize gui.namebox_width                                # Ancho predefinido
    ypos gui.name_ypos                                     # Posición Y predefinida
    ysize gui.namebox_height                               # Altura predefinida

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)  # Marco de fondo
    padding gui.namebox_borders.padding                     # Espaciado interior del marco

# Configura el estilo de la etiqueta de nombre
style say_label:
    properties gui.text_properties("name", accent=True)   # Propiedades de texto para nombre con acento
    xalign gui.name_xalign                                 # Alineación horizontal predefinida
    yalign 0.5                                             # Centra verticalmente

# Configura el estilo del texto de diálogo
style say_dialogue:
    properties gui.text_properties("dialogue")              # Propiedades de texto para diálogo

    xpos gui.dialogue_xpos                                 # Posición X predefinida
    xsize gui.dialogue_width                               # Ancho predefinido
    ypos gui.dialogue_ypos                                 # Posición Y predefinida

    adjust_spacing False                                    # No ajusta el espaciado automáticamente

## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

# Define la pantalla para entrada de texto del usuario
screen input(prompt):
    style_prefix "input"                                   # Aplica prefijo de estilo "input"

    # Crea una ventana contenedora
    window:

        # Crea un contenedor vertical
        vbox:
            xanchor gui.dialogue_text_xalign                # Anclaje horizontal del texto
            xpos gui.dialogue_xpos                          # Posición X predefinida
            xsize gui.dialogue_width                        # Ancho predefinido
            ypos gui.dialogue_ypos                          # Posición Y predefinida

            # Muestra el texto de solicitud (prompt)
            text prompt style "input_prompt"
            
            # Crea el campo de entrada de texto con ID requerido
            input id "input"

# Define el estilo del texto de solicitud heredando del estilo default
style input_prompt is default

# Configura el estilo del texto de solicitud
style input_prompt:
    xalign gui.dialogue_text_xalign                        # Alineación horizontal predefinida
    properties gui.text_properties("input_prompt")         # Propiedades de texto para solicitud

# Configura el estilo del campo de entrada
style input:
    xalign gui.dialogue_text_xalign                        # Alineación horizontal predefinida
    xmaximum gui.dialogue_width                            # Ancho máximo permitido


## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# Define la pantalla de menú de elecciones
screen choice(items):
    style_prefix "choice"                                  # Aplica prefijo de estilo "choice"

    # Crea un contenedor vertical
    vbox:
        # Itera sobre cada elemento de la lista de opciones
        for i in items:
            # Crea un botón de texto con la opción y su acción correspondiente
            textbutton i.caption action i.action

# Define estilos para los componentes del menú de elección
style choice_vbox is vbox                                   # El contenedor vertical hereda de vbox
style choice_button is button                               # Los botones heredan de button
style choice_button_text is button_text                     # El texto de botones hereda de button_text

# Configura el estilo del contenedor vertical de elecciones
style choice_vbox:
    xalign 0.5                                              # Centra horizontalmente
    ypos 405                                                # Posición vertical específica
    yanchor 0.5                                             # Anclaje vertical centrado
    spacing gui.choice_spacing                              # Espaciado entre elementos predefinido

# Configura el estilo de los botones de elección
style choice_button is default:
    properties gui.button_properties("choice_button")        # Propiedades predefinidas para botones de elección

# Configura el estilo del texto de los botones de elección
style choice_button_text is default:
    properties gui.text_properties("choice_button")          # Propiedades de texto para botones de elección


## Pantalla de menú rápido #####################################################
##
## El menú rápido se presenta en el juego para ofrecer fácil acceso a los menus
## externos al juego.

# Define la pantalla del menú rápido de acceso durante el juego
screen quick_menu():

    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100                                              # Prioridad de renderizado máxima

    # Solo muestra el menú rápido si está habilitado
    if quick_menu:

        # Crea un contenedor horizontal para los botones
        hbox:
            style_prefix "quick"                            # Aplica prefijo de estilo "quick"
            style "quick_menu"                              # Aplica estilo específico del menú rápido

            # Botón para retroceder en el diálogo
            textbutton _("Atrás") action Rollback()
            
            # Botón para acceder al historial de diálogo
            textbutton _("Historial") action ShowMenu('history')
            
            # Botón para saltar diálogo (normal o rápido)
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            
            # Botón para activar/desactivar avance automático
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            
            # Botón para abrir menú de guardado
            textbutton _("Guardar") action ShowMenu('save')
            
            # Botón para guardar partida rápidamente
            textbutton _("Guardar R.") action QuickSave()
            
            # Botón para cargar partida rápida
            textbutton _("Cargar R.") action QuickLoad()
            
            # Botón para acceder a preferencias
            textbutton _("Prefs.") action ShowMenu('preferences')


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")             # Añade quick_menu a la lista de pantallas superpuestas

# Variable por defecto para controlar la visibilidad del menú rápido
default quick_menu = True

# Define estilos para los componentes del menú rápido
style quick_menu is hbox                                    # El contenedor hereda de hbox
style quick_button is default                               # Los botones heredan de default
style quick_button_text is button_text                     # El texto hereda de button_text

# Configura el estilo del contenedor del menú rápido
style quick_menu:
    xalign 0.5                                              # Centra horizontalmente
    yalign 1.0                                              # Alinea al fondo de la pantalla

# Configura el estilo de los botones del menú rápido
style quick_button:
    properties gui.button_properties("quick_button")         # Propiedades predefinidas para botones rápidos

# Configura el estilo del texto de los botones del menú rápido
style quick_button_text:
    properties gui.text_properties("quick_button")           # Propiedades de texto para botones rápidos


################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

# Define la pantalla de navegación principal
screen navigation():

    # Crea un contenedor vertical para los botones de navegación
    vbox:
        style_prefix "navigation"                            # Aplica prefijo de estilo "navigation"

        xpos gui.navigation_xpos                             # Posición X predefinida
        yalign 0.5                                           # Centra verticalmente

        spacing gui.navigation_spacing                       # Espaciado entre botones predefinido

        # Si estamos en el menú principal, muestra el botón de empezar
        if main_menu:

            textbutton _("Comenzar") action Start()           # Botón para comenzar nueva partida

        else:                                                # Si no, estamos en el menú del juego

            textbutton _("Historial") action ShowMenu("history")  # Botón para ver historial
            textbutton _("Guardar") action ShowMenu("save")        # Botón para guardar partida

        # Botón de cargar partida (siempre visible)
        textbutton _("Cargar") action ShowMenu("load")

        # Botón de opciones (siempre visible)
        textbutton _("Opciones") action ShowMenu("preferences")

        # Si estamos en modo repetición
        if _in_replay:

            textbutton _("Finaliza repetición") action EndReplay(confirm=True)  # Botón para terminar repetición

        elif not main_menu:                                  # Si no estamos en menú principal ni en repetición

            textbutton _("Menú principal") action MainMenu()  # Botón para volver al menú principal

        # Botón de Acerca de (siempre visible)
        textbutton _("Acerca de") action ShowMenu("about")

        # Si es PC o Web no móvil, muestra el botón de ayuda
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## La ayuda no es necesaria ni relevante en dispositivos móviles.
            textbutton _("Ayuda") action ShowMenu("help")

        # Si es PC, muestra el botón de salir
        if renpy.variant("pc"):

            ## El botón de salida está prohibido en iOS y no es necesario en
            ## Android y Web.
            textbutton _("Salir") action Quit(confirm=not main_menu)  # Botón para salir del juego


# Define estilos para los componentes de navegación
style navigation_button is gui_button                        # Los botones heredan de gui_button
style navigation_button_text is gui_button_text              # El texto hereda de gui_button_text

# Configura el estilo de los botones de navegación
style navigation_button:
    size_group "navigation"                                   # Agrupa botones para igualar tamaño
    properties gui.button_properties("navigation_button")    # Propiedades predefinidas para botones de navegación

# Configura el estilo del texto de los botones de navegación
style navigation_button_text:
    properties gui.text_properties("navigation_button")      # Propiedades de texto para botones de navegación


## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu



# Define estilos para los componentes del menú principal
style main_menu_frame is empty                               # El marco hereda del estilo empty
style main_menu_vbox is vbox                                 # El contenedor vertical hereda de vbox
style main_menu_text is gui_text                             # El texto hereda de gui_text
style main_menu_title is main_menu_text                     # El título hereda del texto del menú
style main_menu_version is main_menu_text                   # La versión hereda del texto del menú

# Configura el estilo del marco del menú principal
style main_menu_frame:
    xsize 420                                                # Ancho fijo del marco
    yfill True                                               # Ocupa todo el alto disponible
    background "gui/overlay/main_menu.png"                   # Imagen de fondo del marco

# Configura el estilo del contenedor vertical del menú principal
style main_menu_vbox:
    xalign 1.0                                               # Alinea a la derecha
    xoffset -30                                              # Desplazamiento izquierdo desde el borde
    xmaximum 1200                                            # Ancho máximo permitido
    yalign 1.0                                               # Alinea al fondo
    yoffset -30                                              # Desplazamiento hacia arriba desde el fondo

# Configura el estilo base del texto del menú principal
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)  # Propiedades de texto con acento

# Configura el estilo del título del menú principal
style main_menu_title:
    properties gui.text_properties("title")                  # Propiedades predefinidas para título

# Configura el estilo de la versión del menú principal
style main_menu_version:
    properties gui.text_properties("version")                # Propiedades predefinidas para versión


## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Se usa esta
## pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

# Define la pantalla base para los menús del juego
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"                               # Aplica prefijo de estilo "game_menu"

    # Selecciona el fondo apropiado según si estamos en el menú principal o no
    if main_menu:
        add gui.main_menu_background                         # Fondo del menú principal
    else:
        add gui.game_menu_background                          # Fondo del menú del juego

    # Crea un marco exterior contenedor
    frame:
        style "game_menu_outer_frame"                         # Aplica estilo del marco exterior

        # Crea un contenedor horizontal
        hbox:

            ## Reservar espacio para la sección de navegación.
            frame:
                style "game_menu_navigation_frame"           # Marco para la sección de navegación

            # Marco principal para el contenido
            frame:
                style "game_menu_content_frame"              # Marco para el contenido principal

                # Si el scroll es de tipo viewport
                if scroll == "viewport":

                    viewport:
                        yinitial yinitial                     # Posición Y inicial
                        scrollbars "vertical"                  # Barra de scroll vertical
                        mousewheel True                        # Habilita scroll con rueda del ratón
                        draggable True                         # Permite arrastrar
                        pagekeys True                          # Habilita teclas de página

                        side_yfill True                        # El contenido ocupa todo el alto

                        vbox:
                            spacing spacing                   # Espaciado entre elementos

                            transclude                       # Transcluye el contenido aquí

                # Si el scroll es de tipo vpgrid (viewport grid)
                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1                                # Una columna
                        yinitial yinitial                     # Posición Y inicial

                        scrollbars "vertical"                  # Barra de scroll vertical
                        mousewheel True                        # Habilita scroll con rueda del ratón
                        draggable True                         # Permite arrastrar
                        pagekeys True                          # Habilita teclas de página

                        side_yfill True                        # El contenido ocupa todo el alto

                        spacing spacing                       # Espaciado entre elementos

                        transclude                           # Transcluye el contenido aquí

                # Si no hay scroll
                else:

                    transclude                               # Transcluye el contenido directamente

    # Incluye la pantalla de navegación
    use navigation

    # Botón para volver al menú anterior
    textbutton _("Volver"):
        style "return_button"                                # Aplica estilo de botón de retorno
        action Return()                                       # Acción para volver atrás

    # Muestra el título del menú
    label title

    # Si estamos en el menú principal, permite acceder con tecla ESC
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")         # Tecla de menú abre el menú principal


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu(_("Huellitas de nuestro amor 🐾💕"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}R") action FilePage("quick")

                    ## range(1, 10) da los números del 1 al 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Subir Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Descargar Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Opciones"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action Preference("display", "window")
                        textbutton _("Pantalla completa") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action Preference("skip", "toggle")
                    textbutton _("Tras elecciones") action Preference("after choices", "toggle")
                    textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

                ## Aquí se pueden añadir 'vboxes' adicionales del tipo
                ## "radio_pref" o "check_pref" para nuevas preferencias.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Veloc. texto")

                    bar value Preference("text speed")

                    label _("Veloc. autoavance")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volumen música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volumen sonido")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Prueba") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volumen voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Prueba") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Silenciar todo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
    predict False

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Esto distribuye los elementos apropiadamente si
                ## 'history_height' es 'None'.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Toma el color del texto 'who' de 'Character', si ha
                        ## sido establecido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("El historial está vacío.")


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Intro")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Inicio, Guía, B/Botón Derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Asegura que otras pantallas no reciban entrada mientras se muestra esta
    ## pantalla.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Sí") action yes_action
                textbutton _("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):
    zorder 100  # siempre encima de todo
    style_prefix "notify"

    # Frame centrado en la pantalla
    frame:
        xalign 0.5          # ¡centro horizontal!
        yalign 0.5          # ¡centro vertical! (o 0.4 si quieres un poquito más arriba)
        xysize (500, 120)   # tamaño cómodo para móviles y PC
        padding (30, 20)

        text "[message!tq]":
            xalign 0.5
            yalign 0.5
            size 36
            color "#ffffff"
            outlines [(4, "#000000", 0, 0)]  # borde negro para legibilidad

    # Desaparece sola después de 3 segundos
    timer 3.0 action Hide('notify')

# Transform para que aparezca y desaparezca suave
transform notify_appear:
    on show:
        alpha 0
        zoom 0.9
        linear 0.3 alpha 1.0 zoom 1.0
    on hide:
        linear 0.4 alpha 0 zoom 0.9

style notify_frame:
    background "gui/notify_bg.png"  # tu imagen personalizada
    padding (40, 30, 40, 30)        # espacio interno para que el texto no toque los bordes
    xalign 0.5
    yalign 0.5
## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

# Estilo custom para narrador 
style narrator_text is say_dialogue:
    color "#63b5fd"                   # azul claro que querías
    size 32                             # opcional
    outlines [(3, "#000000", 0, 0)]   # borde negro

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Ya que puede carecer de ratón, se reempleza el menú rápido con una versión
## con menos botones y más grandes, más fáciles de tocar.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Atrás") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menú") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

# === MENÚ FINAL SAN VALENTÍN - SOLO ESTA SCREEN ===
screen final_sanvalentin_menu(items):
    modal True
    zorder 200

    add "images/background/bg_valentine.png" xalign 0.5 yalign 0.5 zoom 1.05

    #frame:
    #    xalign 0.5
    #    yalign 0.5
    #    xysize (800, 400)
    #    background "#00000080"  # fondo negro semi-transparente (cámbialo por tu imagen si quieres)

    vbox:
        xalign 0.5
        yalign 0.9
        spacing 60
        #text "":
        #    xalign 0.5
        #    size 48
        #    color "#ff69b4"
        #    outlines [(4, "#000000", 0, 0)]
        hbox:
            xalign 0.5
            spacing 120
            textbutton "¡SÍ! 🐾💕":
                action Return(0)
                xsize 320
                ysize 140
                background "#ff69b4"
                hover_background "#ff85c0"
                text_size 40
                text_color "#ffffff"
                
            textbutton "No... 😿":
                action Return(1)
                xsize 320
                ysize 140
                background "#696969"
                hover_background "#808080"
                text_size 40
                text_color "#ffffff"
