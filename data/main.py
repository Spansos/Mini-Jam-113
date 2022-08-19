import pygame as pg
from . import prepare


def main():
    screen = pg.display.get_surface()
    cube = pg.Surface((32, 32))
    cube.fill((100, 100, 100))
    
    while True:
        act_dict = update()
        render(screen)
        
        if act_dict['quit']:
            break

def render(screen: pg.Surface) -> None:
    screen.fill(prepare.BG_COL)
    pg.display.update(screen)


def update() -> dict:
    act_dict = {'quit': False}
    
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            act_dict['quit'] = True
            
    return act_dict