#获取token
import requests
class TestToken:

    def test_get_token(self):
        #获取access_token

        #定义凭证
        corpid ='ww520c3cd31cdac212'
        corpsecret = '758ILGbkB0oIYOdIdxOGBkCeEsQdJR7jg-9IyHZPgyY'
        #请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        #发出get请求
        r = requests.get(url = url)
        #打印响应内容
        print(r.json())

    def test_getToken_pramas(self):
        #使用requests.get中params传参
        # 定义凭证
        corpid = 'ww520c3cd31cdac212'
        corpsecret = '758ILGbkB0oIYOdIdxOGBkCeEsQdJR7jg-9IyHZPgyY'
        # 请求地址（注：为必填值前的部分）
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        #params为字典类型
        params = {
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        # 发出get请求
        r = requests.get(url=url,params = params)
        # 打印响应内容
        print(r.json())