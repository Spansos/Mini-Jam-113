import pygame as pg
import random as rnd
from . import prepare, entities, render

class Option:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    
    def choose(self, data):
        self.func(data)

class Textbox:
    current = None
    title_font = pg.font.Font("resources/8-BIT WONDER.ttf", 8)
    text_font = pg.font.Font("resources/PressStart2P.ttf", 8)
    def __init__(self, title, text, options):
        self.title = title
        self.text = text
        self.options = options
        self.size = pg.Vector2((prepare.SCREEN_DIMS[0]/1.25, prepare.SCREEN_DIMS[1]/2.5))
        
        self.rendered = pg.Surface(self.size)
        
        rendered_title = Textbox.title_font.render(self.title, False, (255, 255, 255), (0, 0, 0))
        self.rendered.blit(rendered_title, (0, 0))
        
        text_size = (self.size[0], self.size[1] - rendered_title.get_height() - 4)
        rendered_text = pg.Surface(text_size)
        for i, v in enumerate(self.text.split('\n')):
            rendered_line = Textbox.text_font.render(v, False, (255, 255, 255), (0, 0, 0))
            rendered_text.blit(rendered_line, (0, i*rendered_line.get_height()))
        self.rendered.blit(rendered_text, (0, rendered_title.get_height() + 4))
        
        rendered_options = pg.Surface((self.size[0], len(self.options) * Textbox.text_font.get_linesize()))
        for i, v in enumerate(options):
            rendered_option = Textbox.text_font.render(f"{i+1}: {v.name}", False, (255,255,255), (0,0,0))
            rendered_options.blit(rendered_option, (0, i*Textbox.text_font.get_linesize()))
        self.rendered.blit(rendered_options, (0, self.size.y - rendered_options.get_height()))
            
    def update(self, data):
        l = len(self.options)
        key = None
        for ev in data['events']:
            if ev.type == pg.KEYDOWN:
                key = ev.key
                
        if key == pg.K_1 and l >= 1:
            self.end()
            self.options[0].func(data)
        if key == pg.K_2 and l >= 2:
            self.end()
            self.options[1].func(data)
        if key == pg.K_3 and l >= 3:
            self.end()
            self.options[2].func(data)
    
    def render(self, screen: pg.Surface):
        screen.blit(self.rendered, prepare.SCREEN_RECT.center - self.size/2 + (0, prepare.SCREEN_RECT.height/8))
    
    def end(self):
        Textbox.current = None


def end_day_dialogue():
    opt1 = Option('yes', lambda x: new_day(x, True))
    opt2 = Option('no', lambda x: 0)
    Textbox.current = Textbox('Your Chambers', 'Do you want to go to sleep\nand end the current day?', (opt1, opt2))


def new_day(data, fade):
    from . import events
    
    if events.Event.cur_mail != None:
        opt1 = Option('Acknowledged', lambda x: 0)
        Textbox.current = Textbox('Need To Check Mail', 'You need to check the\nmail before ending the day.', (opt1,))
        return
        
    
    screen = pg.display.get_surface()
    clock = pg.time.Clock()
    if fade:
        for i in range(20):
            clock.tick(60)
            render.render(screen, data)
            screen.fill((255-255*i/20, 255-255*i/20, 255-255*i/20), special_flags=pg.BLEND_RGB_MULT)
            pg.display.update()

    
    data['tick'] = 0
    entities.Player.player.rect.center = (28*16 + 8, 24)
    entities.Player.player.pos = pg.Vector2(entities.Player.player.rect.topleft)
    pos_events = events.get_pos_events(data)
    events.Event.cur_mail = rnd.choice(pos_events)
    data['days'] -= 1
    if data['days'] <= 0:
        entities.Hero()
    
    if fade:
        for i in range(20):
            clock.tick(60)
            render.render(screen, data)
            screen.fill((255*i/20, 255*i/20, 255*i/20), special_flags=pg.BLEND_RGB_MULT)
            pg.display.update()
