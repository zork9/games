
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

class Tileroom:
    "Room with a tile map"
    def __init__(self,xx,yy,relx,rely):
        # left NOTE : boxes collide so put them after enemies !

	self.x = xx
	self.y = yy

	self.relativex = relx
	self.relativey = rely

	self.tile2 = pygame.image.load('./pics/tile2-grass-1-16x16.bmp').convert()

	self.SCREENWIDTH = 640 
	self.SCREENHEIGHT = 480
	self.MAPWIDTH = 768 
	self.MAPHEIGHT = 1024 
	self.TILEWIDTH = 16 
	self.TILEHEIGHT = 16 
       	#### FIX match lengths of table elements 
	self.tilelist = []

	self.loadmap()

    def moveupdate(self, dx, dy):
	self.x += dx
	self.y += dy

    def draw(self,screen):###player
	###self.update(screen,player)
	for x in range(0, self.MAPHEIGHT / self.TILEHEIGHT):
		for y in range(0, self.MAPWIDTH / self.TILEWIDTH):
			if self.tilelist[y][x] == 120:	
				screen.blit(self.tile2, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))

#	for go in self.tileroomgameobjects:
#		go.update(self,player) ### NOTE every gameobj has this
#		go.draw(screen,self)

    def update(self, screen, player):
	1


    def checktoupdate(self, player):
	return self.checktoupdatex(player) or self.checktoupdatey(player)

    def checktoupdatex(self, player):
	if abs(self.x - player.x) < player.CENTERX:
		return 0
	elif abs(self.MAPWIDTH + self.x) < self.SCREENWIDTH:
		###player.x -= 5
		if player.x > player.CENTERX:
			return 0
		elif player.x <= player.CENTERX:
			return 1
	else:
		return 1

    def checktoupdatey(self, player):
	if abs(self.y - player.y) < player.CENTERY:
		return 0
	elif abs(self.MAPHEIGHT + self.y) < self.SCREENHEIGHT:
		###player.y -= 5
		if player.y > player.CENTERY:
			return 0
		elif player.y <= player.CENTERY:
			return 1
	else:
		return 1

    def isroomdownexit(self):
	###if self.relativex  < -100:
	###	return 1 
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomdownexit():
		self.setxyfromdown()
		return 4 
	return 0 
 
    def collidesword(self,player):
	return None

    def collideswordlow(self,player):
	return None

    def collideup(self,player):
	return None

    def collidewithropes(self,player):
	return None

    def collide(self,player):
	for go in self.tileroomgameobjects:
		if go.collidego(self,player):
			self.undomove()
			return 2	

	r = TileroomBase.collide(self,player)
	# tile 1 
	if r == 2:
		1 #return 2 
	# tile 2 - do not block 
	if r == 2.1:
		1	
	if r == 3.1 or r == 3.2 or r == 3.3 or r == 3.4:
		self.undomove()
		return 2	
	return 0

    def fall(self,player):
	return 2 

    def moveup(self):
	self.direction = "north"
	self.relativey -= 10

    def moveleft(self):
	self.relativex -= 10
	self.direction = "west"
		
    def removeobject(self, o):
        for i in range(0,len(self.tileroomgameobjects)):
            if self.tileroomgameobjects[i] == o:
                self.tileroomgameobjects[i] = None



    def loadmap(self):
	print "tileroom, loadmap() : subclass responsability"	
