import pygame

pygame.init()
pygame.mixer.init()

sounds = ['owl.mp3', 'steve.mp3', 'water.mp3']
sound_index = 0
current_sound = sounds[sound_index]

def Play():
    global sound_index, sounds, current_sound
    pygame.mixer.music.load(current_sound)
    pygame.mixer.music.play()

def Next():
    global sound_index, sounds, current_sound
    sound_index = (sound_index + 1) % len(sounds)
    current_sound = sounds[sound_index]
    pygame.mixer.music.load(current_sound)
    pygame.mixer.music.play()

def Previous():
    global sound_index, sounds, current_sound
    sound_index = (sound_index - 1) % len(sounds)
    current_sound = sounds[sound_index]
    pygame.mixer.music.load(current_sound)
    pygame.mixer.music.play()
def Pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

screen = pygame.display.set_mode((600,600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Play()
            elif event.key == pygame.K_RIGHT:
                Next()
            elif event.key == pygame.K_LEFT:
                Previous()
            elif event.key == pygame.K_SPACE:
                Pause()
    screen.fill((255, 255, 255))
    pygame.display.flip()
