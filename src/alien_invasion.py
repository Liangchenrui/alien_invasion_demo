import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 设置背景色
    bg_color = (230,230,230)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()