"""例题12.4执行代码"""
import pygame
from alien_settings_12_4 import Settings
import alien_game_functions_12_4 as gf 

def run_game():
    """初始化pygame、设置和屏幕对象"""
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("测试按键") # 设置屏幕顶部的标题

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events() # 按键后终端输出按的键的值

        # 更新屏幕，必须包含
        gf.update_screen(ai_settings, screen)

run_game()

