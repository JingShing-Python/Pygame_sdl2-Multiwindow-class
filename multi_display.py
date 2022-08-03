import pygame as pg
from window_class import Multi_window

running = True

x, y = 250, 50
clock = pg.time.Clock()

pg.init()
win1 = Multi_window(True)
win2 = Multi_window()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif getattr(event, "window", None) == win1.win:
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                or event.type == pg.WINDOWCLOSE):
                running = False
        elif getattr(event, "window", None) == win2.win:
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                or event.type == pg.WINDOWCLOSE):
                running = False

    win1.blit()
    win2.blit()

    clock.tick(60)

pg.quit()