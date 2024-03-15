import pygame
import os

_sound_library = {}
def play_sound(path):
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
    sound.play()

pygame.init()
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
is_blue = True
x = 30
y = 30
rect_width = 60
rect_height = 60

clock = pygame.time.Clock()

pygame.mixer.music.load('../assets/sounds/Құрмаш Маханов - Кездесу мен қоштасу].mp3')
music_playing = False
move_keys = [
    pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d,
    pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT
]

key_held_down = {key: False for key in move_keys}

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            music_playing = not music_playing
            if not music_playing:
                pygame.mixer.music.stop()
            else: 
                pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and (event.key in move_keys):
            if not key_held_down[event.key]:
                play_sound('../assets/sounds/slimejump-6913.mp3')
                key_held_down[event.key] = True
        if event.type == pygame.KEYUP and (event.key in move_keys):
            key_held_down[event.key] = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_w]: 
        if y > 0:
            y -= 3
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: 
        if y < screen_height - rect_height:
            y += 3
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: 
        if x > 0:
            x -= 3
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: 
        if x < screen_width - rect_width:
            x += 3

    screen.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, rect_width, rect_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()