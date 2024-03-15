import pygame
import os

_image_library = {}
def get_image(path):
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))

    frog_image = get_image('../assets/images/froggy.webp')
    scaled_frog_image = pygame.transform.scale(frog_image, (100, 100))

    screen.blit(scaled_frog_image, (150, 100))

    pygame.display.flip()
    clock.tick(60)