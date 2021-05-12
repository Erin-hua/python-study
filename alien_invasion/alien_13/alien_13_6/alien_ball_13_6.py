"""例题13.6-管理外星人（球）的行为"""
import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """表示单个外星人（球）的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人（球）并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人(球)图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 外星人（球）在屏幕顶端，x坐标是随机的
        self.rect.bottom = self.rect.height
        self.rect.x = randint(0, self.screen_rect.right - self.rect.width)

        # 存储外星人（球）的准确底部的Y坐标
        self.bottom = float(self.rect.bottom)

    def check_edge(self):
        """如果外星人（球）到达屏幕底部，就返回True"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """向下移动外星人（球）"""
        self.bottom += self.ai_settings.alien_speed_factor
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制外星人（球）"""
        self.screen.blit(self.image, self.rect)
