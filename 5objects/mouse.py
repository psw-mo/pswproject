class Mouse:#定义一个类
    #属性
    colour = 'brown' #颜色，棕色
    size = 'middle' #体型，中等
    character = 'aggressive' #性格，好斗
    #方法
    def eat(self):#吃
        print("老鼠在偷吃")#打印吃

    def run(self): #跑
        print("老鼠在跑") #打印跑

    def sleep(self): #睡觉
        print("老鼠在睡觉") #打印睡觉
#实例化老鼠的类
mouse = Mouse()
print("老鼠的颜色",mouse.colour,"老鼠的体型",mouse.size,"老鼠的性格",mouse.character)#打印老鼠的3个属性
mouse.eat() #调用吃的方法
mouse.run() #调用跑的方法
mouse.sleep() #调用睡觉的方法