from configuracion import *
from sonidos import sonido_colision
from menu_principal import *
import random

# Inicializar Pygame
pygame.init()
mixer.init()

# Configuración de pantalla
"""pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Invasión Espacial")"""

# Cargar imágenes y fuentes una sola vez
fondo = pygame.image.load("recursos/back.png").convert()
fuente_puntaje = pygame.font.Font("fuentes/HighlandGothicLightFLF.ttf", 30)
fuente_mensaje = pygame.font.Font("fuentes/HighlandGothicLightFLF.ttf", 25)

# Inicialización de objetos
jugador = Jugador()
bala = Bala()
enemigos = [Enemigo() for _ in range(5)]
reloj = pygame.time.Clock()
puntaje = 0
jugador_esta_vivo = True  # Variable para determinar si el jugador sigue vivo


# Bucle principal
juego = True
while juego:
    reloj.tick(60)  # Control de FPS

    # Dibujar fondo
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and jugador_esta_vivo:
                bala.disparar(jugador.hitbox.midtop)
            elif evento.key == pygame.K_ESCAPE:
                juego = False

    if jugador_esta_vivo:
        # Actualizar y dibujar jugador
        jugador.mover()
        jugador.dibujar()

        # Actualizar y dibujar bala
        bala.mover()
        bala.dibujar()

        # Actualizar y dibujar enemigos
        for enemigo in enemigos:
            enemigo.mover()
            enemigo.dibujar()

            # Verificar colisión con bala
            for proyectil in bala.balas[:]:
                if enemigo.hitbox.colliderect(proyectil):
                    sonido_colision.play()
                    puntaje += 1
                    enemigo.hitbox.y = random.randint(-100, -70)
                    enemigo.hitbox.x = random.randint(20, 736)
                    bala.balas.remove(proyectil)

            # Verificar colisión con jugador
            if enemigo.hitbox.colliderect(jugador.hitbox):
                mixer.music.stop()  # Detener la música
                jugador_esta_vivo = False  # El jugador ha perdido
                resultado = mostrar_menu_final(pantalla, fondo, FUENTE)  # Mostrar el menú final con opciones
                if resultado == "reiniciar":  # Si el jugador elige reiniciar
                    (puntaje, jugador_esta_vivo, enemigos, bala, jugador) = reiniciar_juego()
                    break  # Reiniciar el ciclo de juego
                elif resultado is None:  # Si el jugador elige salir
                    juego = False
                    break  # Salir del ciclo del juego

    # Mostrar puntaje y actualizar pantalla
    mostrar_puntaje(puntaje, FUENTE, pantalla)
    pygame.display.flip()

pygame.quit()
sys.exit()
