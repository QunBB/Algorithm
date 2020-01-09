import numpy as np


class Floyd:

    def __init__(self, vertex, dis):
        self.vertex = vertex
        self.dis = dis

        self.pre_arr = np.repeat(self.vertex, len(self.vertex)).reshape([len(self.vertex), len(self.vertex)])
        self.path = dict()  # 存储最优路径
        # 将一开始连通的顶点添加到路径中
        for i in range(self.dis.shape[0]):
            for j in range(self.dis.shape[1]):
                if self.dis[i][j] != np.inf:
                    self.set_path(i, j)

    def floyd(self):
        # 将每个顶点都作为中间顶点遍历一次
        for k in range(len(self.vertex)):
            # 获取当前可以到达顶点k的所有顶点
            vs = np.where(self.dis[k] != np.inf)[0]
            if len(vs) < 2:
                continue
            # 遍历所有可以将顶点k当作中间顶点的情况
            for i1 in range(len(vs)):
                for i2 in range(i1+1, len(vs)):
                    v1 = vs[i1]
                    v2 = vs[i2]
                    temp = self.dis[v1][k] + self.dis[v2][k]
                    if temp < self.dis[v1][v2]:
                        self.dis[v1][v2] = temp
                        self.dis[v2][v1] = temp
                        self.update_path(v1, v2, self.get_path(v1, k), self.get_path(k, v2))
                        self.update_path(v2, v1, self.get_path(v2, k), self.get_path(k, v1))

    def get_path(self, i, j):
        """
        获取两个顶点的最短路径
        :param i:
        :param j:
        :return:
        """
        return self.path["{}->{}".format(self.vertex[i], self.vertex[j])]

    def set_path(self, i, j):
        """
        设置两个顶点的最短路径，用list存储
        :param i:
        :param j:
        :return:
        """
        self.path["{}->{}".format(self.vertex[i], self.vertex[j])] = [self.vertex[i], self.vertex[j]]

    def update_path(self, i, j, l1: list, l2: list):
        """
        更新两个顶点的最短路径
        :param i:
        :param j:
        :param l1:
        :param l2:
        :return:
        """
        self.path["{}->{}".format(self.vertex[i], self.vertex[j])] = l1 + l2[1:]


if __name__ == '__main__':
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[np.inf, 5, 7, np.inf, np.inf, np.inf, 2],
              [5, np.inf, np.inf, 9, np.inf, np.inf, 3],
              [7, np.inf, np.inf, np.inf, 8, np.inf, np.inf],
              [np.inf, 9, np.inf, np.inf, np.inf, 4, np.inf],
              [np.inf, np.inf, 8, np.inf, np.inf, 5, 4],
              [np.inf, np.inf, np.inf, 4, 5, np.inf, 6],
              [2, 3, np.inf, np.inf, 4, 6, np.inf]]
    floyd = Floyd(vertex, np.array(weight))
    floyd.floyd()
    print(floyd.path)
