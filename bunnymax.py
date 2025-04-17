import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500
FPS = 60

# Цвета
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
PINK = (255, 180, 180)
BLACK = (0, 0, 0)

def draw_hare(screen):
    body_x, body_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40
    head_x, head_y = body_x, body_y - 50

    # Тело
    pygame.draw.ellipse(screen, GRAY, (body_x - 120, body_y - 60, 200, 120))

    # Голова
    pygame.draw.circle(screen, GRAY, (head_x, head_y), 50)

    # Уши
    draw_ear(screen, head_x - 40, head_y - 40, is_left=True)
    draw_ear(screen, head_x + 40, head_y - 40, is_left=False)

    # Лапы
    pygame.draw.ellipse(screen, GRAY, (body_x - 85, body_y + 25, 30, 40))
    pygame.draw.ellipse(screen, GRAY, (body_x + 55, body_y + 25, 30, 40))

    # Лицо
    draw_face(screen, head_x, head_y)


def draw_body(x, y):

    pygame.draw.ellipse(screen, GRAY, (x - 120, y - 60, 200, 120))

def draw_ear(screen, x, y, is_left=True):
    offset = -1 if is_left else 1
    points = [
        (x, y),
        (x + offset * 30, y - 80),
        (x + offset * 15, y - 100)
    ]
    pygame.draw.polygon(screen, GRAY, points)

    inner_points = [
        (x, y + 5),
        (x + offset * 25, y - 60),
        (x + offset * 12, y - 85)
    ]
    pygame.draw.polygon(screen, PINK, inner_points)

def draw_face(screen, x, y):
    """Рисует лицо зайца (глаза и нос)"""
    # Глаза
    for offset in (-20, 20):
        pygame.draw.circle(screen, WHITE, (x + offset, y - 10), 10)
        pygame.draw.circle(screen, BLACK, (x + offset, y - 10), 5)

    # Нос
    pygame.draw.circle(screen, PINK, (x, y + 10), 8)
    pygame.draw.circle(screen, BLACK, (x, y + 10), 3)


def draw_hare():
    
    body_x, body_y = width // 2, height // 2 + 40

    draw_body(body_x, body_y)
    draw_head(body_x, body_y - 50)
    draw_ear(body_x - 40, body_y - 90, left=True)
    draw_ear(body_x + 40, body_y - 90, left=False)
    draw_leg(body_x - 60, body_y + 40, left=True)
    draw_leg(body_x + 30, body_y + 40, left=False)
    draw_face(body_x, body_y - 50)



def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_hare()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
