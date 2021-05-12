"""例题13.5角色（飞船）和球（外星人）代码"""
import pygame
from alien_settings_13_5 import Settings
from alien_ship_13_5 import Ship
from alien_ball_13_5 import Alien
import alien_game_functions_13_5 as gf
from pygame.sprite import Group

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("例题13-5") # 设置屏幕顶部的标题

    # 创建一个飞船(角色)，一个外星人（球）编组
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    aliens = Group()
    aliens.add(alien)
  
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship) # 按键响应对飞船（角色）的位置是否移动进行设定
        ship.update() # 具体更新飞船(角色)的位置
        gf.update_aliens(ai_settings, screen, ship, aliens) # 具体更新外星人（球）的位置
        gf.update_screen(ai_settings, screen, ship, aliens) # 更新屏幕上的图像，并切换到新屏幕

run_game() 