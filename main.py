import pygame
import sys
from start_game import *
from shop import *

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

logo_image = pygame.image.load("logo.png")
font = pygame.font.Font(None, 36)

def draw(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

def recize_image(image, new_size):
	return pygame.transform.smoothscale(image, new_size)

def load_background():
	try:
		with open("saves/currentBG.txt") as file:
			background_image_path = file.read().strip()
		background_image= pygame.image.load(background_image_path).convert()
		return pygame.transform.scale(background_image, (WIDTH, HEIGHT))
	except FileNotFoundError:
		return None

while True:
	background_image = load_background()
	if background_image is None:
		background_image = pygame.Surface((WIDTH, HEIGHT))
		background_image.fill(WHITE)

	screen.blit(background_image, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start_button_rect.collidepoint(event.pos):
				run_game()
			if shop_button_rect.collidepoint(event.pos):
				run_shop()
			if exit_button_rect.collidepoint(event.pos):
				pygame.quit()
				sys.exit()

	start_button_rect = pygame.draw.rect(screen, GRAY, (50, 50, 100, 50))
	shop_button_rect = pygame.draw.rect(screen, GRAY, (50, 150, 100, 50))
	exit_button_rect = pygame.draw.rect(screen, GRAY, (50, 250, 100, 50))

	draw("Start", font, BLACK, screen, 65, 65)
	draw("Shop", font, BLACK, screen, 65, 165)
	draw("Exit", font, BLACK, screen, 65, 265)

	pygame.display.flip()

















































































































































































































































