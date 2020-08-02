class TongLao:#定义一个类
    #属性
    hp = 0
    power = 0
    #构造法，以def关键字开头
    def __init__(self,hp,power):
        self.hp = hp#定义以self.的变量，hp
        self.power = power#定义以self.的变量，power

    def see_people(self,name):#方法
        if name == 'WYZ':#如果看到无崖子
            print("师弟！！！！")#打印师弟
        elif name == "李秋水":#否则，如果看到李秋水
            print("呸，贱人")#打印贱人
        elif name == "丁春秋":#否则，如果看到丁春秋
            print("叛徒，我杀了你！")#打印我要杀了你

    def fight_zms(self,enemy_hp,enemy_power):#打斗的方法
        self.hp = self.hp/2#血量缩减2倍
        self.power = self.power*10#武力值提升10倍
        self.hp = self.hp - enemy_power#自己剩余血量
        enemy_hp = enemy_hp - self.power#敌人剩余血量
        if self.hp > enemy_hp:#如果童姥血量多余敌人
            print("天山童姥获胜")#打印童姥赢了
        else:
            print("敌人获胜")#否则，打印敌人赢了

tonglao = TongLao(1000,100)#实例化类，传入hp，power参数
#print("天山童姥的生命值：",tonglao.hp,"天山童姥的伤害值：",tonglao.power)#打印童姥hp和power
#tonglao.see_people("WYZ")#调用方法，传入name值
#tonglao.fight_zms(1100,300)#调用方法，传入敌人的hp，和power