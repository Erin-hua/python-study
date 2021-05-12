"""例题12.2的设置类"""
import pygame

class Setting():
    """设置位图的位置和背景色"""

    def __init__(self, screen, bg_color):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载位图图像并获取其外接矩形
        self.image = pygame.image.load('images/my_cat_b.bmp')
        #self.image.fill(bg_color) # 将位图的背景色设置为屏幕的背景色失败
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将该位图绘制到屏幕中央
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """将该位图绘制到屏幕中央"""
        self.screen.blit(self.image, self.rect)
