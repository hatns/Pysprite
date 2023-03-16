import pygame

def draw_overlay(surface):
    pygame.draw.rect(surface, (0,0,0), (512, 0, 2, 512))
    pygame.draw.rect(surface, (0,0,0), (512+128-2, 0, 2, 512))
    pygame.draw.rect(surface, (0,0,0), (512, 0, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 64, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 128, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 192, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 256, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 320, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 352, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 384, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 416, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 448, 128, 2))
    pygame.draw.rect(surface, (0,0,0), (512, 510, 128, 2))

    pygame.draw.rect(surface, (50,50,50), (512, 32, 128, 2))
    pygame.draw.rect(surface, (50,50,50), (512+64, 32, 2, 32))

    pygame.draw.rect(surface, (50,50,50), (512, 96, 128, 2))
    pygame.draw.rect(surface, (50,50,50), (512+64, 96, 2, 32))

    pygame.draw.rect(surface, (50,50,50), (512, 160, 128, 2))
    pygame.draw.rect(surface, (50,50,50), (512+64, 160, 2, 32))

    pygame.draw.rect(surface, (50,50,50), (512, 224, 128, 2))
    pygame.draw.rect(surface, (50,50,50), (512+64, 224, 2, 32))

    pygame.draw.rect(surface, (50,50,50), (512, 288, 128, 2))
    pygame.draw.rect(surface, (50,50,50), (512+64, 32, 2, 32))
