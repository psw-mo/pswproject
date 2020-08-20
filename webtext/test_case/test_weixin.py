from selenium import webdriver
from selenium.webdriver.chrome.options import Options#导入Options
from selenium.webdriver.common.by import By#导入by
import shelve
from time import sleep

class TestDemo():
    def setup_method(self,method):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)#复用浏览器
        self.driver.implicitly_wait(5)#隐式等待，全局

    def teatdown_method(self,method):
        self.driver.quit()#执行完case就退出网页，释放缓存

    def test_cookie(self):
        #获取当前页面的cookies
        #cookies = self.driver.get_cookies()
        #print(cookies)
        #打开企业微信的index页面，但需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies =[
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851064581572'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ldKg-P0Cc99CG5uh18hciMBgpg5VNxoYRorm0HalHyRxE0TWcwcuVDtBHo_e9duVQIv58VpSBG1NSZb_KsRSc0peXJ-MUoa0ZLl4qp2pETfbfcRuFKVeRob3KzS3M-lGwkL3PQEN71WsL3tKq6IY2EmtsdFnCBZJx9GRBxZBBSJmoq9iKVeFKdFD4ap9d9RF3vIYS3_e0FdmDcfYDhwG1z77CMGQiYwL63Q3xKRzK4Eyzf7YhO4ZQ5faPI6Z9xf84gCo_w5hlC5aI-w6AIdHjg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851064581572'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324943155247'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'vL4YAh_rbmkpnq-uSnM08c4bPK3tdrBXHplirWT1W6UtzC871xDBsnOpXd0J5raq'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2359027'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597938836, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8o54van'}, {'domain': '.qq.com', 'expiry': 1597997380, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2000784262.1597907456'},
            {'domain': '.qq.com', 'expiry': 1660982980, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1236580855.1597907456'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629443300, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483714, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '1884760d6a6b1e443ac56f48c17db1ec1bf2232357c0301ad36e155246960602'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629446964, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597907456,1597910965'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483714, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'u6JEjRRHbj'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600502983, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597910965'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2202187886324494'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/','secure': False, 'value': '4420110336'}]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #实现cookie数据的持久储存
    def test_cookieShelve(self):

        #db = shelve.open('./mydbs/cookies')#在mydbs下创建cookies文件
        #db['cookie'] = cookies#将cookies储存，cookie（名字任意）命名
        #db.close()#关闭文件

        db = shelve.open('./mydbs/cookies')#打开cookies文件
        cookies =db['cookie']#取出cookie
        #打开企业微信的index页面，但需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #找到联系人元素，进行点击
        self.driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        #找到上传文件，并进行发送文件
        self.driver.find_element(By.ID,'js_upload_file_input').send_keys('D:\win7我的文档-桌面-收藏夹\Desktop\通讯人员名单.xlsx')
        #点击确认上传
        self.driver.find_element(By.ID,'submit_csv').click()
        assert  "前往查看" ==self.driver.find_element(By.ID,'reloadContact').text