import pygame as pg
import math
from . import prepare, rpg

class Entity:
    entities = []
    def __init__(self) -> None:
        Entity.entities.append(self)
        self.pos = pg.Vector2(0,0)
        self.vel = pg.Vector2(0, 0)
        self.size = (12, 12)
        self.rect = pg.Rect(self.pos, self.size)
        self.stretch = 1
    
    def render(self, screen: pg.Surface, data) -> None:
        pg.draw.rect(screen, (255,255,255), (self.pos-data['cam'], self.size))
    
    def move(self, vec, data):
        self.pos.x += vec[0]
        self.rect.topleft = self.pos
        
        collide_rects_x = self.rect.collidelistall(data['world']['collisions'])
        for i in collide_rects_x:
            colliderect = pg.Rect(data['world']['collisions'][i])
            if vec.x > 0:
                self.rect.right = colliderect.left
            else:
                self.rect.left = colliderect.right
            self.pos.x = self.rect.left
                
        self.pos.y += vec[1]
        self.rect.topleft = self.pos
        
        collide_rects_y = self.rect.collidelistall(data['world']['collisions'])
        for i in collide_rects_y:
            colliderect = pg.Rect(data['world']['collisions'][i])
            if vec.y > 0:
                self.rect.bottom = colliderect.top
            else:
                self.rect.top = colliderect.bottom
            self.pos.y = self.rect.top
        
        return collide_rects_x + collide_rects_y
    
    def update(self, data):
        colliderects = self.move(self.vel, data)
        self.vel *= .75
        self.stretch = (self.stretch - 1) * .8 + 1
        return colliderects


class Player(Entity):
    player = None
    player_png = prepare.RESOURCES['player.png']
    stages = []
    for i in range(4):
        sub_png = pg.Surface((16, 16))
        sub_png.blit(player_png, (0,0), (i*16, 0, 16, 16))
        sub_png.set_colorkey((255, 0, 255))
        stages.append(sub_png)
    
    def __init__(self):
        if Player.player:
            raise Exception("A player already exists")
        super().__init__()
        Player.player = self
        self.stage = 0
    
    def update(self, data):
        colliderects = super().update(data)
        for i in colliderects:
            if tuple(data['world']['collisions'][i]) == (144, 0, 16, 16): # hit door
                if not rpg.Textbox.current:
                    rpg.end_day_dialogue()
        if rpg.Textbox.current and rpg.Textbox.current.title == 'Your Chambers' and not self.rect.colliderect((144, 16, 16, 16)):
            rpg.Textbox.current = None
        
        d_v = pg.Vector2(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            d_v.y -= 1
        if keys[pg.K_a]:
            d_v.x -= 1
        if keys[pg.K_s]:
            d_v.y += 1
        if keys[pg.K_d]:
            d_v.x += 1
        if d_v:
            d_v.normalize_ip()
            d_v *= .6
        self.vel += d_v
    
        grid_pos = pg.Vector2(
            self.rect.centerx // prepare.SCREEN_DIMS[0],
            self.rect.centery // prepare.SCREEN_DIMS[1]
            )
        cam_pos = pg.Vector2(
            grid_pos.x * prepare.SCREEN_DIMS[0],
            grid_pos.y * prepare.SCREEN_DIMS[1]
            )
        data['cam'] = cam_pos
    
    
    def render(self, screen, data):
        surf = Player.stages[self.stage]
        
        bobble_magnitute = self.vel.length() * 12
        
        stretch_surf = pg.transform.scale(surf, (16, 16*(self.stretch)))
        rot_stretch_surf = pg.transform.rotate(stretch_surf, bobble_magnitute*math.sin(data['tick']/(2*math.pi)))
        
        d_size = pg.Vector2(rot_stretch_surf.get_size()) - surf.get_size()
        d_size.y -= (self.stretch - 1) * 16
        d_size2 = pg.Vector2(self.size) - surf.get_size()
        screen.blit(rot_stretch_surf, self.pos-data['cam']-d_size/2 + d_size2/2)