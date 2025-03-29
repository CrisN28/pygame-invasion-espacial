from pygame import mixer
import pygame


# Inicializamos el mixer solo una vez
mixer.init()

# Constantes para los volúmenes
VOLUMEN_NORMAL = 0.09

# Cargar sonidos (si los archivos no existen, se captura el error)
try:
    sonido_disparo = mixer.Sound("recursos/disparo.mp3")
    sonido_disparo.set_volume(VOLUMEN_NORMAL)
except pygame.error as e:
    print(f"Error al cargar el sonido de disparo: {e}")

try:
    sonido_colision = mixer.Sound("recursos/Golpe.mp3")
    sonido_colision.set_volume(VOLUMEN_NORMAL)
except pygame.error as e:
    print(f"Error al cargar el sonido de colisión: {e}")

# Cargar música de fondo
try:
    mixer.music.load("recursos/Musica_fondo.mp3")
    mixer.music.set_volume(VOLUMEN_NORMAL)
    mixer.music.play(-1)  # Reproducción en bucle
except pygame.error as e:
    print(f"Error al cargar la música de fondo: {e}")
