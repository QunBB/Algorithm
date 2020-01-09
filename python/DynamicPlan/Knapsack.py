import numpy as np


def knapsack(weight, value, C):
    """
    :param weight: 每个商品的重量
    :param value: 每个商品的价值
    :param C: 背包的最大容量
    :return:
    """

    v = np.zeros([len(weight)+1, C+1])  # 存储每个单元格的最大价值

    # 存储每个单元格的对应最大价值时选择的商品组合
    goods = np.full([len(weight)+1, C+1], '', dtype='<U30')

    for i in range(1, v.shape[0]):
        for j in range(1, v.shape[1]):
            temp = 0

            # 最大价值的动态规划
            # v[i-1][j]其实就是不加入商品i时的最大价值
            # temp：加入商品i时的最大价值
            if weight[i-1] > j:
                v[i][j] = v[i-1][j]
            else:
                temp = value[i-1] + v[i-1][j - weight[i-1]]
                v[i][j] = max(v[i-1][j], temp)

            # 最佳商品组合，字符串形式，以'_'分割，其实与最大价值的思路一样
            if v[i-1][j] > temp:  # 不加入商品i时的最大价值比加入商品i时的最大价值高
                goods[i][j] = goods[i-1][j]
            elif v[i-1][j] < temp:  # 不加入商品i时的最大价值比加入商品i时的最大价值低
                if goods[i-1][j - weight[i-1]] == '':
                    goods[i][j] = str(i - 1)
                else:
                    goods[i][j] = goods[i-1][j - weight[i-1]] + '_' + str(i-1)
            else:  # 加入商品i时的最大价值比加入商品i时的最大价值相等时，我们取重量较小的
                w1 = 0
                w2 = weight[i-1]
                for g1 in goods[i-1][j].split('_'):
                    w1 += weight[int(g1)]
                for g2 in goods[i-1][j - weight[i-1]].split('_'):
                    w2 += weight[int(g2)]
                if w1 < w2:
                    goods[i][j] = goods[i - 1][j]
                elif w1 > w2:
                    goods[i][j] = goods[i - 1][j - weight[i - 1]] + '_' + str(i - 1)
                else:  # 如果重量也相等的话，我们将两种组合都记录下来，以'|'分割
                    goods[i][j] = goods[i - 1][j] + '|' + goods[i - 1][j - weight[i - 1]] + '_' + str(i - 1)

    print(v)
    print(goods)


if __name__ == '__main__':
    weight = [1, 4, 3]
    value = [1500, 3000, 2000]
    knapsack(weight, value, C=4)
