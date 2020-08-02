class Boyfriend: #定义类，定义一个男朋友
    #属性
    name = "defult"
    appearance = 'handsome' #外表，英俊
    gender = 'male' #性别，男
    age = 0 #年龄
    weight = 0 #体重
    #构造方法
    def __init__(self,name,age,weight):
        #实例属性
        self.name = name#姓名
        self.age = age#年龄
        self.weight = weight#体重
    #方法，def关键字定义方法
    def make_money(self,money): #字面量插值传参money，挣钱
        print(f"会挣{money}钱")#打印挣的钱

    def spoil(self):#宠
        print("宠爱女朋友")#打印宠爱

    def do_something(self):#做事情
        print("能搬很沉的东西")#打印做的事

#实例化类
boyfriend = Boyfriend('天天',20,120)#传入姓名，年龄，体重的参数
print(f"男朋友的姓名是{boyfriend.name},年龄{boyfriend.age},体重{boyfriend.weight}")#输出男朋友的姓名，年龄，体重
print("男朋友的长相",boyfriend.appearance,"男朋友的性别",boyfriend.gender)#输出类中的长相和性别
#调用实例化类的方法
boyfriend.make_money(10000)#传入money参数
boyfriend.spoil()#输出宠爱
boyfriend.do_something()#输出做事情