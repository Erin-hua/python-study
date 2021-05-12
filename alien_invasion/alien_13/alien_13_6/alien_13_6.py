"""例题13.6角色（飞船）和球（外星人）代码"""
import pygame
from alien_settings_13_6 import Settings
from alien_game_stats_13_6 import GameStats
from alien_ship_13_6 import Ship
from alien_ball_13_6 import Alien
import alien_game_functions_13_6 as gf
from pygame.sprite import Group

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("例题13-6") # 设置屏幕顶部的标题

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一个飞船(角色)，一个外星人（球）编组
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    aliens = Group()
    aliens.add(alien)
  
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship) # 按键响应对飞船（角色）的位置是否移动进行设定

        # 游戏处于活动状态时，才需要更新游戏元素的位置
        if stats.game_active:
            ship.update() # 具体更新飞船(角色)的位置
            # 具体更新外星人（球）的位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens)

run_game() 