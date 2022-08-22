import pygame as pg
import json
from . import prepare, entities, rpg, render


def main():
    screen = pg.display.get_surface()
    entities.Player()
    
    data = {'quit': False, 'cam': pg.Vector2(0,0)}
    
    with open("resources/world.json", 'r') as file:
        world_dict = json.loads(file.read())
    data['world'] = world_dict
    data['tick'] = 0
    
    clock = pg.time.Clock()
    rpg.new_day(data, False)
    while True:
        clock.tick(60)
        
        data = update(data)
        render.render(screen, data)
        pg.display.update(screen)
        
        if data['quit']:
            break
        data['tick'] += 1


def update(data) -> dict:
    player = entities.Player.player
    
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            data['quit'] = True
    
    for en in entities.Entity.entities:
        en.update(data)
    
    
    if rpg.Textbox.current:
        rpg.Textbox.current.update(data)

            
    return data