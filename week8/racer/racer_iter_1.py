import pygame, sys, os
from pygame.locals import *
import random, time
 
pygame.init()

# Regulating image path both on Unix and MS-DOS + preventing oveloading with pygame.image.load
_image_library = {}
def get_image(path):
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

done = False
FPS = 60
Clock = pygame.time.Clock()

# Colors
BLACK = pygame.Color(0, 0, 0)         
WHITE = pygame.Color(255, 255, 255)   
GREY = pygame.Color(128, 128, 128)  
RED = pygame.Color(255, 0, 0)   

# Game variables
SPEED = 5

# Setting up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("Racer Game")

# Creating parent class to avoid repetition within Player and Enemy children
class Car(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = get_image(image_path)
        self.rect = self.image.get_rect()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(Car):
    def __init__(self, image_path):
        super().__init__(image_path)
        # Centering Enemy randomly on x-axis counting its image width
        self.rect.center = (random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > (SCREEN_HEIGHT + self.rect.height):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width - 10, SCREEN_WIDTH - self.rect.width + 10), 0)

class Player(Car):
    def __init__(self, image_path):
        super().__init__(image_path)
        # Centering Player on x, y counting its image width and height
        self.rect.center = (SCREEN_WIDTH / 2 - self.rect.width, SCREEN_HEIGHT - self.rect.height)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(5, 0)


# Setting up sprites
P1 = Player("Player.png")
E1 = Enemy("Enemy.png")

# Grouping sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding new User Event that is called every 1000ms
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 2

    SCREEN.fill(WHITE)
    
    # Move and re-draw sprites
    for entity in all_sprites:
        entity.draw(SCREEN)
        entity.move()

    # Handling collisions
    if pygame.sprite.spritecollideany(P1, enemies):
        SCREEN.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(5)
        done = True

    pygame.display.update()
    Clock.tick(FPS)

pygame.quit()
sys.exit()