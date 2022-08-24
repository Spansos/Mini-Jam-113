import pygame as pg
import random as rnd
from . import prepare, rpg

class Event:
    events = []
    event_names = []
    cur_mail = None
    def __init__(self, textbox, condition):
        self.textbox = textbox
        self.condition = condition
        Event.events.append(self)
        Event.event_names.append(self.textbox.title)
    
    
    
def get_pos_events(data):
    events = []
    for ev in Event.events:
        if ev.condition(data):
            events.append(ev)
    return events

title = "A New Dungeon"
text  = "We could slow down the hero by \nluring him into a dungeon.\nHowever, we'd need something\nto lure him with."
def opt1(data):
    Event.cur_mail = None
    data['hero_equip'] = data['hero_equip'] + 1
    data['days'] += rnd.randint(4, 8)
opt1 = rpg.Option('Lure him with equipment', opt1)
def opt2(data):
    Event.cur_mail = None
    data['gold'] -= 4
    data['days'] += rnd.randint(4, 8)
opt2 = rpg.Option('Lure him with gold', opt2)
def opt3(data):
    Event.cur_mail = None
opt3 = rpg.Option('Do nothing', opt3)
def cond(data):
    if data['gold'] < 10:
        return False
    if data['hero_equip'] >= 3:
        return False
    return True
Event(rpg.Textbox(title, text, (opt1, opt2, opt3)), cond)

title = "Bribing A Friend"
text  = "A friend of the hero seems to\nbe open to bribes.\nShould we try to bribe him?"
def opt1(data):
    Event.cur_mail = None
    data['gold'] -= 6
    data['hero_equip'] -= 1
opt1 = rpg.Option('Make him destroy equipment', opt1)
# def opt2(data):
#     data['gold'] -= 10
#     data['days'] += rnd.randint(4, 8)
# opt2 = rpg.Option('Lure him with gold', opt2)
def opt3(data):
    Event.cur_mail = None
opt3 = rpg.Option('Do nothing', opt3)
def cond(data):
    if data['gold'] < 6:
        return False
    if data['hero_equip'] <= 0:
        return False
    return True
Event(rpg.Textbox(title, text, (opt1, opt3)), cond)

title = "Donations"
text  = "Various local pro-villain\norganisations have send in\ndonations for your cause."
def opt1(data):
    Event.cur_mail = None
    data['gold'] += rnd.randint(4, 8)
opt1 = rpg.Option('Naturally.', opt1)
# def opt2(data):
#     data['gold'] -= 10
#     data['days'] += rnd.randint(4, 8)
# opt2 = rpg.Option('Lure him with gold', opt2)
# def opt3(data):
#     pass
# opt3 = rpg.Option('Do nothing', opt3)
def cond(data):
    if data['gold'] > 32:
        return False
    if rnd.randint(0, 1):
        return False
    return True
Event(rpg.Textbox(title, text, (opt1,)), cond)

title = "A Business Investment"
text  = "Some businesses on the road \nthe hero will take have\noffered to take your side for\na small investment"
def opt1(data):
    Event.cur_mail = None
    data['gold'] -= 3
    data['days'] += rnd.randint(1, 3)
opt1 = rpg.Option('Use them to hinder the hero', opt1)
def opt2(data):
    Event.cur_mail = None
    data['gold'] += rnd.randint(-1, 3)
opt2 = rpg.Option('Try to use them for profit', opt2)
def opt3(data):
    Event.cur_mail = None
opt3 = rpg.Option('Do nothing', opt3)
def cond(data):
    if data['gold'] < 6:
        return False
    return True
Event(rpg.Textbox(title, text, (opt1, opt2, opt3)), cond)

title = "Equipment Upgrade"
text  = "A blacksmith is offering\nhis services."
def opt1(data):
    Event.cur_mail = None
    data['gold'] -= 5
    data['player_equip'] += 1
opt1 = rpg.Option('Commission better equipment', opt1)
# def opt2(data):
#     data['gold'] += rnd.randint(-1, 3)
# opt2 = rpg.Option('Try to use them for profit', opt2)
def opt3(data):
    Event.cur_mail = None
opt3 = rpg.Option('Do nothing', opt3)
def cond(data):
    if data['gold'] < 5:
        return False
    if data['player_equip'] >= 3:
        return False
    return True
Event(rpg.Textbox(title, text, (opt1, opt3)), cond)