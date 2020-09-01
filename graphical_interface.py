import pygame
import sys
from hospital_placer import *

pygame.init()

# Defining screen
size = (width, height) = (600, 400)
window = pygame.display.set_mode(size)
window.fill((62, 76, 86))

# Image load
house = pygame.transform.scale(pygame.image.load('house.png'), (35, 35))
hospital = pygame.transform.scale(pygame.image.load('hospital.png'), (35, 35))

# Setting icon and name
pygame.display.set_caption('Hospital Site')

# Fonts
my_font = 'OpenSans-Regular.ttf'
large_font = pygame.font.Font(None, 40)

# House placement
houses = []
while True:
    coordinate = (random.randint(0, width / 40 - 1), random.randint(0, height /
                                                                 40 - 1))
    if coordinate not in houses:
        houses.append(coordinate)
    if len(houses) == 20:
        break

# Hospital placement
hp = Hospital(width, height, 40, 4, houses)
hospitals = hp.optimization(4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Drawing the rectangular boxes for hospital and house placement
    box = dict()
    for column in range(int(width / 40)):
        for row in range(int(height / 40)):
            box[(column, row)] = pygame.Rect(column * 40, row * 40, 40, 40)
            pygame.draw.rect(window, (38, 155, 213), box[(column, row)], 1)

            # House placement
            if (column, row) in houses:
                window.blit(house, (box[(column, row)][0] + 2,
                                    box[(column, row)][1] + 2))

            # Hospital placement
            if (column, row) in hospitals:
                window.blit(hospital, (box[(column, row)][0] + 2,
                                    box[(column, row)][1] + 2))

    # Display update
    pygame.display.update()
