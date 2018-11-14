#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
财务自由

每年支出 / 4% 是你要拥有的可带来增值的财富总额


@author: ZHOU Heng
"""


def main():
    year = 20  # 年
    rate = 12 / 100  # 年化收益率
    base = 2.2  # 本金，单位：万

    money = 0
    for i in range(year):
        money = (base + money) * (1 + rate)

    print(
        "每年投入 {} W元，年化收益 {:2.0f}%，坚持 {} 年后，总资产 {:2.3f} 万元。".format(
            base, rate * 100, year, money
        )
    )


if __name__ == "__main__":
    main()
