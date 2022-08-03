import pygame as pg
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox
from crt_shader import Graphic_engine

class Multi_window:
    def __init__(self, shader = False):
        self.has_shader = shader
        # self.win = Window.from_display_module()
        self.screen = pg.Surface((800, 600)).convert((255, 65280, 16711680, 0))
        self.img = pg.image.load('data/image.png')
        self.img_rect = self.img.get_rect()
        self.screen.blit(self.img, self.img_rect)
        if self.has_shader:
            pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
            self.shader = Graphic_engine(self.screen)
            self.win = Window.from_display_module()
        else:
            # win = Window("asdf", resizable=True)
            self.win = Window('test',(800, 600), fullscreen= False, resizable = True)
            self.renderer = Renderer(self.win)
            self.tex = Texture.from_surface(self.renderer, self.screen)
    
    def blit(self):
        self.screen.blit(self.img, self.img_rect)
        if self.has_shader:
            self.shader.render()
        else:
            self.tex = Texture.from_surface(self.renderer, self.screen)
            self.renderer.clear()
            self.renderer.blit(self.tex)
            self.renderer.present()