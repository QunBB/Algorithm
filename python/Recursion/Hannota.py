def hannota(num, tower_a, tower_b, tower_c):
    """
    :param num: 盘子的数量
    :param tower_a: 盘子移动前所处的塔
    :param tower_b: 需要借助的塔
    :param tower_c: 盘子移动的目标塔
    :return:
    """

    # 如果只有一个盘子，直接从tower_a移动到tower_c即可
    if num == 1:
        print('盘子%d：%s -> %s' % (num, tower_a, tower_c))
    else:
        # 如果有多个盘子，可以看成两个盘子：最下面的一个盘子、上面的所有盘子

        # 第一步：将上面的所有盘子从tower_a移动到tower_b
        hannota(num - 1, tower_a, tower_c, tower_b)

        # 第二步：将最下面的盘子从tower_a移动到tower_c
        print('盘子%d：%s -> %s' % (num, tower_a, tower_c))

        # 第三步：将上面的所有盘子从tower_b移动到tower_c
        hannota(num - 1, tower_b, tower_a, tower_c)


if __name__ == '__main__':
    hannota(5, 'A', 'B', 'C')
