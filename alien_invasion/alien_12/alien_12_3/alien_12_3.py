"""例题12.3火箭代码"""
import pygame
from alien_settings_12_3 import Settings
from alien_rocket_12_3 import Rocket
import alien_game_functions_12_3 as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("Rocket") # 设置屏幕顶部的标题

    # 创建一艘火箭
    rocket = Rocket(ai_settings, screen)
  
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(rocket) # 按键响应对火箭的位置是否移动进行设定
        rocket.update() # 具体更新火箭的位置

        # 更新屏幕上的火箭，并切换到新屏幕
        gf.update_screen(ai_settings, screen, rocket)

run_game() 