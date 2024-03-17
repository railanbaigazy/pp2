import pygame
import json
import os
from enum import Enum

with open('playlist.json', 'r') as file:
    PLAYLIST = json.loads(file.read())["playlist"]

pygame.init()

_image_library = {}
def get_image(path):
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False
pygame.display.set_caption("Music Player")

class Color(Enum):
    BACKGROUND = (247, 247, 247)
    PRIMARY = (0, 0, 0)
    SECONDARY = (133, 72, 54)

font = pygame.font.Font(None, 36)
heading_text = font.render("Now playing:", True, Color.SECONDARY.value)
is_started = False
current_song_id = 0
current_song_time = {"minutes": "0", "seconds": "0"}
is_playing = False
song_text = font.render("_________", True, Color.PRIMARY.value)
duration_text = font.render("0:00 / 0:00", True, Color.SECONDARY.value)
play_image = pygame.transform.scale(get_image("../assets/images/play.png"), (50, 50))
stop_image = pygame.transform.scale(get_image("../assets/images/stop.png"), (50, 50))

last_update_time = 0

def set_song_duration():
    global current_song_id, duration_text, is_started, last_update_time
    if is_started and pygame.time.get_ticks() - last_update_time >= 1000:
        last_update_time = pygame.time.get_ticks()
        duration = PLAYLIST[current_song_id]["duration"]
        duration_minutes = duration["minutes"]
        duration_seconds = duration["seconds"]
        duration_seconds_text = f"0{duration_seconds}" if int(duration_seconds) < 10 else duration_seconds
        duration_text = font.render(f"{countup_song_duration()} / {duration_minutes}:{duration_seconds_text}", True, Color.SECONDARY.value)

def countup_song_duration():
    global current_song_time, is_playing, last_update_time
    minutes = int(current_song_time["minutes"])
    seconds = int(current_song_time["seconds"])
    if is_playing:
        if seconds < 60:
            seconds += 1
        else:
            seconds = 0
            minutes += 1
    current_song_time["minutes"] = minutes
    current_song_time["seconds"] = seconds
    text = f"{minutes}:" + (f"0{seconds}" if int(seconds) < 10 else str(seconds))

    return text
        
def update_song():
    global song_text, is_started, last_update_time
    if not is_started: 
        is_started = True
        last_update_time = pygame.time.get_ticks()
    song_name = PLAYLIST[current_song_id]["name"]
    song_text = font.render(song_name, True, Color.PRIMARY.value)
    set_song_duration()

def toggle_song():
    global is_playing, current_song_id, is_started
    is_playing = not is_playing
    if is_started:
        if not is_playing:
            stop_sound()
        else:
            play_sound(current_song_id)

_sound_library = {}
def play_sound(id):
    global is_playing, current_song_time
    path = PLAYLIST[id]["path"]
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    seconds = int(current_song_time["seconds"])
    minutes = int(current_song_time["minutes"])
    print(current_song_time)
    sound_seconds = minutes * 60 + seconds
    sound.play(0, sound_seconds)

def stop_sound():
    global is_playing
    pygame.mixer.stop() 
    is_playing = False

def next_song():
    global current_song_id, is_playing, current_song_time
    current_song_time = {"minutes": "0", "seconds": "0"}
    current_song_id = (current_song_id + 1) % len(PLAYLIST)
    update_song()
    if is_playing:
        play_sound(current_song_id)

def prev_song():
    global current_song_id, is_playing, current_song_time
    current_song_time = {"minutes": "0", "seconds": "0"}
    current_song_id = (current_song_id - 1) % len(PLAYLIST)
    update_song()
    if is_playing:
        play_sound(current_song_id)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.mixer.stop() 
                next_song()
            elif event.key == pygame.K_LEFT:
                pygame.mixer.stop() 
                prev_song()
            elif event.key == pygame.K_SPACE:
                update_song()
                toggle_song()

    screen.fill(Color.BACKGROUND.value)
    set_song_duration()

    screen.blit(heading_text, ((WIDTH / 2) - heading_text.get_width() // 2, (HEIGHT / 2) - 60))
    screen.blit(song_text, ((WIDTH / 2) - song_text.get_width() // 2, (HEIGHT / 2) - song_text.get_height() // 2))
    screen.blit(duration_text, ((WIDTH / 2) - duration_text.get_width() // 2, (HEIGHT / 2) + 25))

    if is_playing:    
        play_stop_image = stop_image
    else:
        play_stop_image = play_image
    screen.blit(play_stop_image, ((WIDTH / 2) - play_stop_image.get_width() // 2, (HEIGHT / 2) + 60))

    pygame.display.flip()
    clock.tick(60)
