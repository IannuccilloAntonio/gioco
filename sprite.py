import pygame
import math
import sys
import random , time

screen_size = (width, height) = (900 ,500)

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0) 
GREEN = (0, 255, 0)
GREY = (95,95,95)
RED = (255, 0 ,0)
g = 9.81
speed = 5
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
		
	def pos(self):
		self.rect.x = arciere.rect.x
		self.rect.y = arciere.rect.y-300
	def update_pos(self):
		
		self.rect.y += speed 
		if self.rect.y >500:
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
torre.rect.x = 750
torre.rect.y = height/1.95

block = Block("rect4138.png",162, 46)
block.rect.x = 0
block.rect.y = (height/1.7)

arciere = Arciere("arcier.png", 140,185)
arciere.rect.x = 0
arciere.rect.y = (height/1.7)

bomba = Bomba("capoccia.png", 85, 91)
bomba.rect.x = 0
bomba.rect.y = height

torre_morta= Torre("Torreemorta.png", 133, 204)


print bomba.rect.y
#torre_morta.rect.x = 1150
#torre_morta.rect.y = height/1.95


block_list.add(block)
arciere_list.add(arciere)
torre_list.add(torre)
torre_morta_list.add(torre_morta)
bomba_list.add(bomba)

font =pygame.font.SysFont(None, 60)
font2 =pygame.font.SysFont(None, 150)

vita = 50
#done = False
#spara = False
#capoccia= 50
#amico = 20
#capoccia2= 20
gioca = True
def score(message, color):
	text = font.render(message, True, color)
	screen.blit(text, (750, 460))

	pygame.draw.rect(screen, (RED), (750,(height/2.3),capoccia,20))
	pygame.draw.rect(screen, (RED), (arciere.rect.x,(arciere.rect.y-20),capoccia2,20))
def win(message, color):
	text = font2.render(message, True, color)
	screen.blit(text, (450, 300))
def lost(message, color):
	text = font2.render(message, True, color)
	screen.blit(text, (450, 300))


while gioca :
	vita = 50
	done = False
	spara = False
	score= 0
	capoccia= 50
	amico = 20
	capoccia2= 20
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
			
		if spara == True :
			bomba.update_pos()
				
		if block.rect.x < 0: 
			spara = False
		hit_list = pygame.sprite.spritecollide(bomba, arciere_list, False)
		for hit in hit_list:
			amico -= 1
			print amico
			if amico < 0 :
				screen.blit(sfondo,(0,0))
				score(str(vita), WHITE)
				lost("GAME OVER",RED)
				done = True
				gioca = False
		hit_list = pygame.sprite.spritecollide(block, torre_list, False)
		for hit in hit_list:
			vita -= 1
			
			if vita < 1478 :
				capoccia -= 1
				screen.blit(sfondo,(0,0))
        		score(str(vita), WHITE)
		arciere_list.update()
		torre_list.update()
		block_list.update()
		bomba_list.update()
		screen.blit(sfondo,(0,0))
		arciere_list.draw(screen)
		block_list.draw(screen)
		torre_list.draw(screen)
		bomba_list.draw(screen)
		
		if capoccia <= 0:
			arciere_list.update()
			torre_morta_list.update()
			screen.blit(sfondo,(0,0))
			arciere_list.draw(screen)
			torre_morta_list.draw(screen)
			score(str(vita), WHITE)
			torre_morta.rect.x =  750
			torre_morta.rect.y = height/1.95
			torre_morta_list.draw(screen)
			win("VITTORIA", RED)
			block_list.update()
			block_list.draw(screen)
			score(str(capoccia), WHITE)		
		
		
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN :
				if event.key ==  pygame.K_y:
					gioca = True
				if event.key ==  pygame.K_n:
					gioca = False
	pygame.display.flip()
	clock.tick(30)
print ("Hai vinto")
time.sleep(4)
pygame.quit()
