import pygame
import sys
from game import game
from funct import load_image

WIDTH = 1280
HEIGHT = 720

clock = pygame.time.Clock()


def return_to_main_menu(mouse_pos):
    print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x in range(0, 75) and y in range(0, 85):
        start_screen_menu()


def play(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x in range(495, 720) and y in range(250, 450):
        game()
    elif x in range(745, 895) and y in range(315, 450):
        statistics_window()


def terminate():
    pygame.quit()
    sys.exit()


def statistics_window():
    fon = pygame.transform.scale(load_image('Statistics.png'), (WIDTH, HEIGHT))
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_to_main_menu(event.pos)
        pygame.display.flip()


def start_screen_menu():
    fon_menu = pygame.transform.scale(load_image('Geometry_Dash_menu.png'), (WIDTH, HEIGHT))
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.blit(fon_menu, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play(event.pos)
                screen.blit(fon_menu, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    start_screen_menu()
