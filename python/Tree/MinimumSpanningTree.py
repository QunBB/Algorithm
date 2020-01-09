import numpy as np


class Graph:
    """
    图的构造类
    """
    def __init__(self, vertex_num):
        """
        :param vertex_num: 顶点的数量
        """
        self.vertex_num = vertex_num
        self.vertexs = None
        self.weights = None

    def create(self, vertexs, weights):
        """
        :param vertexs: 所有顶点集合
        :param weights: 边的邻接矩阵，二维数组
        :return:
        """
        self.vertexs = vertexs
        self.weights = weights


class MinimumSpanningTree:
    """
     通过构建最小生成树，解决修路：要将所有顶点连通，并且使用的费用最低即权值之和最小
    """
    def import_graph(self, graph: Graph):
        self.graph = graph

    def prim(self, start):
        """
        利用普利姆算法构建最小生成树
        :param start:
        :return:
        """
        # 用于判断每个顶点是否已经访问的list
        visited = [False] * self.graph.vertex_num
        visited[start] = True

        for k in range(1, self.graph.vertex_num):
            min_weight = 10000
            i1 = -1
            i2 = -1

            # 对所有已经加入（已经访问过）的顶点，在它们的所有未访问过的边中找到权值weight最小的边，加入结果集，并标记为已访问过
            for i in range(self.graph.vertex_num):
                if not visited[i]:
                    continue
                for j in range(self.graph.vertex_num):
                    if (self.graph.weights[i][j] < min_weight) & (not visited[j]):
                        min_weight = self.graph.weights[i][j]
                        i1 = i
                        i2 = j
            visited[i2] = True
            print('%s -> %s : %d' % (self.graph.vertexs[i1], self.graph.vertexs[i2], min_weight))

    def kruskal(self):
        """
        利用克鲁斯卡尔算法构建最小生成树
        :return:
        """
        ends = [0] * self.graph.vertex_num  # 用于存储每个顶点的终点

        edges = []  # 用于存储排序后的边
        # 开始进行排序
        # 遍历邻接矩阵，将边提取出来的同时插入edges，并保证有序
        visited = [False] * self.graph.vertex_num
        for i in range(self.graph.vertex_num):
            for j in range(self.graph.vertex_num):
                if visited[j]:
                    continue
                if self.graph.weights[i][j] != 10000:
                    index = len(edges)
                    for n in range(len(edges)):
                        if self.graph.weights[i][j] < weights[edges[n][0]][edges[n][1]]:
                            index = n
                            break
                    edges.insert(index, (i, j))
            visited[i] = True

        # 开始克鲁斯卡尔算法
        # 选取权值最小的n-1条不构成回路的边，即为最小生成树
        selects = []
        for edge in edges:
            if len(selects) > self.graph.vertex_num - 1:
                break
            # 首先判断是否构成回路
            end1 = self.get_end(edge[0], ends)
            end2 = self.get_end(edge[1], ends)
            if end1 == end2:
                continue
            elif end1 > end2:
                ends[end2] = end1  # 更新终点数组
                selects.append((self.graph.vertexs[edge[0]], self.graph.vertexs[edge[1]]))
            else:
                ends[end1] = end2
                selects.append((self.graph.vertexs[edge[0]], self.graph.vertexs[edge[1]]))
        print(selects)

    def get_end(self, v, ends):
        """
        计算输入顶点的终点
        :param v:
        :param ends: 存储每个顶点的终点
        :return:
        """
        while ends[v] != 0:
            v = ends[v]
        return v


if __name__ == '__main__':
    # 普利姆算法测试
    graph = Graph(7)
    vertexts = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weights = [[10000, 5, 7, 10000, 10000, 10000, 2],
               [5, 10000, 10000, 9, 10000, 10000, 3],
                [7, 10000, 10000, 10000, 8, 10000, 10000],
                [10000, 9, 10000, 10000, 10000, 4, 10000],
                [10000, 10000, 8, 10000, 10000, 5, 4],
                [10000, 10000, 10000, 4, 5, 10000, 6],
                [2, 3, 10000, 10000, 4, 6, 10000]]
    graph.create(vertexts, weights)
    tree = MinimumSpanningTree()
    tree.import_graph(graph)
    tree.prim(0)

    # 克鲁斯卡尔算法测试
    graph = Graph(7)
    vertexts = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weights = [[10000,  12, 10000, 10000, 10000,  16,  14],
                [12,   10000,  110000, 10000, 10000,   7, 10000],
                [10000,  110000,   10000,   3,   5,   6, 10000],
                [10000, 10000,   3,   10000,   4, 10000, 10000],
                [10000, 10000,   5,   4,   10000,   2,   8],
                [16,   7,   6, 10000,   2,   10000,   9],
                [14, 10000, 10000, 10000,   8,   9,   10000]]
    graph.create(vertexts, weights)
    tree = MinimumSpanningTree()
    tree.import_graph(graph)
    tree.kruskal()
