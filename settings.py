import pygame
import math

class Settings:
	def __init__(self, screen, SCREEN_W, SCREEN_H, slider, bullet_damage, rect_hp, slider_rect2, done, hp_slider_rect2, number_list,hpnum_list, triangle_red, triangle_green, triangle_blue, rectangle_red, rectangle_green, rectangle_blue):
		self.SCREEN_W = SCREEN_W
		self.SCREEN_H = SCREEN_H
		self.screen = screen
		self.slider = slider
		self.done = done

		self.font = pygame.font.Font(None, 30)

		#mouse position
		self.mouse_pos = pygame.mouse.get_pos()

		# click color
		self.bullet_color = (255,255,255)
		self.hp_color = (255,255,255)

		""" COLOR SETTINGS """
		# TRIANGLE
		self.triangle_red = triangle_red
		self.triangle_green = triangle_green
		self.triangle_blue = triangle_blue
		# RECTANGLE
		self.rectangle_red = rectangle_red
		self.rectangle_green = rectangle_green
		self.rectangle_blue = rectangle_blue
		

		#setting background
		self.setting_rect = pygame.Rect(0, 0, 300, SCREEN_H)
		self.setting_rect.topleft = (0,0)

		# bullet settings
		self.bullet_text = self.font.render("Bullet Damage", True, (0,0,0))  # "bullet damage" text
		self.bullet_text_rect = self.bullet_text.get_rect(center = (150, 50)) # rect of text above

		self.bullet_damage = bullet_damage # real bullet damage
		self.bullet_surf = self.font.render(f"{self.bullet_damage}", True, (0,0,0)) # real bullet damage
		# rect of real bullet damage
		self.bullet_rect = self.bullet_surf.get_rect(midtop = (self.bullet_text_rect.midbottom[0], self.bullet_text_rect.midbottom[1]+10))
		# Creating rect for for real bullet damage when you click it you can change it
		self.damage_set_rect = pygame.Rect(0,0,(self.bullet_rect.right - self.bullet_rect.left) + 10, (self.bullet_rect.bottom - self.bullet_rect.top) + 10)
		self.damage_set_rect.center = self.bullet_rect.center # position update
		# bullet_color slider
		# TRIANGLE RED
		self.slider_rect = pygame.Rect(0,0,255,10) # Creating slider for change triangle color
		self.slider_rect.center = (self.setting_rect.center[0], self.damage_set_rect.bottom + 20) # position set for slider

		self.slider_rect2 = pygame.Rect(0,0,10, 20) # red color pointer
		self.slider_rect2.center = slider_rect2 # position set for the point

		# TRIANGLE GREEN
		self.green_slider = pygame.Rect(0,0,255,10)
		self.green_slider.center = (self.setting_rect.center[0], self.slider_rect.bottom + 25)
		# GREEN pointer
		self.green_pointer = pygame.Rect(0,0,10,20)
		self.green_pointer.center = (self.green_slider.left + self.triangle_green, self.green_slider.centery)

		# TRIANGLE BLUE
		self.blue_slider = pygame.Rect(0,0,255,10)
		self.blue_slider.center = (self.setting_rect.center[0], self.green_slider.bottom + 25)
		# BLUE pointer
		self.blue_pointer = pygame.Rect(0,0,10,20)
		self.blue_pointer.center = (self.blue_slider.left + self.triangle_blue, self.blue_slider.centery)


		# rectangle settings
		self.hp_text = self.font.render("Rectangle HP", True, (0,0,0)) # "Rectangle HP" text
		self.hp_text_rect = self.hp_text.get_rect(center = (150, self.blue_slider.bottom + 60)) # rect of the text above

		self.rect_hp = rect_hp # real hp
		self.hp_surf = self.font.render(f"{self.rect_hp}", True, (0,0,0)) # real hp
		
		self.hp_rect = self.hp_surf.get_rect(midtop = (self.hp_text_rect.midbottom[0], self.hp_text_rect.midbottom[1]+10)) # rect of the real hp
		# rect for set real hp
		self.hp_set_rect = pygame.Rect(0,0,(self.hp_rect.right - self.hp_rect.left) + 10, (self.hp_rect.bottom - self.hp_rect.top) + 10)
		self.hp_set_rect.center = self.hp_rect.center
		
		# RECTANGLE COLOR CHANGE
		
		# RECTANGLE RED
		self.hp_slider_rect = pygame.Rect(0,0,255,10)
		self.hp_slider_rect.center = (self.setting_rect.center[0], self.hp_set_rect.bottom + 20)

		self.hp_slider_rect2 = pygame.Rect(0,0,10, 20) # pointer
		self.hp_slider_rect2.center = (self.hp_slider_rect.left + self.rectangle_red, self.hp_slider_rect.centery)

		# RECTANGLE GREEN
		self.rect_green_slider = pygame.Rect(0,0,255,10)
		self.rect_green_slider.center = (self.setting_rect.center[0], self.hp_slider_rect.bottom + 25)
		# RECTANGLE GREEN POINTER
		self.rect_green_pointer = pygame.Rect(0,0,10,20)
		self.rect_green_pointer.center = (self.rect_green_slider.left + self.rectangle_green, self.rect_green_slider.centery)

		# RECTANGLE BLUE
		self.rect_blue_slider = pygame.Rect(0,0,255,10)
		self.rect_blue_slider.center = (self.setting_rect.center[0], self.rect_green_slider.bottom + 25)
		# RECTANGLE BLUE POINTER
		self.rect_blue_pointer = pygame.Rect(0,0,10,20)
		self.rect_blue_pointer.center = (self.rect_blue_slider.left + self.rectangle_blue, self.rect_blue_slider.centery)


		
		self.number_list = number_list
		self.hpnum_list = list(str(self.rect_hp))
		self.changing_limit = False


	
		
	def bullet_damage_set(self,number_pressed, okey, delete):
		if self.damage_set_rect.collidepoint(self.slider):
			self.bullet_color = (173,216,230)
			if okey:
				self.number_list.append(f"{number_pressed}")

			elif delete:
				self.number_list.pop(-1)
				if len(self.number_list) == 0:
					self.number_list.append("0")
				

		# TRIANGLE RED
		elif (self.slider_rect.collidepoint(self.slider) or self.slider_rect2.collidepoint(self.slider)) and not self.done:
			self.slider_rect2.centerx = self.mouse_pos[0]

			self.triangle_red = int(self.slider_rect2.centerx - self.slider_rect.left)
			if self.triangle_red < 0:
				self.triangle_red = 0

			elif self.triangle_red > 255:
				self.triangle_red = 255

		# TRIANGLE GREEN
		elif (self.green_slider.collidepoint(self.slider) or self.green_pointer.collidepoint(self.slider)) and not self.done:
			self.green_pointer.centerx = self.mouse_pos[0]

			self.triangle_green = int(self.green_pointer.centerx - self.green_slider.left)
			if self.triangle_green < 0:
				self.triangle_green = 0

			elif self.triangle_green > 255:
				self.triangle_green = 255

		# TRIANGLE BLUE
		elif (self.blue_slider.collidepoint(self.slider) or self.blue_pointer.collidepoint(self.slider)) and not self.done:
			self.blue_pointer.centerx = self.mouse_pos[0]

			self.triangle_blue = int(self.blue_pointer.centerx - self.blue_slider.left)
			if self.triangle_blue < 0:
				self.triangle_blue = 0

			elif self.triangle_blue > 255:
				self.triangle_blue = 255
			

		# if outside the slider_rect
		# RED POINTER
		if self.slider_rect2.left < self.slider_rect.left:
			self.slider_rect2.left = self.slider_rect.left
		elif self.slider_rect2.right > self.slider_rect.right:
			self.slider_rect2.right = self.slider_rect.right

		# GREEN POINTER
		if self.green_pointer.left < self.green_slider.left:
			self.green_pointer.left = self.green_slider.left

		elif self.green_pointer.right > self.green_slider.right:
			self.green_pointer.right = self.green_slider.right

		# BLUE POINTER
		if self.blue_pointer.left < self.blue_slider.left:
			self.blue_pointer.left = self.blue_slider.left

		elif self.blue_pointer.right > self.blue_slider.right:
			self.blue_pointer.right = self.blue_slider.right

	def rectangle_hp(self,number_pressed,okey,delete):
		if self.hp_set_rect.collidepoint(self.slider):
			self.hp_color = (173,216,230)

			if okey:
				self.hpnum_list.append(f"{number_pressed}")
				self.changing_limit = True

			elif delete:
				self.hpnum_list.pop(-1)
				self.changing_limit = True
				if len(self.hpnum_list) == 0:
					self.hpnum_list.append("0")

		# Rectangle Red
		elif (self.hp_slider_rect.collidepoint(self.slider) or self.hp_slider_rect2.collidepoint(self.slider)) and not self.done:
			self.hp_slider_rect2.centerx = self.mouse_pos[0]

			self.rectangle_red = self.hp_slider_rect2.centerx - self.hp_slider_rect.left
			if self.rectangle_red < 0:
				self.rectangle_red = 0

			elif self.rectangle_red > 255:
				self.rectangle_red = 255

		# Rectangle Green
		elif (self.rect_green_slider.collidepoint(self.slider) or self.rect_green_pointer.collidepoint(self.slider)) and not self.done:
			self.rect_green_pointer.centerx = self.mouse_pos[0]

			self.rectangle_green = self.rect_green_pointer.centerx - self.rect_green_slider.left
			if self.rectangle_green < 0:
				self.rectangle_green = 0

			elif self.rectangle_green > 255:
				self.rectangle_green = 255

		# Rectangle Blue
		elif (self.rect_blue_slider.collidepoint(self.slider) or self.rect_blue_pointer.collidepoint(self.slider)) and not self.done:
			self.rect_blue_pointer.centerx = self.mouse_pos[0]

			self.rectangle_blue = self.rect_blue_pointer.centerx - self.rect_blue_slider.left
			if self.rectangle_blue < 0:
				self.rectangle_blue = 0
				
			elif self.rectangle_blue > 255:
				self.rectangle_blue = 255



		
		# if outside the slider_rect
		# RECT RED POINTER
		if self.hp_slider_rect2.left < self.hp_slider_rect.left:
			self.hp_slider_rect2.left = self.hp_slider_rect.left
		elif self.hp_slider_rect2.right > self.hp_slider_rect.right:
			self.hp_slider_rect2.right = self.hp_slider_rect.right

		# RECT GREEN POINTER
		if self.rect_green_pointer.left < self.rect_green_slider.left:
			self.rect_green_pointer.left = self.rect_green_slider.left
		elif self.rect_green_pointer.right > self.rect_green_slider.right:
			self.rect_green_pointer.right = self.rect_green_slider.right

		# RECT BLUE POINTER
		if self.rect_blue_pointer.left < self.rect_blue_slider.left:
			self.rect_blue_pointer.left = self.rect_blue_slider.left
		elif self.rect_blue_pointer.right > self.rect_blue_slider.right:
			self.rect_blue_pointer.right = self.rect_blue_slider.right
			

	def rectangle_armor(self):
		pass

	def draw(self):
		# draw setting rect
		pygame.draw.rect(self.screen, (200,200,200), self.setting_rect)
		# draw bullet damage text
		self.screen.blit(self.bullet_text, self.bullet_text_rect)
		
		pygame.draw.rect(self.screen, self.bullet_color,self.damage_set_rect,0,5)
		
		self.screen.blit(self.bullet_surf, self.bullet_rect)

		# TRIANGLE RED SLIDER
		pygame.draw.rect(self.screen, (80,80,80), self.slider_rect, 0, 5)

		pygame.draw.rect(self.screen, (0,0,0), self.slider_rect2, 0, 5)

		# TRIANGLE GREEN SLIDER
		pygame.draw.rect(self.screen, (80,80,80), self.green_slider, 0, 5)

		pygame.draw.rect(self.screen, (0,0,0), self.green_pointer, 0, 5)

		# TRIANGLE BLUE SLIDER
		pygame.draw.rect(self.screen, (80,80,80), self.blue_slider, 0, 5)

		pygame.draw.rect(self.screen, (0,0,0), self.blue_pointer, 0, 5)

		# draw rectangle hp text
		self.screen.blit(self.hp_text, self.hp_text_rect)
		
		pygame.draw.rect(self.screen, self.hp_color,self.hp_set_rect,0,5)
		
		self.screen.blit(self.hp_surf, self.hp_rect)

		# RECTANGLE RED SLIDER
		pygame.draw.rect(self.screen, (80,80,80), self.hp_slider_rect, 0, 5)
		
		pygame.draw.rect(self.screen, (0,0,0), self.hp_slider_rect2, 0, 5)
		
		# RECTANGLE GREEN
		pygame.draw.rect(self.screen, (80,80,80), self.rect_green_slider, 0, 5)
		pygame.draw.rect(self.screen, (0,0,0), self.rect_green_pointer,0,5)

		# RECTANGLE BLUE
		pygame.draw.rect(self.screen, (80,80,80), self.rect_blue_slider, 0, 5)
		pygame.draw.rect(self.screen, (0,0,0), self.rect_blue_pointer, 0, 5)

	def update(self, number_pressed, okey, delete):
		self.bullet_damage_set(number_pressed,okey, delete)
		self.rectangle_hp(number_pressed,okey,delete)
		self.rectangle_armor()
		self.draw()

























