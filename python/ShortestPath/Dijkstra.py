import numpy as np


class Graph:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

        self.dis = None  # 记录出发顶点到其他各个顶点的最短累计距离
        self.pre = None  # 记录出发顶点到其他各个顶点的前驱顶点
        self.visited = None  # 记录每个顶点是否已经访问过
        self.path = None  # 记录出发顶点到其他各个顶点的最短路径

    def init(self, index):
        """
        初设化Dijkstra算法
        :param index: 出发顶点
        :return:
        """
        self.dis = np.full([len(self.vertex), ], np.inf)
        self.pre = [-1] * len(self.vertex)
        self.visited = [False] * len(self.vertex)
        self.path = [[] for i in range(len(self.vertex))]

        self.dis[index] = 0
        self.visited[index] = True
        self.path[index].append(self.vertex[index])

    def djs(self, index, show=True):
        """
        Dijkstra算法的执行方法：以index为出发顶点，计算index达到其他各个顶点的最短距离
        :param show:
        :param index:
        :return:
        """
        start_index = index
        self.init(index)
        self.update(index)
        for i in range(1, len(self.vertex)):
            index = self.update_vertex()
            self.update(index)
        if show:
            self.show_djs(start_index)

    def update(self, index):
        """
        以index为访问顶点，更新每个顶点的前驱顶点和累计距离
        :param index:
        :return:
        """
        for i in range(len(self.vertex)):
            length = self.dis[index] + self.weight[index][i]
            # 当遇到能够能以更短距离达到自己的出发顶点时，则进行更新
            if (length < self.dis[i]) & (not self.visited[i]):
                self.pre[i] = index  # 更换前驱节点
                self.dis[i] = length  # 更换累计距离
                # 更换路径
                self.path[i] = self.path[index].copy()  # 前驱节点的最优路径
                self.path[i].append(self.vertex[i])  # 再加上自己

    def update_vertex(self):
        """
        更新下次的访问顶点
        :return:
        """
        dis = np.inf
        index = 0
        for i in range(len(self.vertex)):
            if (not self.visited[i]) & (dis > self.dis[i]):
                dis = self.dis[i]
                index = i
        self.visited[index] = True
        return index

    def show_djs(self, index):
        """
        打印Dijkstra算法的结果：出发顶点到各个顶点的最短距离和最优路径
        :param index:
        :return:
        """
        for i in range(len(self.vertex)):
            if i == index:
                continue
            print("{}到{}的最短距离为{}，最优路径为-->{}".format(
                self.vertex[index], self.vertex[i], self.dis[i], self.path[i]))


if __name__ == '__main__':
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[np.inf, 5, 7, np.inf, np.inf, np.inf, 2],
            [5, np.inf, np.inf, 9, np.inf, np.inf, 3],
            [7, np.inf, np.inf, np.inf, 8, np.inf, np.inf],
            [np.inf, 9, np.inf, np.inf, np.inf, 4, np.inf],
            [np.inf, np.inf, 8, np.inf, np.inf, 5, 4],
            [np.inf, np.inf, np.inf, 4, 5, np.inf, 6],
            [2, 3, np.inf, np.inf, 4, 6, np.inf]]
    graph = Graph(vertex, weight)
    graph.djs(3)
