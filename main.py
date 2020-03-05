import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img1 = pygame.image.load('img1.png')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    for i in range(50):
        
        for j in range(50):
         win.blit(img1, (i * 47, j * 47))


    pygame.display.update()

pygame.quit()