import pygame
import math

class HP_BAR:
	def __init__(self, screen, SCREEN_W, SCREEN_H, rect_hp, lose_hp_percent, inside_rect_w, damage_taked):
		super().__init__()

		self.screen = screen
		self.SCREEN_W = SCREEN_W
		self.SCREEN_H = SCREEN_H
		self.rect_hp = rect_hp
		self.lose_hp_percent = lose_hp_percent
		self.inside_rect_w = inside_rect_w
		self.damage_taked = damage_taked

		self.rect = pygame.Rect(0, 0, 300, 30)
		self.rect.topright = (self.SCREEN_W - 15, 15)

		self.inside_rect = pygame.Rect(0, 0, self.inside_rect_w, 20)
		self.inside_rect.left = self.rect.left + 5
		self.inside_rect.bottom = self.rect.bottom - 5

		self.font = pygame.font.Font(None, 15)
		self.hp_surface = self.font.render(f"{self.rect_hp}", True, (255,255,255))
		self.hp_rect = self.hp_surface.get_rect(center = self.rect.center)

	def reduce_hp_bar(self, changing_limit):
		if self.damage_taked:
			self.inside_rect_w = self.inside_rect_w - (self.inside_rect_w * self.lose_hp_percent)

		if changing_limit:
			self.inside_rect_w = 290


	def draw(self):
		pygame.draw.rect(self.screen, (255,0,0), self.inside_rect, 0, 5)
		pygame.draw.rect(self.screen, (255,255,255), self.rect, 5, 5)
		self.screen.blit(self.hp_surface, self.hp_rect)


	
	def update(self,changing_limit):
		self.reduce_hp_bar(changing_limit)
		self.draw()





















