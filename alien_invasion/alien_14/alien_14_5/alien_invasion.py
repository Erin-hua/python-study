"""例题14.4章外星飞船代码"""
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button 
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 整个屏幕的初始设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # 设置屏幕的宽和高
    pygame.display.set_caption("Alien Invasion") # 设置屏幕顶部的标题

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb =Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
  
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # 按键响应对飞船、子弹的位置是否移动进行设定
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        # 游戏处于活动状态时，才需要更新游戏元素的位置
        if stats.game_active:
            ship.update() # 具体更新飞船的位置
            # 具体更新子弹的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game() 