#coding=utf-8
from hefan_api_testcases.pub_code.splicing_url import public_url
import unittest,requests


data_dic = {"activityCoverImg":"","activityImgHeight":"0","bucket":"hefanimage","activityImgWidth":"0","messageContent":a,"videoCoverImgHeight":"555","fanClubId":"40","activityEndTime":"0","activityTotalNumber":"0","pictureUrls":"[""]","messageDesc":"","messageTitle":"包包","videoCoverImgWidth":"990"}

url = "http://testerclubapi.hefantv.com/v1/message/savePostn"


class Test_api_case(unittest.TestCase):
    def setUp(self):
        self.public = list(public_url(data_dic,url))
        self.header = {
            "authinfo": str(self.public[1]),
                  "buriedPoint": str({"channelNo": "HF17", "deviceType": "android", "deviceModel": "M57AC",
                                  "uid": "1912621",
                                  "deviceToken": "d31a76ab52c44434aeb5ab404e0af919", "appVer": "1.1.31.649",
                                  "devImei": "99000739017682", "sysVersion": "5.1", "netType": "5",
                                  "clp": "192.168.3.6",
                                  "appCode": "37"})}

    def test_case(self):
        responses = requests.post(self.public[0],headers=self.header)
        responses.encoding='utf-8'
        # self.assertEqual(responses.json()['code'],1000,msg="code Error")
        with open('a.txt', 'w') as f:
            f.write(responses.text)


