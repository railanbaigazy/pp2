import pygame

pygame.init()

screen_height = 400
screen_width = 400
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
x = 200
y = 200
radius = 25
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_w]: 
        if y > radius:
            y -= 20
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: 
        if y < screen_height - radius:
            y += 20
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: 
        if x > radius:
            x -= 20
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: 
        if x < screen_width - radius:
            x += 20
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()