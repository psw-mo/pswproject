import requests
class TestDepartment:

    def setup(self):
        #获取token
        # 定义凭证
        corpid = 'ww520c3cd31cdac212'
        corpsecret = '758ILGbkB0oIYOdIdxOGBkCeEsQdJR7jg-9IyHZPgyY'
        # 请求地址（注：为必填值前的部分）
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # params为字典类型
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发出get请求
        r = requests.get(url=url, params=params)
        # 获取access_token
        self.token = r.json()["access_token"]

    def test_creat_department(self):
        #请求地址(创建部门)
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        #定义请求参数
        print(self)
        param = {
                "access_token":self.token
        }
        #定义请求体
        data ={
            "name": "技术部2",
           "name_en": "psw",
           "parentid": 1,
           "order": 1,
           "id":3
        }
        #发送post请求
        r = requests.post(url = url,json = data,params = param)
        #断言（判断）
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
