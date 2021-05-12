"""例题12.5管理飞船的大部分行为"""
import pygame

class Ship():
    """管理飞船的大部分行为"""

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
    
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # 将每艘新飞船放在屏幕最左边的中间
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # 存储飞船中心点y坐标的小数值
        self.centery = float(self.rect.centery)

        # 上下移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船中心点的y值，而不是rect的中心点y值
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.centery更新rect对象
        self.rect.centery = self.centery
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)