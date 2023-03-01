'''
Date: 2022-10-14 09:50:33
LastEditors: Zfj
LastEditTime: 2022-10-31 17:10:12
FilePath: \ntchat\examples\get_rooms.py
Description: 
'''
# -*- coding: utf-8 -*-
import sys
import time
import os
os.environ['NTCHAT_LOG'] = "ERROR"
import ntchat

wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)

# 等待登录
wechat.wait_login()

# 获取群列表并输出
# rooms = wechat.get_rooms()
roomUserList = wechat.get_room_members(room_wxid="18462446628@chatroom")
print("群列表: ")
# print(roomUserList['member_list'])
for item in roomUserList['member_list']:
    print({'1:'+item['account'],'2:'+item['nickname'],'3:'+item['wxid']})


# 以下是为了让程序不结束，如果有用于PyQt等有主循环消息的框架，可以去除下面代码
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()

