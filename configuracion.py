import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Invasión Espacial")

# Colores
BLANCO = (255, 255, 255)

# Fuente
FUENTE = pygame.font.Font("fuentes/HighlandGothicLightFLF.ttf", 33)
