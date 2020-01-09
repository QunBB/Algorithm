import numpy as np


class KnightTour:
    """
    马踏棋盘（骑士周游）小游戏，以"日"的走法将整个棋盘走满，并且不能重复走
    """

    def __init__(self, size):
        self.X = size
        self.Y = size
        # 棋盘的二维数组，用于记录每一步所走的位置
        self.chessboard = np.zeros([self.X, self.Y], dtype=np.int32)
        # 用于记录每个位置是否已经走过
        self.visited = np.full([self.X, self.Y], False, dtype=bool)
        # 是否完成游戏的标记
        self.finished = False
        # 用于存储所有解法
        self.all_solution = []

    def solution(self, x, y, get_all=False):
        """
        获取马踏棋盘的走法
        :param x: 出发位置的横坐标，从0开始
        :param y: 出发位置的纵坐标
        :param get_all: 是否获取所有走法
        :return:
        """
        if get_all:
            self.tour_all(x, y, 1)
            print('总共有 %d 种解法' % (len(self.all_solution)))
            for i in range(len(self.all_solution)):
                print('第%d种解法：' % (i + 1))
                print(self.all_solution[i])
        else:
            self.tour(x, y, 1)
            print(self.chessboard)

    def tour(self, x, y, step):
        """
        通过递归和回溯的方法寻找解法，找到一种解决即停止
        :param x: 当前位置的横坐标
        :param y: 当前位置的纵坐标
        :param step: 当前的步数
        :return:
        """
        self.visited[x][y] = True
        self.chessboard[x][y] = step
        nexts = self.get_next(x, y)
        # 通过贪心算法进行优化，按照下一步的所有可走位置的下一步的可走位置数量进行升序排序
        # 这样先进行递归的数量会比较少
        nexts.sort(key=lambda x: len(self.get_next(x[0], x[1])))
        for p in nexts:
            if not self.visited[p[0]][p[1]]:
                self.tour(p[0], p[1], step+1)

        if (step < self.X * self.Y) & (not self.finished):  # 如果已经无路可走但仍未结束，或者处于回溯过程中
            self.chessboard[x][y] = 0
            self.visited[x][y] = False
        else:  # 已经完成游戏
            self.finished = True

    def tour_all(self, x, y, step):
        """
        通过递归和回溯的方法寻找所有解法
        :param x: 当前位置的横坐标
        :param y: 当前位置的纵坐标
        :param step: 当前的步数
        :return:
        """
        self.visited[x][y] = True
        self.chessboard[x][y] = step
        nexts = self.get_next(x, y)
        # 通过贪心算法进行优化，按照下一步的所有可走位置的下一步的可走位置数量进行升序排序
        # 这样先进行递归的数量会比较少
        # nexts.sort(key=lambda x: len(self.get_next(x[0], x[1])))
        for p in nexts:
            if not self.visited[p[0]][p[1]]:
                self.tour_all(p[0], p[1], step+1)

        # 已经按照规则将棋盘走满，获得一种解法
        if step == self.X * self.Y:
            # print("====")
            # print(self.chessboard)
            self.all_solution.append(self.chessboard.copy())

        # 开始回溯，寻找其他解法
        self.chessboard[x][y] = 0
        self.visited[x][y] = False

    def get_next(self, x, y):
        """
        返回当前位置的下一步所有可走位置集合
        :return:
        """
        res = []
        if (x - 1 >= 0) & (y - 2 >= 0):
            res.append([x - 1, y - 2])

        if (x - 2 >= 0) & (y - 1 >= 0):
            res.append([x - 2, y - 1])

        if (x + 1 < self.X) & (y - 2 >= 0):
            res.append([x + 1, y - 2])

        if (x + 2 < self.X) & (y - 1 >= 0):
            res.append([x + 2, y - 1])

        if (x - 2 >= 0) & (y + 1 < self.Y):
            res.append([x - 2, y + 1])

        if (x - 1 >= 0) & (y + 2 < self.Y):
            res.append([x - 1, y + 2])

        if (x + 2 < self.X) & (y + 1 < self.Y):
            res.append([x + 2, y + 1])

        if (x + 1 < self.X) & (y + 2 < self.Y):
            res.append([x + 1, y + 2])

        return res


if __name__ == '__main__':
    game = KnightTour(5)
    game.solution(0, 0, True)
