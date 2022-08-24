import pygame as pg
from . import prepare, entities, rpg

DATA_TO_UI = {'player_equip':'player level', 'hero_equip': 'hero level', 'days': 'days left', 'gold': 'gold'}
FONT = pg.font.Font("resources/PressStart2P.ttf", 8)

def render(screen: pg.Surface, data) -> None:
    screen.fill(prepare.BG_COL)
    
    screen.blit(prepare.RESOURCES['world.png'], -data['cam'])
    for en in entities.Entity.entities:
        en.render(screen, data)
    if rpg.Textbox.current:
        rpg.Textbox.current.render(screen)
    for i, (k, v) in enumerate(DATA_TO_UI.items()):
        screen.blit(FONT.render(f"{v}: {data[k]}", False, (255,255,255), (0,0,0)), (0, i*FONT.get_linesize()))