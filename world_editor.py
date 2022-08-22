import pygame as pg
import json

world = pg.image.load('resources/world.png')
screen = pg.display.set_mode(world.get_size(), pg.SCALED|pg.RESIZABLE)

col_posses = []
end_json = {}
running = True
while running:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
            
    m_pos = pg.mouse.get_pos()
    g_pos = (m_pos[0] // 16, m_pos[1] // 16)
    r_pos = (g_pos[0] * 16,  g_pos[1] * 16)
    
    if pg.mouse.get_pressed()[0]:
        if r_pos not in col_posses:
            col_posses.append(r_pos)
    if pg.mouse.get_pressed()[2]:
        if r_pos in col_posses:
            col_posses.remove(r_pos)
    
    screen.fill((0,0,0))
    screen.blit(world, (0,0))
    for r in col_posses:
        pg.draw.rect(screen, (155, 0, 0), (r, (16, 16)))
    pg.display.update()

col_rects = []
for i in col_posses:
    col_rects.append((i[0], i[1], 16, 16))


end_json['collisions'] = col_rects

with open('resources/world.json', 'w') as file:
    write_json = json.dumps(end_json)
    file.write(write_json)