import pygame as pg
from . import prepare, entities, rpg


def render(screen: pg.Surface, data) -> None:
    screen.fill(prepare.BG_COL)
    
    screen.blit(prepare.RESOURCES['world.png'], -data['cam'])
    for en in entities.Entity.entities:
        en.render(screen, data)
    if rpg.Textbox.current:
        rpg.Textbox.current.render(screen)