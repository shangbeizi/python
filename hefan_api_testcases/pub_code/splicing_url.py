import requests
import time
import hashlib



def now_time():
    '''
    获取当前时间的时间戳，13位数的毫秒
    :return: 当前时间（毫秒）
    '''
    times= time.time()*1000
    time_ms= str(times).split('.')[0]
    return time_ms



def public_url(data_dic,url):
    '''
    拼接app格式的url
    :return:拼接后的url
    '''
    #以utf-8的编码方式对msg进行md5加密
    user_login_response = list(userlogin())
    token = user_login_response[0]
    data_dic_str = str(data_dic)
    msg_no_md5 = str(user_login_response[1])+'_key_'+data_dic_str
    msg_md5 = hashlib.md5(msg_no_md5.encode(encoding='utf-8')).hexdigest()
    #拼接测试url的入参
    datas = {"data":data_dic_str,"time":now_time(),"consume":user_login_response[1],"msg":msg_md5}
    #拼接测试url地址
    test_url = requests.get(url,params=datas).url
    # 使用return返回测试url的值
    return test_url,token


def userlogin(mobile=13552180750,msCode=8888):
    #初始化登陆入参
    userlogin_url = 'http://testerpassport.hefantv.com/v2/login/userLogin'
    userlogin_data_dic = {"deviceToken":"null","mobile":mobile,"msCode":msCode,"deviceNo":"480dcc51f94861a3ede9e18b645943c5ee842443"}
    #生成登陆所需md5加密串
    data_dic_str = str(userlogin_data_dic)
    msg_no_md5 = ''+'_key_'+data_dic_str
    msg_md5 = hashlib.md5(msg_no_md5.encode(encoding='utf-8')).hexdigest()
    #生成requests.get方法中params的关键字，params把字典形式的入参转换成key-value形式存入url中
    datas = {"data":data_dic_str,"time":now_time(),"consume":'', "msg":msg_md5}

    login_url = requests.get(userlogin_url,params=datas)
    #把返回结果转换成字典格式
    response = login_url.json()
    #以字典的方式取值
    token = response['data']['token']
    userId = response['data']['userId']

    return token,userId

