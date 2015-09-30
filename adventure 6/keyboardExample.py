import pygame
pygame.init()

#Window Setup
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#game loop
done = False
while not done:
    keys = pygame.key.get_pressed()

    #display a message when 'w' key is pressed
    if keys[pygame.K_w]:
        print "Hello"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(32)
pygame.quit()

