from PIL import Image
import numpy as np
import pygame 
from pygame.locals import *
import cv2
from imutils import resize

pygame.init()
pygame.font.init()

# WINDOW
WIN_WIDTH, WIN_HEIGHT = 500, 500
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("ASCII Video Player")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FONTS 
PIXEL_SIZE = 7
font = pygame.font.SysFont("comicsans", PIXEL_SIZE)
 
running = True 
ascii_img = []
density = "@%&#-_+~!,."
clock = pygame.time.Clock()
vid = cv2.VideoCapture(0)
while running:
    clock.tick(30)

    ascii_img = []
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    _, frame = vid.read()
    img = resize(frame, width=WIN_WIDTH//PIXEL_SIZE)
    
    for row in img:
        ascii_row = []
        for pixel in row:
            avg = int(np.mean(pixel))
            if avg>=250:
                ascii_row.append(density[0])
            elif avg>=225:
                ascii_row.append(density[1])
            elif avg>=200:
                ascii_row.append(density[2])
            elif avg>=175:
                ascii_row.append(density[3])
            elif avg>=150:
                ascii_row.append(density[4])
            elif avg>=125:
                ascii_row.append(density[5])
            elif avg>=100:
                ascii_row.append(density[6])
            elif avg>=75:
                ascii_row.append(density[7])
            elif avg>=50:
                ascii_row.append(density[8])
            elif avg>=25:
                ascii_row.append(density[9])
            else:
                ascii_row.append(density[10])
        ascii_img.append(ascii_row)

    for i, row in enumerate(ascii_img):
        for j, pixel in enumerate(row):
            text = font.render(pixel, True, WHITE)
            window.blit(text, (j*PIXEL_SIZE, i*PIXEL_SIZE))    

    pygame.display.update()    