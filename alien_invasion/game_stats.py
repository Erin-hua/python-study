"""跟踪游戏统计信息的类"""

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 最高分在游戏运行期间不能被重置
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        # 每次开始游戏时都重置这些信息
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # 每次开始新游戏时都重置等级
        self.level = 1