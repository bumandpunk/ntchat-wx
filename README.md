<h1 align="center">NtChat-WX</h1>
<p align="center">
    <a href="https://github.com/bumandpunk/ntchat-wx/releases"><img src="https://img.shields.io/badge/release-1.0.0-blue.svg?" alt="release"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?" alt="License"></a>
</p>




## 介绍

- 基于pc微信的api接口
- 支持收发文本、群@、名片、图片、文件、视频、链接卡片等
- 微信机器人demo及相关功能示例见 [examples/echo_bot_on.py](examples/echo_bot_on.py)  ,已实现对接第三方api功能及机器人权限控制
- demo中api使用天行数据和https://api.aa1.cn/ 的免费api ，可自行申请替换key
## 支持的微信版本下载
- 下载 [WeChatSetup3.6.0.18.exe](https://github.com/bumandpunk/ntchat-wx/releases/download/v3.6.0.18/WeChatSetup-3.6.0.18.exe)
- 下载 [禁用微信自动更新.exe](https://github.com/bumandpunk/ntchat-wx/releases/download/v3.6.0.18/PC.exe)
## 帮助文档
- 查看 [常见问题](docs/FAQ.md)
- 查看 [常用示例](examples)
- 查看 [微信机器人示例](examples/echo_bot_on.py)  
## 安装

```bash
pip install ntchat
```
如需chatgpt功能
```bash
pip install openai
```
国内源安装
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntchat
```
启动机器人
```bash
cd ./examples
python echo_bot_on.py
```

## 简单入门实例

如果你想要给文件传输助手发一条信息，只需要这样

```python
# -*- coding: utf-8 -*-
import sys
import ntchat

wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)

# 等待登录
wechat.wait_login()

# 向文件助手发送一条消息
wechat.send_text(to_wxid="filehelper", content="hello, filehelper")

try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
```

## 获取联系人和群列表
```python
# -*- coding: utf-8 -*-
import sys
import ntchat

wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)

# 等待登录
wechat.wait_login()

# 获取联系人列表并输出
contacts = wechat.get_contacts()

print("联系人列表: ")
print(contacts)

rooms = wechat.get_rooms()
print("群列表: ")
print(rooms)


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
```

## 监听消息并自动回复

```python
# -*- coding: utf-8 -*-
import sys
import ntchat

wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)


# 注册消息回调
@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def on_recv_text_msg(wechat_instance: ntchat.WeChat, message):
    data = message["data"]
    from_wxid = data["from_wxid"]
    self_wxid = wechat_instance.get_login_info()["wxid"]

    # 判断消息不是自己发的，并回复对方
    if from_wxid != self_wxid:
        wechat_instance.send_text(to_wxid=from_wxid, content=f"你发送的消息是: {data['msg']}")


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
```
## 感谢支持
<img style="width:320px;height:450px;" src="https://zhangfujie.icu/wx.jpg"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img style="width:320px;height:450px" src="https://zhangfujie.icu/zfb.jpg"/>
