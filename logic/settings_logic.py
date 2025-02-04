import pygame
from product.materials.Button import Button
from product.materials.Slider import Slider
from product.materials.Message import Message


def settings_logic(screen, music, volume):
    fps = 60
    clock = pygame.time.Clock()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    mes = ''
    font = pygame.font.Font(None, int(screen.get_height() * 0.1))
    text_permission = font.render('Разрешение', True, (95, 60, 125))
    text_volume = font.render('Громкость музыки', True, (95, 60, 125))
    size_btns = [Button(0.25, 0.1625, (0.5, 0.1), '350x300'),
                 Button(0.25, 0.2875, (0.5, 0.1), '500x420'),
                 Button(0.25, 0.4125, (0.5, 0.1), '700x600')]
    ext_btn = Button(0.35, 0.85, (0.3, 0.1), 'Выйти')
    slider = Slider(0.15, 0.7, (0.6, 0.1), 0, 100, 50, orientation='horizontal')
    message = Message(0.2, 0.3125, (0.6, 0.4), 'Да', 'Нет')

    while True:
        for event in pygame.event.get():
            if mes == '':
                if event.type == pygame.QUIT:
                    return 'Exit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mes = 'Выйти в меню'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in size_btns:
                            if button.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(),
                                               screen.get_height()):
                                pygame.display.set_mode(tuple(map(int, button.text.split('x'))))
                                break
                        if slider.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(), screen.get_height()):
                            slider.LMB = True
                            print(1)
                        if ext_btn.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(),
                                            screen.get_height()):
                            mes = 'Выйти в меню'
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for button in size_btns:
                            button.mouse_at_button = False
                        slider.LMB = False
                if event.type == pygame.MOUSEMOTION:
                    flag = True
                    for button in size_btns:
                        if button.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(), screen.get_height()):
                            flag = False
                            break
                    if slider.LMB and flag:
                        slider.motion(event.rel[0], screen.get_width(), screen.get_height())
                        pygame.mixer.music.set_volume(round(slider.value) / 100)
                    ext_btn.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(), screen.get_height())
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        result = message.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(),
                                                  screen.get_height())
                        if result == 'Да':
                            return 'Menu'
                        elif result == 'Нет':
                            message.fir_btn_txt.mouse_at_button = False
                            message.sec_btn_txt.mouse_at_button = False
                            mes = ''
                if event.type == pygame.MOUSEMOTION:
                    message.mouse_in(event.pos[0] - 1, event.pos[1] - 1, screen.get_width(), screen.get_height())

        screen.fill((190, 190, 190))
        for button in size_btns:
            button.draw(screen)
        ext_btn.draw(screen)
        slider.draw(screen)
        if mes:
            message.draw(screen, mes)
        screen.blit(text_permission, (int(screen.get_width() - text_permission.get_width()) // 2,
                                      int(screen.get_height() * 0.05) +
                                      (int(screen.get_height() * 0.1) - text_permission.get_height()) // 2))
        screen.blit(text_volume, (int(screen.get_width() - text_volume.get_width()) // 2,
                                  int(screen.get_height() * 0.6) +
                                  (int(screen.get_height() * 0.1) - text_volume.get_height()) // 2))
        pygame.display.flip()
        clock.tick(fps)
