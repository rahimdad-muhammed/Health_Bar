import pygame
from sys import exit
import math

from triangle import Triangle
from rectangle import Rectangle
from rect_hpBar import HP_BAR
from settings import Settings


class Main:
	def __init__(self):
		super().__init__()
		
		pygame.init()
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		pygame.display.set_caption("Number Sense")
		self.clock = pygame.time.Clock()

		# SCREEN DIMENSIONS
		self.SCREEN_W, self.SCREEN_H = self.screen.get_size()

		# Triangle colors
		self.triangle_red = 250
		self.triangle_green = 0
		self.triangle_blue = 0

		# Rectangle color
		self.rectangle_red = 255
		self.rectangle_green = 255
		self.rectangle_blue = 0

		# Triangle
		self.shout = False
		self.bullets = []
		self.bullet_damage = 500
		self.triangle = Triangle(self.screen, self.SCREEN_W, self.SCREEN_H, self.shout, self.bullets, self.bullet_damage, self.triangle_red, self.triangle_green, self.triangle_blue)


		# Rectangle
		self.rect_hp = 5000
		self.rectangle = Rectangle(self.screen, self.SCREEN_W, self.SCREEN_H, self.bullets,self.rect_hp, self.bullet_damage, self.rectangle_red, self.rectangle_green, self.rectangle_blue)
		self.lose_hp_percent = self.rectangle.lose_hp_percent
		self.damage_taked = self.rectangle.damage_taked

		# HP Bar
		self.inside_rect_w = 290
		self.hp_bar = HP_BAR(self.screen, self.SCREEN_W, self.SCREEN_H, self.rect_hp, self.lose_hp_percent, self.inside_rect_w, self.damage_taked)

		# settings 
		self.slider = (0,0)
		self.done = False
		self.number_list = ["5","0","0"]
		self.hpnum_list = list(str(self.rect_hp))
		self.settings = Settings(self.screen, self.SCREEN_W, self.SCREEN_H, self.slider, self.bullet_damage, self.rect_hp, (0,0), self.done, (300,500), self.number_list, self.hpnum_list, self.triangle_red, self.triangle_green, self.triangle_blue, self.rectangle_red, self.rectangle_green, self.rectangle_blue)
		self.slider_rect2 = (self.settings.slider_rect.left + self.triangle_red, self.settings.slider_rect.centery)
		self.hp_slider_rect2 = self.settings.hp_slider_rect.center
		self.number_pressed = 0
		self.okey = False
		self.delete = False
		self.changing_limit = self.settings.changing_limit
		


	def game_loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					self.done = False
					self.slider = event.pos

					if event.pos[0] > 300 and event.button ==1:
						self.shout = True

				if event.type == pygame.MOUSEBUTTONUP:
					self.done = True

				if event.type == pygame.KEYDOWN:
					# check if the number key is pressed
					if pygame.K_0 <= event.key <= pygame.K_9:
						self.okey = True
						self.number_pressed = event.key - pygame.K_0

					if event.key == pygame.K_BACKSPACE:
						self.delete = True

							

			# Black Background
			self.screen.fill((0,0,0))


			# Triangle
			self.triangle = Triangle(self.screen, self.SCREEN_W, self.SCREEN_H, self.shout, self.bullets, self.bullet_damage, self.triangle_red, self.triangle_green, self.triangle_blue)
			self.triangle.update()
			self.shout = self.triangle.shout
			self.bullets = self.triangle.bullets
			self.bullet_damage = self.triangle.bullet_damage
			

			# Rectangle
			self.rectangle = Rectangle(self.screen, self.SCREEN_W, self.SCREEN_H, self.bullets, self.bullet_damage, self.rect_hp, self.rectangle_red, self.rectangle_green, self.rectangle_blue)
			self.rectangle.update()
			self.bullets = self.rectangle.bullets
			self.rect_hp = self.rectangle.rect_hp
			self.lose_hp_percent = self.rectangle.lose_hp_percent
			self.damage_taked = self.rectangle.damage_taked

			# HP BAR
			self.hp_bar = HP_BAR(self.screen, self.SCREEN_W, self.SCREEN_H, self.rect_hp, self.lose_hp_percent, self.inside_rect_w,self.damage_taked)
			self.hp_bar.update(self.changing_limit)
			self.inside_rect_w = self.hp_bar.inside_rect_w

			# Settings,
			self.settings = Settings(self.screen, self.SCREEN_W, self.SCREEN_H, self.slider, self.bullet_damage, self.rect_hp, self.slider_rect2,self.done, self.hp_slider_rect2, self.number_list, self.hpnum_list, self.triangle_red, self.triangle_green, self.triangle_blue, self.rectangle_red, self.rectangle_green, self.rectangle_blue)
			self.settings.update(self.number_pressed, self.okey,self.delete)
			self.slider_rect2 = self.settings.slider_rect2.center
			self.hp_slider_rect2 = (self.settings.hp_slider_rect2.centerx, self.settings.hp_slider_rect.centery)
			self.number_list = self.settings.number_list
			self.bullet_damage = int("".join(self.number_list))
			# hp
			self.hpnum_list = self.settings.hpnum_list
			self.rect_hp = int("".join(self.hpnum_list))
			self.okey = False
			self.delete = False
			self.changing_limit = self.settings.changing_limit
			# colors
			# triangle
			self.triangle_red = self.settings.triangle_red
			self.triangle_green = self.settings.triangle_green
			self.triangle_blue = self.settings.triangle_blue
			# rectangle
			self.rectangle_red = self.settings.rectangle_red
			self.rectangle_green = self.settings.rectangle_green
			self.rectangle_blue = self.settings.rectangle_blue



	
			pygame.display.update()
			self.clock.tick(60)

	def update(self):
		self.game_loop()


# Run
Main().update()
















