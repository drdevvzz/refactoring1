import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Зайчик")

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


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.draw.ellipse(screen, SAND_KING, (300, 300, 250, 180))

    pygame.draw.ellipse(screen, SAND_KING, (350, 250, 120, 100))

    pygame.draw.ellipse(screen, LIGHT_SAND_KING, (370, 270, 70, 50))

    pygame.draw.circle(screen, BLACK, (390, 290), 5)
    pygame.draw.circle(screen, BLACK, (430, 290), 5)

    pygame.draw.circle(screen, BLACK, (410, 310), 4)

    for i in range(-10, 11, 10):
        pygame.draw.line(screen, BLACK, (410, 310), (380, 300 + i), 1)
        pygame.draw.line(screen, BLACK, (410, 310), (440, 300 + i), 1)

    draw_ear(screen, (380, 230), 140, -10)
    draw_ear(screen, (440, 230), 140, 10)

    pygame.draw.circle(screen, PAWS, (330, 450), 30)
    pygame.draw.circle(screen, PAWS, (470, 450), 30)
    pygame.draw.circle(screen, PAWS, (290, 380), 35)
    pygame.draw.circle(screen, PAWS, (510, 380), 35)

    pygame.draw.circle(screen, TAIL, (280, 370), 25)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
