import pygame
from product.materials.Message import Message
from product.materials.Button import Button


def connect_logic(screen, music, volume):
    fps = 60
    clock = pygame.time.Clock()
    running = True
    mes = False
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    message = Message(0.2, 0.1, (0.6, 0.4), 'Да', 'Нет')
    rebus_btn = Button(0.2, 0.15, (0.6, 0.1), 'Ребусы/Загадки')
    matching_btn = Button(0.2, 0.275, (0.6, 0.1), 'Пятнашки')
    puzzle_btn = Button(0.2, 0.4, (0.6, 0.1), 'Пазлы')
    ext_btn = Button(0.2, 0.75, (0.6, 0.1), 'Выйти в меню')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Exit'
            if event.type == pygame.MOUSEMOTION:
                if not mes:
                    rebus_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    matching_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    puzzle_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    ext_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                else:
                    message.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not mes:
                    if rebus_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Rebus'
                    if matching_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Mutching'
                    if puzzle_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Puzzle'
                    if ext_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        mes = True
                else:
                    res = message.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    if res:
                        if res == 'Да':
                            return 'Menu'
                        else:
                            mes = False

        screen.fill((190, 190, 190))
        rebus_btn.draw(screen)
        matching_btn.draw(screen)
        puzzle_btn.draw(screen)
        ext_btn.draw(screen)
        if mes:
            message.draw(screen, 'Вы хотите выйти в меню?')
        pygame.display.flip()
        clock.tick(fps)
