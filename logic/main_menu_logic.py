import pygame
from product.materials.Message import Message
from product.materials.Button import Button


def main_menu_logic(screen, music, volume):
    fps = 60
    clock = pygame.time.Clock()
    running = True
    mes = False
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    message = Message(0.2, 0.1, (0.6, 0.4), 'Да', 'Нет')
    play_btn = Button(0.3, 0.15, (0.4, 0.1), 'Играть')
    crt_img_btn = Button(0.3, 0.275, (0.4, 0.1), 'Редактор')
    stg_btn = Button(0.3, 0.4, (0.4, 0.1), 'Настройки')
    abt_btn = Button(0.3, 0.525, (0.4, 0.1), 'О нас')
    ext_btn = Button(0.3, 0.65, (0.4, 0.1), 'Выйти')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Exit'
            if event.type == pygame.MOUSEMOTION:
                if not mes:
                    play_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    crt_img_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    stg_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    abt_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    ext_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                else:
                    message.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not mes:
                    if play_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Game'
                    if crt_img_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Menu'
                    if stg_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Settings'
                    if abt_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        return 'Menu'
                    if ext_btn.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height()):
                        mes = True
                else:
                    res = message.mouse_in(event.pos[0], event.pos[1], screen.get_width(), screen.get_height())
                    if res:
                        if res == 'Да':
                            return 'Exit'
                        else:
                            mes = False

        screen.fill((190, 190, 190))
        play_btn.draw(screen)
        crt_img_btn.draw(screen)
        stg_btn.draw(screen)
        abt_btn.draw(screen)
        ext_btn.draw(screen)
        if mes:
            message.draw(screen, 'Вы хотите выйти?')
        pygame.display.flip()
        clock.tick(fps)
