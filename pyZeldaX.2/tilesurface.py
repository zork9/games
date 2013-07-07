
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from types import *
from time import *

class TileSurface:
    ""
    def __init__(self,xx,yy,relx,rely,ww,hh,id,surface):
	self.tiles = []
	self.id = id
        self.surface = surface 

	self.x = xx
	self.y = yy
	self.relativex = relx
	self.relativey = rely
	self.w = ww
	self.h = hh

    def draw(self,screen):
	### FIX make_surface
        ### FIX screen.blit(self.surface.make_surface(), (0+self.x, 0+self.y))
        screen.blit(self.surface, (0+self.x, 0+self.y))
	
