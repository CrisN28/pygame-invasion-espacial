import pygame
from configuracion import BLANCO
from enemigo import Enemigo
from bala import Bala
from jugador import Jugador
import sys
from pygame import mixer


def mostrar_puntaje(puntaje, fuente, pantalla):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))


def mostrar_mensaje(texto, fuente, pantalla):
    # Crear superficie con el texto
    texto_renderizado = fuente.render(texto, True, (255, 255, 255))  # Blanco como color del texto
    # Obtener el rectángulo centrado en la pantalla
    texto_rect = texto_renderizado.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))
    # Dibujar el texto en la pantalla
    pantalla.blit(texto_renderizado, texto_rect)


def mostrar_menu_final(pantalla, fondo, fuente):
    # Mostrar fondo pero sin cambiarlo
    pantalla.blit(fondo, (0, 0))  # Mantener el fondo original
    mostrar_mensaje("Perdiste! Pulsa R para reiniciar o Q para salir.", fuente, pantalla)
    pygame.display.flip()

    # Esperar que el jugador elija
    espera = True
    while espera:
        for evento_juego in pygame.event.get():
            if evento_juego.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento_juego.type == pygame.KEYDOWN:
                if evento_juego.key == pygame.K_r:  # Reiniciar
                    return "reiniciar"
                elif evento_juego.key == pygame.K_q:  # Salir
                    pygame.quit()
                    sys.exit()


def reiniciar_juego():
    mixer.music.play(-1)
    enemigos = [Enemigo() for _ in range(5)]
    bala = Bala()
    jugador = Jugador()
    return 0, True, enemigos, bala, jugador
