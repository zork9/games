#!/usr/local/bin/python
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
from playerlink import *
from tileroom1 import *

class Game:
	"Main function"
	def __init__(self):
		pygame.init()
		pygame.font.init()
		pygame.key.set_repeat(10,100)
		self.screen = pygame.display.set_mode((640, 480))
		self.font = pygame.font.SysFont("Times", 32)
       
	def titleloop(self):
		blankimage = pygame.image.load('./pics/blank.bmp').convert()
		titleimage = pygame.image.load('./pics/titlescreen1.bmp').convert()
        
###        self.room = MaproomTown1(0,0)
###        self.manameter = ManaMeter(0,0)
###        self.lifemeter = LifeMeter(250,0)
###        self.player = PlayerLink(lifemeter,manameter)
		self.player = PlayerLink()
	     
		terminate = 0
		while terminate == 0:
			pygame.display.update()
			self.screen.blit(titleimage, (0,0))
			for event in pygame.event.get():
				if event.type == KEYUP or event.type == pygame.MOUSEBUTTONUP:
					terminate = 1

	def mainloop(self): 
		blankimage = pygame.image.load('./pics/blank.bmp').convert()
		self.room = Tileroom1(0,0,0,0)

		terminate = 0
		while terminate == 0:
			self.screen.blit(blankimage, (0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					terminate = 1
				if event.type == KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    			if event.key == K_DOWN:
						self.player.movedown(self.room)	
                    			elif event.key == K_UP:
						self.player.moveup(self.room)	
                    			elif event.key == K_LEFT:
						self.player.moveleft(self.room)	
                    			elif event.key == K_RIGHT:
						self.player.moveright(self.room)
				elif event.type == KEYUP:
					self.player.stopmove()

			self.room.draw(self.screen)
			self.player.draw(self.screen)
			pygame.display.update()

	def setxy(self,xx,yy):
		self.x = xx
		self.y = yy

###    def chooseroom(self, roomnumber,font):
            
if __name__ == "__main__":
    foo = Game()
    foo.titleloop()
    foo.mainloop()


