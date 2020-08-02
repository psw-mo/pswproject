class Flower:#定义一个类
    #属性
    colour = "red"#颜色
    smell = "sweet"#味道
    kind = "玫瑰"#品种
    #方法
    def sell(self):#sell的方法
        print("花那去卖钱")#打印花可以卖钱

    def give(self):#give的方法
        print("花拿去送人")#打印花可以送人
 #实例化类
flower = Flower()
print("花的颜色",flower.colour,"花的味道",flower.smell,"花的品种",flower.kind)#打印花的属性
flower.sell()#调用sell方法
flower.give()#调用give方法