import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Зайчик")

# Цвета
SAND_KING = (210, 180, 140)
LIGHT_SAND_KING = (240, 220, 180)
PAWS = (190, 160, 120)
TAIL = (255, 245, 225)
PINK = (255, 240, 230)
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 235)

def draw_ear(surface, start_pos, length, angle):
    ear_surface = pygame.Surface((20, length), pygame.SRCALPHA)
    pygame.draw.ellipse(ear_surface, SAND_KING, (0, 0, 20, length))
    pygame.draw.ellipse(ear_surface, PINK, (5, 5, 10, length - 10))
    rotated = pygame.transform.rotate(ear_surface, angle)
    surface.blit(rotated, rotated.get_rect(center=start_pos))

def draw_head(surface, x, y):
    pygame.draw.ellipse(surface, SAND_KING, (x, y, 250, 180))  # Голова
    pygame.draw.ellipse(surface, SAND_KING, (x+50, y-50, 120, 100))  # Мордочка
    pygame.draw.ellipse(surface, LIGHT_SAND_KING, (x+70, y-40, 70, 50))  # Внутренняя часть мордочки (поднята выше)

def draw_eyes(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x+90, y), 5)  # Левый глаз (поднят выше)
    pygame.draw.circle(surface, BLACK, (x+130, y), 5)  # Правый глаз (поднят выше)

def draw_nose(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x+110, y+20), 4)  # Нос (поднят выше)

def draw_whiskers(surface, x, y):
    for i in range(-10, 11, 10):
        pygame.draw.line(surface, BLACK, (x+110, y+20), (x+80, y+10+i), 1)  # Левые усы (подняты выше)
        pygame.draw.line(surface, BLACK, (x+110, y+20), (x+140, y+10+i), 1)  # Правые усы (подняты выше)

def draw_paws(surface, x, y):
    pygame.draw.circle(surface, PAWS, (x+30, y+150), 30)  # Левая передняя лапа
    pygame.draw.circle(surface, PAWS, (x+170, y+150), 30)  # Правая передняя лапа
    pygame.draw.circle(surface, PAWS, (x-10, y+80), 35)  # Левая задняя лапа
    pygame.draw.circle(surface, PAWS, (x+210, y+80), 35)  # Правая задняя лапа

def draw_hare(surface, x, y):
    draw_head(surface, x, y)
    draw_eyes(surface, x, y-20)  # Передаем новые координаты для глаз
    draw_nose(surface, x, y-20)  # Передаем новые координаты для носа
    draw_whiskers(surface, x, y-20)  # Передаем новые координаты для усов
    draw_ear(surface, (x+80, y-70), 140, -10)  # Левое ухо
    draw_ear(surface, (x+140, y-70), 140, 10)  # Правое ухо
    draw_paws(surface, x, y)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)
    draw_hare(screen, 300, 300)  # Рисуем зайчика в позиции (300, 300)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
