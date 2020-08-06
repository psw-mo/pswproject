import pytest
from pytest_text.clac.Calc import Calculator
import yaml

with open('./data1.yaml') as f:#打开data1文件
    datas = yaml.safe_load(f)['add']#读取文件中add的数据给datas
    add_num = datas['add_num']#读取datas下的add_num的数值
    add_ids = datas['add_ids']#读取datas下的add_ids的数值
    div_num = datas['div_num']
    div_ids = datas['div_ids']

class Testcalc():

    #在类中的setup中进行实例化计算器
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")#调用方法时，打印开始计算

    def teardown(self):
        print("结束计算")#调用结束时，打印结束计算

    @pytest.mark.parametrize('a,b,result',add_num,ids = add_ids)
    def test_add(self,a,b,result):
        try:
            c = self.calc.test_add(a,b)
        except TypeError:
            print("数值类型错误")
        else:
            if isinstance(c,float):
                c = round(c,2)
            else:
                assert result == c

    @pytest.mark.parametrize('a,b,result',div_num,ids = div_ids)
    def test_div(self,a,b,result):
        try:
            c = self.calc.test_div(a, b)
        except TypeError:
            print("数值类型错误")
        else:
            if isinstance(c, float):
                c = round(c, 2)
            else:
                assert result == c