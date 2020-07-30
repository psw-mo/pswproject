'''
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''

def fight():
    my_hp = 1100   ##定义双方hp值和power值
    your_hp = 1000
    my_power = 200
    your_power = 200
    while True:   ##进行多次对打
        my_hp=my_hp-your_power   ##双方剩余hp
        your_hp=your_hp-my_power
        if my_hp <= 0:
            print("我剩下的hp：", my_hp)
            print("你剩下的hp：", your_hp)
            print("你赢了")
            break    ###先小于0的就赢了，跳出循环
        elif your_hp <= 0:
            print("我剩下的hp：", my_hp)
            print("你剩下的hp：", your_hp)
            print("我赢了")
            break


##调用
fight()

