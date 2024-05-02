import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

#initialise pygame
pygame.init()

#sets the game display name at window top
pygame.display.set_caption("Super Star Quest")

#set window size,fps and speed of user movement
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOUR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("Background", "Green.png"))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


#EVENT LOOP
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png")
#event loop while loop, ensures FPS
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)
    pygame.quit()
    quit()


#ONLY CALLING THIS FUNCTION IF CALLED, NOT RUN WHEN BEING CALLED FROM OTHER FILES/FUNCTIONS
if __name__=="__main__":
    main(window)