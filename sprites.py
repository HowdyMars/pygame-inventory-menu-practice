'''Handling Sprites'''
import pygame as pg

class SpriteSheet():
	def __init__(self, image, name: str = "item"):
		self.name = name
		self.sheet = pg.image.load(image).convert_alpha()

	def get_image(self, frame, width, height, scale):
		image = pg.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pg.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey('black')

		return image
	
class Animation():
	def __init__(self, screen, image):
		self.screen = screen
		self.sprite_sheet = SpriteSheet(image)
		self.animation_list = []
		self.player_animation_steps = [9] # index from sprite sheet | indexs: 0 'idle'
		self.animation_cooldown = 90 #mili-seconds
		self.start_frame = 0
		self.step_counter = 0
		self.last_update = pg.time.get_ticks()

	def player_animation(self, index, rect):
		current_time = pg.time.get_ticks()
		for animation in self.player_animation_steps:
			temp_img_list = []
			for _ in range(animation):
				temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 32, 32, 3))
				self.step_counter += 1
			self.animation_list.append(temp_img_list)
			
		if current_time - self.last_update >= self.animation_cooldown:
			self.start_frame += 1
			self.last_update = current_time
			if self.start_frame >= len(self.animation_list[index]):
				self.start_frame = 0

		self.screen.blit(self.animation_list[index][self.start_frame], (rect))
		pg.mask.from_surface(self.animation_list[index][self.start_frame])

class Menus(Animation):
	def __init__(self, screen, image):
		super().__init__(screen, image)
		self.start_menu_steps = [1, 1, 1] # index from sprite sheet | indexs: 0 'base' | 1 'play' | 2 'quit'
		self.menu_index = 1

	def start_menu_sprites(self):
		current_time = pg.time.get_ticks()
		for animation in self.start_menu_steps:
			temp_img_list = []
			for _ in range(animation):
				temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 300, 305, 2))
				self.step_counter += 1
			self.animation_list.append(temp_img_list)
			
		if current_time - self.last_update >= self.animation_cooldown:
			self.start_frame += 1
			self.last_update = current_time
			if self.start_frame >= len(self.animation_list[self.menu_index]):
				self.start_frame = 0

		self.screen.blit(self.animation_list[self.menu_index][self.start_frame], (350, 50))

	def menu_options(self, events, gameStateManager):
		'''listen for key input then change index'''
		for event in events:
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_UP and self.menu_index > 1:
					self.menu_index -= 1
				if event.key == pg.K_DOWN and self.menu_index <= 1:
					self.menu_index +=1
				if event.key == pg.K_SPACE and self.menu_index == 1:
					gameStateManager.set_state('level')
				if event.key == pg.K_SPACE and self.menu_index == 2:
					pg.quit()

class ItemSprites(Animation):
	def __init__(self, screen, image):
		super().__init__(screen, image)
		self.item_list = []
		self.item_list_steps = [5, 15, 1, 10, 1, 15, 15] # 15, 1, 10, 1, 15, 15
		# index from sprite sheet | indexs: 0 'armor' | 1 'bows' | 2 'ruby' | 3 'helm' | 4 'goldBar' | 5 'shield' | 6 'sword'
		self.type_index = 6
		self.item_index = 4
		self.frame_count = 0

	def item_sprites(self):
		for type in self.item_list_steps:
			temp_img_list = []
			for _ in range(type):
				temp_img_list.append(self.sprite_sheet.get_image(self.frame_count, 32, 32, 2))
				self.frame_count += 1
			self.item_list.append(temp_img_list)
		
		self.screen.blit(self.item_list[self.type_index][self.item_index], (100, 100))



