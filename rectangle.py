import pygame
import math

class Rectangle:
	def __init__(self, screen, SCREEN_W, SCREEN_H, bullets, bullet_damage, rect_hp, rectangle_red, rectangle_green, rectangle_blue):
		super().__init__()

		self.screen = screen
		self.bullets = bullets
		self.bullet_damage = bullet_damage
		self.damage_taked = False
		self.SCREEN_W = SCREEN_W
		self.SCREEN_H = SCREEN_H

	
		self.rect = pygame.Rect(0, 0, 300, 300)
		self.rect.centerx, self.rect.centery = (SCREEN_W / 2) + 300, (SCREEN_H / 2)
		self.rect_colour = (rectangle_red,rectangle_green,rectangle_blue)

		self.rect_hp = rect_hp
		try:
			self.lose_hp_percent = self.bullet_damage / self.rect_hp
		except ZeroDivisionError:
			self.lose_hp_percent = 0

	def take_damage(self):
		for bullet in self.bullets:
			if self.rect.collidepoint(bullet[0]) and not(self.rect_hp <= 0):
				self.bullets.pop(0)
				self.rect_colour = (255,255,255)
				
				self.rect_hp = int(self.rect_hp - (self.rect_hp * self.lose_hp_percent))
				self.damage_taked = True

			if bullet[0][0] > self.SCREEN_W:
				self.bullets.pop(0)

	

	def hp_min(self):
		if self.rect_hp < 0:
			self.rect_hp = 0

	def draw(self):
		if not self.rect_hp <= 0:
			pygame.draw.rect(self.screen, self.rect_colour, self.rect, 0, 0)

	def update(self):
		self.take_damage()
		self.hp_min()
		self.draw()


