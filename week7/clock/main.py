import pygame
import os
from datetime import datetime

_image_library = {}
def get_image(path):
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
pygame.display.set_caption("Simple Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock_image = pygame.transform.scale(get_image('../assets/images/alarm-clock.png'), (350, 350))
minute_hand_img = pygame.transform.rotate(pygame.transform.scale(get_image('../assets/images/minutes_hand.png'), (180, 180)), -225)
second_hand_img = pygame.transform.scale(get_image('../assets/images/seconds_hand.png'), (300, 300))

clock = pygame.time.Clock()

def rotate_center(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(WIDTH//2, HEIGHT//2)).center)
    return rotated_image, new_rect

def draw_clock_hands():
    current_time = datetime.now()
    second_angle = - current_time.second * 6
    minute_angle = - current_time.minute * 6

    rotated_minute_hand, minute_hand_rect = rotate_center(minute_hand_img, minute_angle)
    screen.blit(rotated_minute_hand, minute_hand_rect)

    rotated_second_hand, second_hand_rect = rotate_center(second_hand_img, second_angle)
    screen.blit(rotated_second_hand, second_hand_rect)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    screen.blit(clock_image, ((WIDTH - 352) // 2, (HEIGHT - 384) // 2))
    draw_clock_hands()

    pygame.display.flip()

    clock.tick(60)
