import pygame 
import sys 
import time

pygame.init()

screen_width=800

screen_heigth=600

screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.FULLSCREEN)

image_path = "C:/Users/ismae/OneDrive/Imágenes/Pruebas/cor.jpg"

image = pygame.image.load(image_path)

image = pygame.transform.scale(image, (screen_width, screen_heigth))

screen.blit(image, (0,0))
pygame.display.flip()

tiempo_mostrado=10

tiempo_inicial = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tiempo_actual = time.time()

    if tiempo_actual - tiempo_inicial >= tiempo_mostrado:
        running = False