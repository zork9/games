
# Copyright (C) Johan Ceuppens 2010-2013
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
from tilesurface import *
from tilesurfacerbase import *

class TileSurfacer(TileSurfacerBase):
    ""
    def __init__(self):
        TileSurfacerBase.__init__(self)
	### tile wdith and height
	self.tilew = 16
	self.tileh = 16
	### number of tiles from left to right on the tilesheet
	self.surfacesw = 20 
	### number of tiles up to down on the tilesheet 
	self.surfacesh = 20 
	self.surfaces = []
	for y in range(0,self.surfacesh):
		for x in range(0,self.surfacesw):
			self.surfaces.append(None)

        self.tilesimage = pygame.image.load("./pics/tilesheet1.bmp").convert()
	self.splitintosurfaces()

	### FIX surface.get_bounding_rect
    def splitintosurfaces(self):
	pxarray = pygame.PixelArray(self.tilesimage)

	xoff = 0
	yoff = 0

	for y in range(0,self.surfacesh):
		xoff = 0
		for x in range(0,self.surfacesw):
			surface = pygame.Surface((self.tilew,self.tileh))
			k = 0
			l = 0
			surfacepxarray = pygame.PixelArray(pygame.Surface((self.tilew,self.tileh))) 
			for i in range(0+yoff,self.tileh+yoff-1):
				k = 0
				for j in range(xoff+0,xoff+self.tilew-1):
					surfacepxarray[k,l] = pxarray[j,i]
					k += 1
				l += 1
			self.surfaces[y*self.surfacesw+x] = surfacepxarray
			self.tiles.append(TileSurface(self.x+xoff+self.bgoffsetx,self.y+yoff+self.bgoffsety,0,0,self.tilew,self.tileh,x+self.tilew*y,self.surfaces[y*self.surfacesw+x].make_surface())) 
			xoff += self.tilew
		yoff += self.tileh


	### FIX remove
    def getid(self,xx,yy):
	for tile in self.tiles:
		if xx > tile.x and xx < tile.x+self.tilew and yy > tile.y and yy < tile.y+self.tileh:
			### print "tile.id = %s" % tile.id	
			return tile.id
		else:
			1 ### print "click tileboxx=%d tileboxy=%d tilex=%d tiley=%d" % (self.x,self.y,self.x+tile.x, self.y+tile.y)
				
	### FIX remove
    def get(self,xx,yy):
	for tile in self.tiles:
		if xx > tile.x and xx < tile.x+self.tilew and yy > tile.y and yy < tile.y+self.tileh:
			print "tile.id = %s" % tile.id	
			return tile
		else:
			1 ### print "click tileboxx=%d tileboxy=%d tilex=%d tiley=%d" % (self.x,self.y,self.x+tile.x, self.y+tile.y)
	return None

	### FIX remove
    def getwithid(self,id):
	for tile in self.tiles:
		if tile.id == id:
			### print "getwithid : tile.id = %s" % tile.id	
			return tile
		else:
			1 ### print "click tileboxx=%d tileboxy=%d tilex=%d tiley=%d" % (self.x,self.y,self.x+tile.x, self.y+tile.y)
	return None

    def getimage(self, id):
	for tile in self.tiles:
		if tile.id == id:
			return tile.surface
	return None
