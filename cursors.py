import pygame
#Cursor Style Settings
system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
bitmap_1 = pygame.cursors.Cursor(*pygame.cursors.arrow)
bitmap_2 = pygame.cursors.Cursor((24, 24), (0, 0), *pygame.cursors.compile(pygame.cursors.thickarrow_strings))
cursors = [system, bitmap_1, bitmap_2]
