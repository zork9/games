
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
from stateimagelibrary import *

class PlayerLink:
    "Player Link"

    def __init__(self):
	###self.lifemeter = lifemeter

	self.CENTERX = 280
	self.CENTERY = 200

        self.x = 281 
        self.y = 300 
        self.w = 48 
        self.h = 48 
	self.stimlibleft = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerlink-left-1-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-left-2-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-left-3-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-left-4-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibleft.addpicture(image)	

	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerlink-right-1-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-right-2-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-right-3-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-right-4-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibright.addpicture(image)	
        self.fightcounter = 0
 
	self.stimlibup = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerlink-up-1-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibup.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-up-2-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibup.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-up-3-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibup.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-up-4-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibup.addpicture(image)	

	self.stimlibdown = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerlink-down-1-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-down-2-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-down-3-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/playerlink-down-4-48x48.bmp').convert()
        image.set_colorkey((0,128,255)) 
	self.stimlibdown.addpicture(image)	


	self.changeplayernumber = None
	self.direction = "stop"

    def moveupdate(self, dx, dy):
	self.x += dx
	self.y += dy


    def stopmove(self):
	self.direction = "stop"

    def moveleft(self,room):
	self.direction = "west"
	if not room.checktoupdate(self):
		self.moveupdate(-5,0)	
	else:	
		room.moveupdate(+5,0)	

    def moveright(self,room):
	self.direction = "east"
	if not room.checktoupdate(self):
		self.moveupdate(+5,0)	
	else:	
		room.moveupdate(-5,0)	

    def moveup(self,room):
	self.direction = "north"
	if not room.checktoupdate(self):
		self.moveupdate(0,-5)	
	else:	
		room.moveupdate(0,+5)	

    def movedown(self,room):
	self.direction = "south"
	if not room.checktoupdate(self):
		self.moveupdate(0,+5)	
	else:	
		room.moveupdate(0,-5)	

    def drawstatic(self, screen):
	self.stimlibdown.drawstatic(screen,self.x,self.y,0)

    def draw(self, screen):
	if self.direction == "south":
        	self.stimlibdown.draw(screen, self.x,self.y)
	elif self.direction == "north":
        	self.stimlibup.draw(screen, self.x,self.y)
	elif self.direction == "west":
        	self.stimlibleft.draw(screen, self.x,self.y)
	elif self.direction == "east":
        	self.stimlibright.draw(screen, self.x,self.y)
	else:
		self.stimlibdown.drawstatic(screen, self.x ,self.y, 0)

