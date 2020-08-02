class Game:#定义一个游戏的类
    #属性
    name = "defult"#游戏的名字
    kind = '多人联机'#游戏种类
    style = "回合制"#游戏风格
    capacity = 0#游戏大小
    #构造法，将name和capacity变为self.的变量
    def __init__(self, name, capacity):
        self.name = name#游戏名字
        self.capacity = capacity#游戏大小

    def player_name(self,set_name):#游戏玩家名字的方法，字面量插值传递参数
        print(f"玩家的名字：{set_name}")#打印玩家名字

    def fight(self,my_hp,your_hp,my_power,your_power):#定义游戏的打斗，hp和伤害值进行字面量插值传参
        while True:  ##进行多次对打
            my_hp = my_hp - your_power  ##多次对打，我方剩余hp
            your_hp = your_hp - my_power##多次对打，你方剩余hp
            if my_hp <= 0:#如果我的hp小于0
                print("我剩下的hp：", my_hp)#打印我剩下的hp
                print("你剩下的hp：", your_hp)#打印你剩下的hp
                print("你赢了")#打印你赢了
                break  ###跳出整个循环
            elif your_hp <= 0:#如果你的hp小于0
                print("我剩下的hp：", my_hp)#打印我剩下的hp
                print("你剩下的hp：", your_hp)#打印你剩下的hp
                print("我赢了")#打印我赢了
                break##跳出整个循环
#实例化类
game = Game("阴阳师",720)#传入名字，大小
print(f"游戏名字：{game.name},游戏大小：{game.capacity}kb")#打印游戏名字和大小
game.player_name("随便")#调用游戏玩家姓名的方法，传入玩家名字参数
game.fight(1100,1200,200,100)#调用游戏打斗的方法，传入hp和power的值