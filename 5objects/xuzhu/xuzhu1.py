from tonglao.tonglao1 import TongLao#导入父类

class XuZhu(TongLao):#定义一个类，xuzhu，继承父类
    def __init__(self,hp,power):#构造法
        TongLao.__init__(self,hp,power)#继承父类的属性

    def read(self):#念经的方法
        print("罪过罪过")#打印罪过

    def fight(self):#打斗的方法
        xuzu = XuZhu(1000,100)#实例化虚竹
        xuzu.read()#调用虚竹的类

xuzu = XuZhu(1000,100)#实例化虚竹，传入hp，power值
print("虚竹的生命值：",xuzu.hp,"虚竹的伤害值：",xuzu.power)#打印虚竹的hp和power
xuzu.fight()#调用方法