import pygame
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the object based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # draw the object on the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))

    # update the display
    pygame.display.flip()

    # control the frame rate
    clock.tick(60)

# quit the game
pygame.quit()
