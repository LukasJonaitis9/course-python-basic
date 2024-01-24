import pygame
import os

pygame.init()


pygame.mixer.init()


screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Simple MP3 Player")


mp3_folder = "/path/to/your/mp3/files"


mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]


pygame.mixer.music.load(os.path.join(mp3_folder, mp3_files[0]))


current_track = 0
playing = False


def play_track(track_index):
    global playing
    pygame.mixer.music.load(os.path.join(mp3_folder, mp3_files[track_index]))
    pygame.mixer.music.play()
    playing = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(mp3_files)
                play_track(current_track)
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(mp3_files)
                play_track(current_track)

    pygame.display.flip()

pygame.quit()