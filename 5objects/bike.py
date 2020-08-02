class Bike:  # 定义一个自行车的类
    # 属性
    logo = "defult"  # 品牌
    colour = 'black'  # 颜色
    weight = 0  # 重量

    # 构造法
    def __init__(self, logo, weight):
        self.logo = logo  # 品牌
        self.weight = weight  # 重量

    def ride(self, km):  # 骑行的方法，字面量插值传参
        print(f"可以骑行{km}km")  # 打印骑行多少km

    def sell(self):  # 买卖的方法
        print("可以进行交易")  # 打印交易

    def manned(self):  # 载人的方法
        print("可以载人")  # 打印载人


# 实例化类
bike = Bike('凤凰牌', 20)  # 传入品牌和重量的参数
print("自行车的颜色：", bike.colour, "自行车的品牌：", bike.logo, "自行车的重量：", bike.weight)  # 打印自行车的属性
bike.ride(200)  # 传入骑行的公里数参数，调用方法
bike.sell()  # 调用买卖的方法
bike.manned()  # 调用载人的方法