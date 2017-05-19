import pygame
import math
import sys
import random

screen_size = (width, height) = (1300 ,500)

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0) 
GREEN = (0, 255, 0)
GREY = (95,95,95)
RED = (255, 0 ,0)
g = 9.81

class Arciere (pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Arciere, self).__init__()   #costruttore
		self.sprite_sheet = pygame.image.load(filename).convert()
		self.image = pygame.Surface((width, height))
		self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
		self.image.set_colorkey(GREY)
		self.rect = self.image.get_rect()

	def movimento_destra(self):
		self.rect.x +=10
		
	def movimento_sinistra(self):
		self.rect.x -=10

class Block(pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Block, self).__init__()   #costruttore
		
		self.sprite_sheet = pygame.image.load(filename).convert()

		self.image = pygame.Surface((width, height))
                self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
		self.image.set_colorkey(GREY) 
		self.v = 14
		self.alpha = 0.15
		self.rect = self.image.get_rect()
		self.t= 0
	def aumenta (self):
		self.v +=1
	def diminuisce(self):
		self.v -=1
	def angolo_su(self):
		self.alpha += 0.03
	def angolo_giu(self):
		self.alpha -= 0.03
	def reset_pos(self):
		self.rect.y = height/1.6
		self.rect.x = arciere.rect.x
                self.t = 0
	

	def update(self):
                self.t += 1./20.
                self.rect.x += self.v * math.cos(self.alpha)
                self.rect.y -= -(0.15*g*self.t) + self.v * math.sin(self.alpha)
		if self.rect.x  < 10 :
			self.reset_pos()


class Torre (pygame.sprite.Sprite):
        def __init__(self, filename,  width, height):
                super(Torre, self).__init__()   #costruttore
                
                self.sprite_sheet = pygame.image.load(filename).convert()
                self.image = pygame.Surface((width, height))
                self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
               
                self.image.set_colorkey(GREY)
                self.rect = self.image.get_rect()

class Bomba (pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Bomba, self).__init__()   #costruttore
               
		self.sprite_sheet = pygame.image.load(filename).convert()
		self.image = pygame.Surface((width, height))
		self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
               
		self.image.set_colorkey(GREY)
		self.rect = self.image.get_rect()
		self.v = 14
		self.alpha = 0.15
		self.t=0
	def pos(self):
		self.rect.x += random.randint(-10,-5)
		self.rect.y += random.randint(-1,0)
	def update_pos(self):
		self.t += 1./20.
		self.rect.x += self.v * math.cos(self.alpha)
		self.rect.y -= -(0.15*g*self.t) + self.v * math.sin(self.alpha)
		if self.rect.x <10:
			self.pos()
		

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bello")

clock = pygame.time.Clock()

sfondo = pygame.image.load("sfondo.jpg").convert()

block_list = pygame.sprite.Group()
arciere_list = pygame.sprite.Group()
torre_list = pygame.sprite.Group()
torre_morta_list = pygame.sprite.Group()
bomba_list=pygame.sprite.Group()

torre= Torre("Torreepng.png",133, 204)
torre.rect.x = 1150
torre.rect.y = height/1.95

block = Block("rect4138.png",162, 46)
block.rect.x = 0
block.rect.y = (height/1.7)

arciere = Arciere("arcier.png", 140,185)
arciere.rect.x = 0
arciere.rect.y = (height/1.7)

bomba = Bomba("bombaa.png", 78, 70)
bomba.rect.x = random.randrange(100, 500)
bomba.rect.y = random.randrange(100, 500)

torre_morta= Torre("Torreemorta.png", 133, 204)






print bomba.rect.y
#torre_morta.rect.x = 1150
#torre_morta.rect.y = height/1.95


block_list.add(block)
arciere_list.add(arciere)
torre_list.add(torre)
torre_morta_list.add(torre_morta)

font =pygame.font.SysFont(None, 60)
font2 =pygame.font.SysFont(None, 150)

vita = 20
done = False
spara = False
score= 0
capoccia= 20

def score(message, color):
	text = font.render(message, True, color)
	screen.blit(text, (1200, 460))

	pygame.draw.rect(screen, (RED), (1100,(height/2.3),capoccia,20))
def win(message, color):
	text = font2.render(message, True, color)
	screen.blit(text, (450, 300))


	
while not done :
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN :
			if event.key ==  pygame.K_UP:
				block.aumenta()
			if event.key ==  pygame.K_DOWN:
				block.diminuisce()
			if event.key == pygame.K_LEFT:
				block.angolo_su()
			if event.key == pygame.K_RIGHT:
				block.angolo_giu()
			if event.key == pygame.K_a:
				arciere.movimento_sinistra()
				block.update()
			if event.key == pygame.K_d:
				arciere.movimento_destra()
				block.update()
			if event.key == pygame.K_SPACE:
		        	block.reset_pos()
		        	spara = True
	if capoccia <=50:
		bomba.pos()
		bomba.update_pos()	
	if block.rect.x < 0: 
		spara = False
	
	hit_list = pygame.sprite.spritecollide(block, torre_list, False)
    	for hit in hit_list:
        	vita -= 1
		if vita <1478 :
			capoccia -= 1
        		score(str(vita), WHITE)
	if capoccia <= 0:
		
		arciere_list.update()
        	torre_morta_list.update()
		screen.blit(sfondo,(0,0))
		arciere_list.draw(screen)
		torre_morta_list.draw(screen)
		score(str(vita), WHITE)
		torre_morta.rect.x = 1150
		torre_morta.rect.y = height/1.95
		torre_morta_list.draw(screen)
		if spara == True :
			block_list.update()
			block_list.draw(screen)
		score(str(vita), WHITE)
		win("VITTORIA", RED)
		#pygame.draw.rect(screen, (GREY), (1100,(height/2.3),capoccia, 20))
	else:

		#arciere.rect.x = 0
		#arciere.rect.y = (height/1.7)
		arciere_list.update()
		torre_list.update()
		block_list.update()
		bomba_list.update()
		screen.blit(sfondo,(0,0))
		arciere_list.draw(screen)
		block_list.draw(screen)
		torre_list.draw(screen)
		bomba_list.draw(screen)
		score(str(vita), WHITE)
		
        #hit.reset_pos()
	
	
	pygame.display.flip()
	clock.tick(30)

print ("Hai vinto")
pygame.quit()
