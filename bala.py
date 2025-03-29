import pygame
from configuracion import pantalla
from sonidos import sonido_disparo


class Bala:
    def __init__(self):
        self.imagen = pygame.image.load("recursos/bala.png").convert_alpha()
        self.balas = []  # Lista para múltiples balas
        self.velocidad = 8
        self.limite_balas = 2  # Número máximo de balas

    def disparar(self, posicion):
        # Solo disparar si no hay más de 2 balas
        if len(self.balas) < self.limite_balas:
            nueva_bala = self.imagen.get_rect(midtop=posicion)
            self.balas.append(nueva_bala)
            sonido_disparo.play()

    def mover(self):
        for bala in self.balas[:]:  # Iterar sobre una copia para eliminar elementos sin errores
            bala.y -= self.velocidad
            if bala.bottom < 0:
                self.balas.remove(bala)

    def dibujar(self):
        for bala in self.balas:
            pantalla.blit(self.imagen, bala)
