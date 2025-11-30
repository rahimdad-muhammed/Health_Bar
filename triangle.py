import pygame
import math

class Triangle:
	def __init__(self, screen, SCREEN_W, SCREEN_H, shout, bullets, bullet_damage, triangle_red, triangle_green, triangle_blue):
		super().__init__()

		self.screen = screen
		self.SCREEN_W = SCREEN_W
		self.SCREEN_H = SCREEN_H

		self.triangle = {
			"color" : (triangle_red,triangle_green,triangle_blue),
			"head" : pygame.Vector2((SCREEN_W / 2) - 230, (SCREEN_H / 2)),
			"back1" : pygame.Vector2((SCREEN_W / 2) - 300, (SCREEN_H / 2) + 30),
			"back2" : pygame.Vector2((SCREEN_W / 2) - 300, (SCREEN_H / 2) - 30)
			}


		self.bullets = bullets
		self.shout = shout
		self.bullet_damage = bullet_damage

		# triangle color
		self.triangle_red = triangle_red
		self.triangle_green = triangle_green
		self.triangle_blue = triangle_blue


	def beam(self):
		if self.shout:
			self.bullets.append([
				pygame.Vector2((self.SCREEN_W / 2) - 230, (self.SCREEN_H / 2)),
				pygame.Vector2((self.SCREEN_W / 2) - 245, (self.SCREEN_H / 2) + 5),
				pygame.Vector2((self.SCREEN_W / 2) - 245, (self.SCREEN_H / 2) - 5)
				])

			self.shout = False

		for bullet in self.bullets:
			bullet[0].x += 10
			bullet[1].x += 10
			bullet[2].x += 10



	def draw(self):
		pygame.draw.polygon(self.screen, self.triangle["color"], [self.triangle["head"], self.triangle["back1"], self.triangle["back2"]])
		
		for bullet in self.bullets:
			pygame.draw.polygon(
				self.screen,
				(self.triangle_red,self.triangle_green,self.triangle_blue),
				bullet
				)
			



	

	def update(self):
		self.beam()
		self.draw()


















		