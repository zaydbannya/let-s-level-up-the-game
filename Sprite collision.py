import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500 ,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("times new roman", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, weidth):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.disply.set_caption("sprite collision")
all_sprites = pygame.sprite.Groupe()
sprite1 = Sprite(pygame.color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y