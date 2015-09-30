import math
import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

width = 200
height = 200
x = windowSize[0] / 2 - width / 2
y = windowSize[1] / 2 - height / 2
colour = pygame.color.Color('#57B0F6')
black = pygame.color.Color('#000000')

count = 0
done = False

while not done:
    screen.fill(black)
#    pygame.draw.ellipse(screen, colour, [x, y, width, height])
    pygame.draw.rect(screen, colour, [x, y, width, height])
    width += math.cos(count) * 10
    x -= (math.cos(count) * 10) / 2
    height += math.sin(count) * 10
    y -= (math.sin(count) * 10) / 2
    count += 0.5

    if width == height:
        pygame.display.set_caption("CIRCLE!!!")
    #else:
    #    pygame.display.set_caption("NOT A CIRCLE.")

    pygame.display.flip()

#    pygame.image.save(screen, "rect_" + str(count) + ".png")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(24)

pygame.quit()
