import pygame
import random
from configuracion import pantalla


class Enemigo:
    def __init__(self):
        self.imagen = pygame.image.load("recursos/ovni_enemigo.png").convert_alpha()
        self.hitbox = self.imagen.get_rect(center=(random.randint(20, 736), random.randint(-100, -70)))
        self.velocidad = random.randint(2, 4)  # Variar velocidad de los enemigos

    def mover(self):
        self.hitbox.y += self.velocidad
        if self.hitbox.y > 600:
            self.hitbox.y = random.randint(-100, -70)
            self.hitbox.x = random.randint(20, 736)
            self.velocidad = random.randint(2, 4)  # Nueva velocidad al reiniciar

    def dibujar(self):
        pantalla.blit(self.imagen, self.hitbox)
