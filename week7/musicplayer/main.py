import pygame
import json
import os
from enum import Enum

with open('playlist.json', 'r') as file:
    PLAYLIST = json.loads(file.read())["playlist"]

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False
pygame.display.set_caption("Music Player")

class Color(Enum):
    BACKGROUND = (255, 255, 255)
    PRIMARY = (0, 0, 0)

font = pygame.font.Font(None, 36)
heading_text = font.render("Now playing:", True, Color.PRIMARY.value)
current_song_id = 0
is_playing = False
song_text = font.render("_________", True, Color.PRIMARY.value)

def update_song():
    global song_text, is_playing
    song_name = PLAYLIST[current_song_id]["name"]
    song_text = font.render(song_name, True, Color.PRIMARY.value)
    is_playing = not is_playing

    if not is_playing:
        stop_sound()
    else:
        play_sound(current_song_id)

_sound_library = {}
def play_sound(id):
    global is_playing
    path = PLAYLIST[id]["path"]
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()

def stop_sound():
    global is_playing
    path = PLAYLIST[id]["path"]
    sound = _sound_library.get(path)
    sound.stop()
    is_playing = False

def next_song():
    global current_song_id, is_playing
    current_song_id = (current_song_id + 1) % len(PLAYLIST)
    update_song()
    play_sound(current_song_id)

def prev_song():
    global current_song_id
    current_song_id = (current_song_id - 1) % len(PLAYLIST)
    update_song()
    play_sound(current_song_id)

def stop_sound():
    global is_playing
    pygame.mixer.stop() 
    is_playing = False 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
            elif event.key == pygame.K_SPACE:
                update_song()

    screen.fill(Color.BACKGROUND.value)

    screen.blit(heading_text, ((WIDTH / 2) - heading_text.get_width() // 2, (HEIGHT / 2) - 50))
    screen.blit(song_text, ((WIDTH / 2) - song_text.get_width() // 2, (HEIGHT / 2) - song_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
