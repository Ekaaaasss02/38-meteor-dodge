
import pygame

SPEED = 9
COLOR = (80, 240, 255)


class Laser:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 3, y - 12, 6, 16)

    def update(self):
        self.rect.y -= SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR, self.rect, border_radius=3)
        pygame.draw.line(
            screen,
            (220, 255, 255),
            (self.rect.centerx, self.rect.top),
            (self.rect.centerx, self.rect.bottom),
            2,
        )

    def off_screen(self):
        return self.rect.bottom < 0