"""存储让游戏《抓球》运行的函数"""
import sys
import pygame
from alien_ball_13_5 import Alien
from alien_ship_13_5 import Ship

def check_keydown_events(event, ship):
    """响应按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color) 
    ship.blitme() # 绘制飞船
    aliens.draw(screen) # 绘制外星人群

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_aliens(ai_settings, screen, ship, aliens):
    """更新外星人的位置，并删除需要消失的外星人"""
    # 具体更新外星人的位置,为编组aliens中的每个外星人调用alien.update()
    aliens.update()

    # 删除到达屏幕底部的外星人
    for alien in aliens.copy():
        if alien.check_edge():
            aliens.remove(alien)

    if len(aliens) == 0:
        print("alien hit bottom!!!")

    # 单个精灵（飞船）和编组之间矩形冲突检测，删除和飞船碰撞的外星人
    # 返回冲突的外星人列表，疑问：飞船不是精灵也可以检测？？？
    collisions = pygame.sprite.spritecollide(ship, aliens, True)

    if len(collisions) != 0:
        print("alien hit ship!!!")
    
    if len(aliens) == 0:
        # 新建一个外星人
        alien = Alien(ai_settings, screen)
        aliens.add(alien)
