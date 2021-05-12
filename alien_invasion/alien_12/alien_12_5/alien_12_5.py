"""例题12.5代码"""
import pygame
from alien_settings_12_5 import Settings
from alien_ship_12_5 import Ship
import alien_game_functions_12_5 as gf
from pygame.sprite import Group

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("例题12.5飞船上下移动并向右发射子弹") # 设置屏幕顶部的标题

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
  
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets) # 按键响应对飞船、子弹的位置是否移动进行设定
        ship.update() # 具体更新飞船的位置
        gf.update_bullets(bullets, ship) # 具体更新子弹的位置
        gf.update_screen(ai_settings, screen, ship, bullets) # 更新屏幕上的图像，并切换到新屏幕

run_game() 