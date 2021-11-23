import pygame
    
system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)

bitmap_1 = pygame.cursors.Cursor(*pygame.cursors.arrow)
bitmap_2 = pygame.cursors.Cursor(
(24, 24), (0, 0), *pygame.cursors.compile(pygame.cursors.thickarrow_strings)
)

surf = pygame.Surface((40, 40)) # you could also load an image 
surf.fill((120, 50, 50))        # and use that as your surface
color = pygame.cursors.Cursor((20, 20), surf)

cursors = [system, bitmap_1, bitmap_2, color]
