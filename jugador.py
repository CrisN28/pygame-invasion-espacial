import pygame
from configuracion import pantalla


class Jugador:
    def __init__(self):
        self.imagen = pygame.image.load("recursos/transbordador-espacial.png").convert_alpha()
        self.hitbox = self.imagen.get_rect(center=(368, 536))
        self.velocidad = 5

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.hitbox.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.hitbox.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.hitbox.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.hitbox.y += self.velocidad

        self.hitbox.clamp_ip(pantalla.get_rect())

    def dibujar(self):
        pantalla.blit(self.imagen, self.hitbox)
