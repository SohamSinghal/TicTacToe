import pygame
from pygame.constants import *
from Constants import *
import time
pygame.init()
size = width, height = 600, 600
margin = 5
font = pygame.font.SysFont('Arial',50)
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode(size)
i = 0
screen.fill(colour["black"])
l = [7,8,9,4,5,6,1,2,3]
i = 0
for x in range(3):
    for y in range(3):
            X = margin+y*width//3
            Y = margin+x*height//3
            W = (width/3)-2*margin
            H = (height/3)-2*margin
            pygame.draw.rect(screen,colour["white"],pygame.Rect(X,Y,W,H))
            font_render = font.render(example[str(l[i])],True,colour["black"])
            screen.blit(font_render,(X+W/2*0.8,Y+H/2*0.7))
            i = i + 1
            pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()

            
