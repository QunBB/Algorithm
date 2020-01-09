def greedy_cover(stations: dict):
    """
    使用贪心算法解决集合覆盖问题：选择最少的广播台，让所有的地区都可以接收到信号
    :param stations:
    :return:
    """

    # 创建一个set存放需要覆盖但还未覆盖的地区
    not_cover = set()
    for v in stations.values():
        for s in v:
            not_cover.add(s)
    selects = []  # 存放我们选择的电台
    while True:
        # 首先，选择覆盖了最多未覆盖地区的电台
        max_key = ''
        max_num = 0
        for k in stations.keys():
            intersection = not_cover.intersection(stations[k])
            if len(intersection) > max_num:
                max_key = k
                max_num = len(intersection)
        selects.append(max_key)
        # 然后，将选择电台覆盖的地区从not_cover中移除
        for e in stations[max_key]:
            if e in not_cover:
                not_cover.remove(e)
        # 如果，not_cover未空即所有地区已覆盖，则可以结束算法
        if len(not_cover) == 0:
            break

    return selects


if __name__ == '__main__':
    stations = {"k1": ["北京", "上海", "天津"], "k2": ["广州", "北京", "深圳"],
                "k3": ["成都", "上海", "杭州"], "k4": ["上海", "天津"],
                "k5": ["杭州", "大连"]}
    print(greedy_cover(stations))
