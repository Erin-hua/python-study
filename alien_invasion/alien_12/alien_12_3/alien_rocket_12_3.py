"""管理火箭的大部分行为"""
import pygame

class Rocket():
    """管理火箭的大部分行为"""

    def __init__(self, ai_settings, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
    
        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # 将每艘新火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx # centerx只能存储整数值
        self.rect.centery = self.screen_rect.centery

        # 在火箭的属性centerx和centery中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭的位置"""
        # 更新火箭的centerx和centery值，而不是rect的centerx值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor 
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor

        # 根据self.centerx和centery更新rect对象
        # self.rect.centerx将只存储self.center的整数部分
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)