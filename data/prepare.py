import pygame as pg
import os

pg.init()


# vars for later use
SCREEN_DIMS = (304, 208)
CAPTION = "Temp Name"
SCREEN_RECT = pg.Rect((0, 0), SCREEN_DIMS)
BG_COL = (20, 30, 35)


# make and set screen
ICON = pg.Surface((32, 32))
pg.display.set_caption(CAPTION)
pg.display.set_icon(ICON)
_screen = pg.display.set_mode(SCREEN_DIMS, pg.SCALED|pg.RESIZABLE)


# loading screan
_screen.fill(BG_COL)
_render = pg.font.SysFont("Arial", 48).render("Loading...", False, pg.Color("white"))
_screen.blit(_render, _render.get_rect(center=SCREEN_RECT.center))
pg.display.update()



#loads graphic things
TILE_SIZE = (32, 32)

RESOURCES = {}
for file in os.listdir("resources"):
    name, ext = file.split('.')
    if ext == 'png':
        RESOURCES[file] = pg.image.load(os.path.join("resources", file)).convert()