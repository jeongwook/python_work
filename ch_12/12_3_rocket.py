import sys

import pygame

class Ship():

	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 4
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 4
		if self.moving_up and self.rect.top > 0:
			self.rect.centery -= 4
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 4

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
			elif event.key == pygame.K_UP:
				ship.moving_up = True
			elif event.key == pygame.K_DOWN:
				ship.moving_down = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
			elif event.key == pygame.K_UP:
				ship.moving_up = False
			elif event.key == pygame.K_DOWN:
				ship.moving_down = False

def run_game():
	# Initialize game and create a screen object
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))

	# Set the background color.
	bg_color = (230, 230, 230)

	# Make a ship.
	ship = Ship(screen)

	# Main loop
	while True:

		# Watch for keyboard events.
		check_events(ship)
		ship.update()

		# Redraw the screen during each pass through the loop
		screen.fill(bg_color)
		ship.blitme()

		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()