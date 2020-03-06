import pygame
pygame.init()

win = pygame.display.set_mode((800, 615))
img1 = pygame.image.load('img1.png')
img2 = pygame.image.load('img2.png')
img3 = pygame.image.load('img3.png')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))
    for i in range(50):
        for j in range(50):
         win.blit(img1, (i * 47, j * 47)) #Door picture
    row = [1, 0, 0, 1]
    for i in range(4):
        if row[i] == 1:
            win.blit(img2, (47, 0))
        if row[i] == 0:
            win.blit(img2, (i, 0)) # Open Door picture
    row = [1, 0, 0, 1]
    for i in range(4):
        if row[i] == 1:
            win.blit(img3, (i*90, 0))
        if row[i] == 0:
            win.blit(img3, (i * 90, 0)) #Stairs Image
    pygame.display.update()
pygame.quit()