"""
作者：Huayu Zong
日期：2022年12月日
"""

import json
import urllib.request
import urllib.error
import random


USE_GITHUB_REMOTE_VRIFIFY = False
HEADERS = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42")

#根据输入的键值，验证用户名是否注册
def verify_username_registered(dict_obj, user_name):
    #用户名不存在，返回0
    if dict_obj.get(user_name) is None:
        print('用户名不存在')
        return (False, None)

    #存在返回1
    return (True, dict_obj.get(user_name))


def get_login_app_password(dict_obj):
    password = dict_obj['password']
    print(f'password = {password}')
    return password


def get_login_aliyun_params(dict_obj):
    device_certificate_dict = dict_obj['device_certificate']
    product_key = device_certificate_dict['ProductKey']
    device_name = device_certificate_dict['DeviceName']
    device_secret = device_certificate_dict['DeviceSecret']
    print(product_key, device_name, device_secret)

    return (product_key, device_name, device_secret)
    pass


def get_file_from_github(url):
    # opener = urllib.request.build_opener()
    # ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    #            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    #            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    #            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    #            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    #            ]
    # opener.addheaders = [('User-Agent', random.choice(ua_list))]
    #
    # #1.获取指定url下的所有内容
    # try:
    #
    #     response = opener.open(url)
    #     get_data  = response.read().decode('utf-8')
    #     print(type(get_data), get_data)
    #     response.close()
    #
    #     # 2.将得到的网页内容的数据解析成字典
    #     dict_obj = json.loads(get_data)
    #     print(type(dict_obj), dict_obj)
    #
    #     return dict_obj
    # except urllib.error.HTTPError  as err:
    #     print(err)
    #     return None
    # except urllib.error.URLError as err:
    #     print(err)
    #     return None
    # except Exception :  # global errro variable
    #     print(Exception)
    #     return None
    pass








def verify_login_from_github(user_name_input, password_input):
    #url = 'https://raw.githubusercontent.com/zhy18895378166/TBox-App-OTA/main/UserManagerSystem.json'
    #url = 'https://gitee.com/zong_huayu/tbox-app-client/raw/master/UserManagerSystem.json'
    url = 'https://www.baidu.com'

    dict_obj_all = get_file_from_github(url)
    if dict_obj_all != None:
        is_registered, need_parse_data = verify_username_registered(dict_obj_all, user_name_input)
        if is_registered == True:
            pw = get_login_app_password(need_parse_data)
            if pw == password_input:
                get_login_aliyun_params(need_parse_data)
                # (todo) 可以把数据写到文件
                print("登录成功")
                return (True, 'login success')
            else:
                print("Error: 密码错误")
                return (False, 'password error')
        else:
            print("Error: 用户名未注册")
            return (False, 'username not register')
    else:
        return (True, 'login success')


def verify_login_from_local(user_name_input, password_input):
    user_name = 'zhy'
    password = 'zhy123'

    if user_name_input == user_name and password_input == password:
        return True
    else:
        print('user name or password error!')
        return False
    pass



def verify_login(user_name_input, password_input):
    if USE_GITHUB_REMOTE_VRIFIFY is True:
        #todo
        pass
    else:
        if verify_login_from_local(user_name_input, password_input) is True:
            return (True, 'login success')
        else:
            return (False, 'login error')


#
# url = 'https://raw.githubusercontent.com/zhy18895378166/TBox-App-OTA/main/UserManagerSystem.json'
#     #url = 'https://gitee.com/login'
#     #url = 'https://www.baidu.com'
#     #url = 'https://blog.csdn.net/qq_32355021/article/details/124850726'
#     # 生成GET请求
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'}
#     rqg = requests.get(url,headers = headers,auth=('2465612295@qq.com','abcd19960501?!'))
#     print("status:", rqg.status_code)  # 查看状态码
#     if rqg.status_code == 200:
#         print('get success')
#
#     print("结果类型:", type(rqg))  # 查看结果类型
#
#     print("编码:", rqg.encoding)  # 查看编码
#     print("响应头:", rqg.headers)  # 查看响应头
#     print("网页内容：", rqg.text)  # 查看网页内容
#
#
#     while True:
#         pass
#
#
