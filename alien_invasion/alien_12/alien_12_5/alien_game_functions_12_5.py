"""存储大量让游戏《外星人入侵》运行的函数"""
import sys
import pygame
from alien_bullet_12_5 import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键事件"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开事件"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color) 
    # 在飞船和外星人前面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # 绘制飞船

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets, ship):
    """更新子弹的位置，并删除已消失的子弹"""
    # 具体更新子弹的位置,为编组bullets中的每颗子弹调用bullet.update()
    bullets.update()

    # 删除已消失的子弹
    # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    for bullet in bullets.copy():
        if bullet.rect.left > ship.screen_rect.right: # 表示子弹的rect的left属性超过屏幕的right属性，表明子弹已穿过屏幕右端
            bullets.remove(bullet)
    # print(len(bullets))