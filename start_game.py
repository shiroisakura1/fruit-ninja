import pygame
import random
import os
import sys

def run_game():
	pass
	pygame.init()
    BLACK = (0, 0, 0)
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fruit ninja")

    apple_image = pygame.image.load("apple.png")
    banana_image = pygame.image.load("banana.png")
    watermelon_image = pygame.image.load("watermelon.png")
    orange_image = pygame.image.load("orange.ong")

    apple_image = pygame.transform.scale(apple_image, (45, 45))
    banana_image = pygame.transform.scale(banana_image, (45, 45))
    orange_image = pygame.transform.scale(orange_image, (45, 45))
    watermelon_image = pygame.transform.csale(watermelon_image, (45, 45))

    bomb_image = pygame.image.load("bomb.png")
    bomb_image = pygame.transform.scale(bomb_image, (45, 45))

    explored_image = pygame.image.load("explored.png")
    explored_image = pygame.transform.scale(explored_image, (45, 45))

    knife_image = pygame.image.load("knife.png")
    knife_image = pygame.transform.scale(knife_image, (45, 45))

    pygame.mouse.set_visible(False)
    fruits = [(apple_image, 2), (banana_image ,3), (watermelon_image, 4), (orange_image, 5)]

    bombs = [bomb_image]

    spot_apple_image = pygame.image.load("spot_apple.png")
    spot_banana_image = pygame.image.load("spot_banana.png")
    spot_watermelon_image = pygame.image.load("spot_watermelon.png")
    spot_orange_image = pygame.image.load("spot_orange.ong")

    spot_apple_image = pygame.transform.scale(spot_apple_image, (45, 45))
    spot_banana_image = pygame.transform.scale(spot_banana_image, (45, 45))
    spot_orange_image = pygame.transform.scale(spot_orange_image, (45, 45))
    spot_watermelon_image = pygame.transform.csale(spot_watermelon_image, (45, 45))

	fruits_to_spot = {
		apple_image: spot_apple_image,
		banana_image: spot_banana_image,
		orange_image: spot_orange_image,
		watermelon_image: spot_watermelon_image
	}
	class GameObject:
		def __init__ (self, image, speed):
			self.image = image
			self.speed = speed
			self.width, self.height = self.image.get_size()
			self.x = random.randint(0, SCREEN_WIDTH - self.width)
			self.y = self.height

	class Spot:
		def __init__ (self, image, x, y):
			self.image = image
			self.width, self.height = self.image.get_size()
			self.x = x - (self.width - self.width) // 2
			self.y = y - (self.height - self.height) // 2












































































































































































