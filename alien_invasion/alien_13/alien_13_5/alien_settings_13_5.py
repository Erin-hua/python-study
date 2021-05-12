"""例题13.5的设置类"""
class Settings():
    """存储例题13.5的设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船（角色）设置
        self.ship_speed_factor = 1.5 # 飞船移动速度的初始值

        # 外星人（球）设置
        self.alien_speed_factor = 1