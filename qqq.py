# -*- coding: utf-8 -*-
import requests
import hashlib
import time
import json
import random


class Youdao(object):
    def __init__(self, msg):
        self.msg = msg.encode('utf-8')
        self.url = 'https://fanyi.qq.com/api/translate'

    def get_result(self):
        '''headers里面有一些参数是必须的，注释掉的可以不用带上'''
        uuid = int(time.time() * 1000)
        data = {
                    "source":"auto",
                    "target":"zh",
                    "sourceText":self.msg,
                    "qtv":"adaa147e0205f436",
                    "qtk":"arpw6PmOYhVx2ZZdjA8zbmHILkrP0DWiIDIyWPQe5bWDnX/crhk8YR3JImCr+9Um4Ndg00nCWvV07rwsEvHaZxAjfbIex2BUZMrYwxe7Kw+xnrTRwKTGjecjBtllixxtQximxFCyI7k29EKeYGpBLA==",
                    "sessionUuid":"translate_uuid" + str(uuid)
        }
        headers = {
         "Accept": "application/json, text/javascript, */*; q=0.01",
         "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "fanyi.qq.com",
        "Origin": "https://fanyi.qq.com",
        "Referer": "https://fanyi.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        # 请求体的长度
        "Content-Length": str(len(str(data))),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "pgv_pvi=3994058752;fy_guid=f5d9a428-cc79-49dd-b775-130b92b90cd5; ts_refer=www.google.com/; pgv_pvid=3787775825; ts_uid=1687449336; gr_user_id=0c6d3dcc-13d7-4396-be80-3d645949b693; grwng_uid=a770616a-553e-4354-b0f1-136d30f33d60; pgv_info=ssid=s9058691778; ts_last=fanyi.qq.com/; 9c118ce09a6fa3f4_gr_session_id=b5e9114d-f07d-43ca-929d-693c65d6ac07; 8c66aca9f0d1ff2e_gr_session_id=7b8290ab-d993-45c1-bf49-5cfaea106e5a; 9c118ce09a6fa3f4_gr_session_id_b5e9114d-f07d-43ca-929d-693c65d6ac07=true; qtv=e815966a57175ce4; qtk=nl10vs4Mbu6r6/fWR2Bp3xIi16fs5hdcBE66NvTtKhtzIoEetOSRKgTmFcEVTGRPnZcSTfvjr9/gqb27KeimKNLAUetWQfAyspVZ+vBQ+TGXoUITQyhyRxZqbVfETYwsi1PPIx4Y4OvFRCjYuZ2pHg==; openCount=4"
        }
        html = requests.post(self.url, data=data, headers=headers).text
        print(html)

        infos = json.loads(html)
        result = infos['translate']['records'][0]['targetText']
        print(result)
        return result
                
if __name__ == '__main__':
    y = Youdao('身だしなみを整えておるようなので、しばらくお待ち頂けますか？')
    y.get_result()
