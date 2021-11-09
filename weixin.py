import requests
import re
from my_get import recognize
from lxml import etree

def health_report():
    ses = requests.session()
    url_1 = "https://weixine.ustc.edu.cn/"
    url_2 = "https://passport.ustc.edu.cn/"
    headers = {
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.150 Safari/537.36 "
    }
    ses.get(url=url_1 + "2020/login", headers=headers)
    res = ses.get(url=url_1 + "2020/caslogin", headers=headers)
    CAS = re.search("(LT-\w+)", res.text)[0]
    res = ses.get(url=url_2 + "validatecode.jsp?type=login", headers=headers)
    try:
        with open("/tmp/a.png", 'wb') as fp:
            fp.write(res.content)
    except:
        print('fail to open the picture')
    cop = recognize("/tmp/a.png")

    #print("cop: " + cop)
    _data = {
        "model": "uplogin.jsp",
        "CAS_LT": CAS,
        "service": "https://weixine.ustc.edu.cn/2020/caslogin",
        "warn": "",
        "showCode": "1",
        "username": "PB19020658",
        "password": "1375446341",
        "LT": cop,
        "button": ""
    }
    _headers = {
        "Connection": "close",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.150 Safari/537.36 ",
        "Referer": "https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                "application/signed-exchange;v=b3;q=0.9",
        "Origin": "https://passport.ustc.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
    }

    proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
    res = ses.post(url=url_2 + "login", headers=_headers, data=_data)
    tree = etree.HTML(res.text)
    _token = ""
    if tree.xpath('//input[@name="_token"]/@value')[0]:
        _token = tree.xpath('//input[@name="_token"]/@value')[0]

    else:
        print(res.text)
    #print("_token: " + _token)
    _headers = {
        "Connection": "close",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.150 Safari/537.36 ",
        "Referer": "https://weixine.ustc.edu.cn/2020/home",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                "application/signed-exchange;v=b3;q=0.9",
        "Origin": "https://weixine.ustc.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document"
    }
    _data = {
        "_token": _token,
        "now_address": "1",
        "gps_now_address": "",
        "now_province": "340000",
        "gps_province": "",
        "now_city": "340100",
        "gps_city": "",
        "now_country": "340104",
        "gps_country": "",
        "now_detail": "",
        "is_inschool":"6",
        "body_condition": "1",
        "body_condition_detail": "",
        "now_status": "1",
        "now_status_detail": "",
        "has_fever": "0",
        "last_touch_sars": "0",
        "last_touch_sars_date": "",
        "last_touch_sars_detail": "",
        "is_danger": "0",
        "is_goto_danger": "0",
        "jinji_lxr": "龚长根",
        "jinji_guanxi": "父子",
        "jiji_mobile": "13815457535",
        "other_detail": ""
    }

    res = ses.post(url=url_1 + "2020/daliy_report", headers=_headers, data=_data)
    if '上报成功' in res.text:
        return 1

if __name__ == "__main__":
    ret = 0
    while ret != 1:
        ret = health_report()

    print('success')
