import pygame
pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)

colour = pygame.color.Color('#646400')
row = 0
done = False
while not done:
    increment = 255/100

    while row <= height:
        pygame.draw.rect(screen, colour, (0, row, width, row + increment))
        pygame.display.flip()
        #if colour[0] + increment < 255:
        #    colour[0] += increment
        #if colour[1] + increment < 255:
        #    colour[1] += increment
        if colour[2] + increment < 255:
            colour[2] += increment
        row += increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
