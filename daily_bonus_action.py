import requests
import bilibili
import re
import time
import os


# 尝试登陆
account=input ().strip ()
password=input ().strip ()
print(account)
print(password)

b = bilibili.Bilibili()
b.login(username=account, password=password)

# 获取 Cookie
cookie_str = ""
cookies = b.get_cookies()
for cookie in cookies:
    cookie_str += cookie + "=" + cookies[cookie] + "; "

headers_with_cookie={'User-Agent': "Mozilla/5.0 BiliDroid/6.4.0 (bbcallen@gmail.com) os/android model/M1903F11I mobi_app/android build/6040500 channel/bili innerVer/6040500 osVer/9.0.0 network/2",
                     'Cookie': cookie_str}


print("夏日音乐季活动 start>>>")

print("尝试获得分享抽奖机会...")

r = requests.post("https://api.bilibili.com/x/activity/lottery/addtimes", verify=False, headers=headers_with_cookie, data={
    "sid": "dd83a687-c800-11ea-8597-246e966235d8",
    "action_type": 3,
    "csrf": b.get_csrf()
})

print("响应: " + r.text)
if r.json()['code'] == 0:
    print("获取成功.")

time.sleep(2)

# 尝试获取关注列表
r = requests.get("https://www.bilibili.com/blackboard/2020SummerMusic.html?native.theme=1&night=0")
for i in re.findall(r"\\\"uid\\\":\\\"[0-9]+\\\"", r.text):
    i = i.replace("uid", "")
    i = i.replace(":", "")
    i = i.replace("\\", "")
    i = i.replace("\"", "")
    print("获取到待关注的id: " + i)
    time.sleep(3)
    if b.follow(i):
        print("关注成功!")

        print("尝试获得关注抽奖机会...")

        r = requests.post("https://api.bilibili.com/x/activity/lottery/addtimes", verify=False, headers=headers_with_cookie, data={
            "sid": "dd83a687-c800-11ea-8597-246e966235d8",
            "action_type": 4,
            "csrf": b.get_csrf()
        })

        time.sleep(3)

        print("响应: " + r.text)
        if r.json()['code'] == 0:
            print("获取成功.")
            break

time.sleep(3)

for i in range(0, 2):
    print("尝试抽奖...")
    r = requests.post("https://api.bilibili.com/x/activity/lottery/do", verify=False, headers=headers_with_cookie, data={
        "sid": "dd83a687-c800-11ea-8597-246e966235d8",
        "type": 1,
        "csrf": b.get_csrf()
    })
    print("响应: " + r.text)
    if r.json()['code'] == 0:
        print("抽奖成功!")
        print("获得奖品: " + r.json()['data'][0]['gift_name'])
    time.sleep(5)

print("<<<end 夏日音乐季活动")

time.sleep(5)

# 手书嘉年华活动
print("手书嘉年华活动 start>>>")

# 获取需要投币的 UP 主列表
r = requests.get("https://api.bilibili.com/medialist/gateway/base/detail?media_id=1005976362&pn=0&ps=20", headers=headers_with_cookie, verify=False)
for i in r.json()['data']['medias'][0:5]:
    bvid = i['bvid']
    print("待投币视频: " + bvid)
    b.reward(aid=bvid)
    time.sleep(2)

print("尝试获取抽奖资格...")
r = requests.post("https://api.bilibili.com/x/activity/handwrite/addlotterytimes", verify=False, headers=headers_with_cookie, data={
    "csrf": b.get_csrf()
})
print("响应: " + r.text)
if r.json()['code'] == 0:
    print("获取抽奖资格成功.")

time.sleep(2)

print("尝试抽奖...")
r = requests.post("https://api.bilibili.com/x/activity/lottery/do", verify=False, headers=headers_with_cookie, data={
    "sid": "23ec0c85-b53c-11ea-8597-246e966235d8",
    "type": 1,
    "csrf": b.get_csrf()
})
print("响应: " + r.text)
if r.json()['code'] == 0:
    print("抽奖成功!")
    print("获得奖品: " + r.json()['data'][0]['gift_name'])

print("<<<end 手书嘉年华活动")

