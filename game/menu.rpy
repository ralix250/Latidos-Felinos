# menu.rpy
# =============================================
# Contiene TODOS los menús personalizados del juego:
# - main_menu (con 2 columnas, ATL y purr)
# - navigation (barra lateral o inferior)
# - Animaciones ATL y sonidos comunes
# =============================================

# Transform ATL para botones (rebote suave al hover)
transform btn_hover_anim:
    on hover:
        zoom 1.05
        linear 0.15 yoffset -10
        linear 0.15 yoffset 0
    on idle:
        linear 0.2 zoom 1.0 yoffset 0

# Sonido hover (versión corta, 1s o menos – ¡asegúrate de tener este archivo!)
define hover_purr = "audio/efectos/Cat Purr Short.mp3"

# =============================================
# Menú principal (pantalla inicial del juego)
# =============================================
screen main_menu():
    tag menu

    # Fondo personalizado (cambia por tu imagen si no usas gui)
    add gui.main_menu_background  # o usa gui.main_menu_background si lo prefieres

    # Grid de 2 columnas x 3 filas (6 botones)
    grid 2 3:
        xalign 0.5
        yalign 0.85
        xspacing 80
        yspacing 40

        # Fila 1
        imagebutton:
            idle "gui/menu/btn_jugar.png"
            hover "gui/menu/btn_jugar_hover.png"
            hover_sound hover_purr
            action Start()
            at btn_hover_anim

        imagebutton:
            idle "gui/menu/btn_cargar.png"
            hover "gui/menu/btn_cargar_hover.png"
            hover_sound hover_purr
            action ShowMenu("load")
            at btn_hover_anim

        # Fila 2
        imagebutton:
            idle "gui/menu/btn_opciones.png"
            hover "gui/menu/btn_opciones_hover.png"
            hover_sound hover_purr
            action ShowMenu("preferences")
            at btn_hover_anim

        imagebutton:
            idle "gui/menu/btn_acerca_de.png"
            hover "gui/menu/btn_acerca_de_hover.png"
            hover_sound hover_purr
            action ShowMenu("about")
            at btn_hover_anim

        # Fila 3
        imagebutton:
            idle "gui/menu/btn_ayuda.png"
            hover "gui/menu/btn_ayuda_hover.png"
            hover_sound hover_purr
            action ShowMenu("help")
            at btn_hover_anim

        imagebutton:
            idle "gui/menu/btn_salir.png"
            hover "gui/menu/btn_salir_hover.png"
            hover_sound hover_purr
            action Quit(confirm=False)
            at btn_hover_anim

    # Título y versión (opcional, si lo quieres en el menú principal)
    if gui.show_name:
        vbox:
            xalign 0.5 yalign 0.1 spacing 10
            text "[config.name!t]":
                size 60 color "#ffffff" outlines [(4, "#000000", 0, 0)]
            text "[config.version]":
                size 30 color "#dddddd"

# =============================================
# Menú de navegación (usado en game_menu, load, preferences, etc.)
# =============================================
screen navigation():
    vbox:
        style_prefix "nav"
        xalign 0.02
        yalign 0.5
        spacing 10

        textbutton _("Volver") action Return()
        textbutton _("Guardar") action ShowMenu("save")
        textbutton _("Cargar") action ShowMenu("load")
        textbutton _("Opciones") action ShowMenu("preferences")
        textbutton _("Acerca de") action ShowMenu("about")
        textbutton _("Ayuda") action ShowMenu("help")
        textbutton _("Salir") action Quit(confirm=not main_menu)

# Estilos básicos para navigation (puedes mover a screens.rpy si prefieres globales)
style nav_vbox:
    xsize 300

style nav_button:
    size_group "navigation"
    padding (10, 5)
    xalign 0.0

style nav_button_text:
    color "#ffffff"
    hover_color "#ff69b4"  # rosa gatuno
    size 28

style main_menu_grid:
    variant "small"
    xspacing 40
    yspacing 20