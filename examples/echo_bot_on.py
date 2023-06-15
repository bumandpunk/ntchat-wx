# -*- coding: utf-8 -*-
import urllib.error as error
import urllib.request as request
import urllib
import threading
import random
import json
import requests
import ntchat
import sys
import time
import os
import openai

os.environ['NTCHAT_LOG'] = "ERROR"

wechat = ntchat.WeChat()


# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)
with open("data.json", 'r', encoding='utf-8') as fw:
    injson = json.load(fw)
with open("four.json", 'r', encoding='utf-8') as fw2:
    injson2 = json.load(fw2)
with open("zhiling.json", 'r', encoding='utf-8') as main:
    allZhiling = json.load(main)



chatData = []

def chatgptai(val):
 #用户发言
 data = {"role": "user", "content": val}
 #首次把用户发言加入数组中
 chatData.append(data)#组织名及api填写
 openai.organization = "xxxxxxxxxxxx"
 openai.api_key = "apikey"
 completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=chatData
)
 #把回复内容也加进去，下次用
 chatData.append(completion.choices[0].message)
 return completion.choices[0].message.content.replace('\n', '')
def chatgptimg(val):

  openai.organization = "xxxxx"
  openai.api_key = "xxxxxxxx"
  completion = openai.Image.create(
  prompt=val,
  n=1,
  size="512x512"
)

  image_url= completion.data[0].url
  headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
  r = requests.get(image_url,headers=headers)
  imgName = val + str(random.randint(1,999))
  bendi_url = './resources/imgList/'+ imgName +'.jpg'
  
  with open(bendi_url ,mode = "wb") as f:
      f.write(r.content) #图片内容写入文件
      return_url = '本地文件夹路径' + imgName + '.jpg'
      return  return_url
global t


def fun_timer():
    # 定时发送指定文案
    print(time.strftime('%H:%M'))
    if (time.strftime('%H:%M') == "11:11"):
        wechat.send_text(to_wxid="xxxx", content="xxxx")
    # 定时发送发送群聊拍一拍
    wechat.send_pat(room_wxid='xxxx', patted_wxid='xxxx')
    # 定时发送发送群聊@
    wechat.send_room_at_msg(to_wxid='xxxx',
                            content='{$@}怎么不说话',
                            at_list=['xxx'])
    # 20s执行一次
    t = threading.Timer(20.0, fun_timer)

    t.start()


fun_timer()


def minguo():

    api_url = 'https://apis.tianapi.com/mgjuzi/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def qinghua():
    api_url = 'https://apis.tianapi.com/saylove/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def shi():
    api_url = 'https://apis.tianapi.com/qingshi/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def emo():
    api_url = 'https://apis.tianapi.com/hsjz/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def tiangou():
    api_url = 'https://apis.tianapi.com/tiangou/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def aini():
    api_url = 'https://apis.tianapi.com/caihongpi/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def wenan():
    api_url = 'https://apis.tianapi.com/pyqwenan/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['content'])
                    # print()
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def taici():
    api_url = 'https://apis.tianapi.com/dialogue/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['dialogue']+'—'+result['result']['source'])
                    # print(result['result']['dialogue']+'—'+result['result']['source'])
                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def penren():

    text_url = "https://v.api.aa1.cn/api/api-wenan-ktff/index.php?type=" + \
        str(random.randint(1, 5))

    response = requests.get(text_url)
    res = json.loads(response.text, strict=False)
    text = res['text'].replace('\n', '')
    return text


def saohua():
    text_url = "https://v.api.aa1.cn/api/api-saohua/index.php?type=json"

    response = requests.get(text_url)
    res = json.loads(response.text, strict=False)
    text = res['saohua'].replace('\n', '')
    return text
# 天气预报查询示例


def tianqi(val):
    api_url = 'https://api.tianapi.com/tianqi/index'
    params_dict = {
        "city": val,  # 查询天气的城市名称，如：北京、苏州、上海
        "key": "xxxxxxxxxxxxxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    area = result['newslist'][0]['area']
                    date = result['newslist'][0]['date']
                    temperature = result['newslist'][0]['lowest'] + \
                        '—' + result['newslist'][0]['highest']
                    sunrise = result['newslist'][0]['sunrise']
                    sunset = result['newslist'][0]['sunset']

                    weather = result['newslist'][0]['weather']
                    wind = result['newslist'][0]['wind']

                    windsc = result['newslist'][0]['windsc']
                    tips = result['newslist'][0]['tips']
                    return (("城市：%s\n日期：%s\n温度：%s\n日出：%s\n日落：%s\n天气：%s\n风向：%s\n风力：%s\n提示：%s" % (area, date,
                                                                                                temperature, sunrise, sunset, weather, wind, windsc, tips)))
                    # print()
                else:
                    return ("nono查不到")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return ("阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def jiqi(val):
    api_url = 'https://apis.tianapi.com/robot/index'
    params_dict = {
        "key": "xxxxxxx",  # 您申请的接口API接口请求Key
        "question": val
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['code']

                if (error_code == 200):
                    return (result['result']['reply'])
                    # print()
                else:
                    return ("我卡啦卡啦")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return ("我卡啦卡啦")
    except error.HTTPError as err:
        return ('我卡啦卡啦')
    except error.URLError as err:
        # 其他异常
        return (err)


def four():
    return injson2[random.randint(0, len(injson2))]['text']


def kou6():
    return injson[random.randint(0, len(injson))]['text']


def zhiling_text():

    # @property {String}			triggerMode			匹配模式
    # @property {String}			trigger			    匹配关键词
    # @property {String}			functionName	    调用方法名
    # @property {String}			sendType			发送消息类型
    # @property {Boolean}			needPower			是否需要权限

    return '1.6\n2.舔\n3.emo\n4.爱你\n5.文案\n6.情诗\n7.情话\n8.句子\n9.台词\n10.开喷\n11.发烧\n12.星期四\n13.天气-xxx\n15.转图-xxx'


def yiqing(val):
    api_url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    params_dict = {
        # "key": "xxxxxxx",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['ret']

                if (error_code == 0):
                    # return(result['result']['content'])
                    china_data = result['data']['diseaseh5Shelf']['areaTree'][0]['children']
                    for item in china_data:
                        if (val in item['name']):
                           #  return(item['today'],item['name'],item['date'])

                            return (("城市：%s\n今日新增确诊：%s\n今日本地确诊：%s\n今日无症状新增：%s\n中风险地区数量：%s\n高风险地区数量：%s\n数据更新时间：%s" % (item['name'],
                                                                                                                     item['today']['local_confirm_add'], item['today']['confirm'], item['today'][
                                                                                                                         'wzz_add'], item['total']['mediumRiskAreaNum'], item['total']['highRiskAreaNum'],
                                                                                                                     item['total']['mtime']
                                                                                                                     )))
                        if (item['children']):
                            for it in item['children']:
                                if (val in it['name']):
                                    # return(it['today'],it['name'],it['date'])
                                    return (("城市：%s\n今日新增确诊：%s\n今日本地确诊：%s\n今日无症状新增：%s\n中风险地区数量：%s\n高风险地区数量：%s\n数据更新时间：%s" % (it['name'],
                                                                                                                             it['today']['local_confirm_add'], it['today']['confirm'], it['today'][
                                                                                                                                 'wzz_add'], it['total']['mediumRiskAreaNum'], it['total']['highRiskAreaNum'],
                                                                                                                             it['total']['mtime']
                                                                                                                             )))
                                    # return it['today']

                else:
                    return ("交一下钱谢谢")
            except Exception as e:
                return ("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            return (" 阿,别查了")
    except error.HTTPError as err:
        return ('HTTPError等会再查')
    except error.URLError as err:
        # 其他异常
        return (err)


def texttoimg(val):
    if len(val) > 100:
        return '替换为本地图片路径既可'
    else:
        image_url = "https://v.api.aa1.cn/api/api-jupai/index.php?msg=" + \
            str(val)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
        r = requests.get(image_url, headers=headers)
        bendi_url = './resources/imgList/' + val + '.jpg'
        with open(bendi_url, mode="wb") as f:
            f.write(r.content)  # 图片内容写入文件
        return_url = '替换为本地图片路径既可/' + val + '.jpg'
        return return_url


def load_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def modify_user_list(wechat_instance, room_wxid, filename, user, revoke_msg, grant_msg):
    data = load_json(filename)
    if user in data['list']:
        data['list'].remove(user)
        wechat_instance.send_text(to_wxid=room_wxid, content=revoke_msg)
    else:
        data['list'].append(user)
        wechat_instance.send_text(to_wxid=room_wxid, content=grant_msg)
    save_json(filename, data)
def on_recv_text_msg(wechat_instance: ntchat.WeChat, message):
    allRoom = load_json("room.json")
    allPower = load_json("powerlist.json")
    allZhiling = load_json("zhiling.json")

    data = message["data"]
    from_wxid = data["from_wxid"]
    # 可替换机器人控制人账号
    self_wxid = wechat_instance.get_login_info()["wxid"]
    room_wxid = data["room_wxid"]

    for item in allRoom['list']:
        if room_wxid in item:
            for it in allZhiling:
                    should_send = False
                    if it['triggerMode'] == 'contain' and data['msg'].startswith(it['trigger']) and it['sendType'] in ['text', 'img']:
                        should_send = True
                    elif it['triggerMode'] == 'match' and data['msg'] == it['trigger'] and it['sendType'] == 'text':
                        should_send = True
                    elif it['triggerMode'] == 'at' and it['trigger'] in data['at_user_list']:
                        should_send = True
                
                    if should_send:
                        sendMsg(wechat_instance, room_wxid, it['functionName'], it['sendType'], from_wxid, data, it)

            

            if from_wxid == self_wxid and data['at_user_list']:
                if '授权' in data['msg']:
                    modify_user_list(wechat_instance, room_wxid, "powerlist.json", data['at_user_list'][0],
                                     '微信:'+data['at_user_list'][0]+'已取消管理员',
                                     '微信:'+data['at_user_list'][0]+'添加管理员成功\n可指令控制开关机')
                else:
                    modify_user_list(wechat_instance, room_wxid, "blacklist.json", data['at_user_list'][0],
                                     '微信:'+data['at_user_list'][0]+'已解除',
                                     '微信:'+data['at_user_list'][0]+'已被拉黑')

    if from_wxid in allPower['list']:
        allList = load_json("room.json")
        if data['msg'] == '开机':
            wechat_instance.send_text(to_wxid=room_wxid, content='已启动--发送[指令]查看全部指令')
            if room_wxid not in allList['list']:
                allList['list'].append(room_wxid)
                save_json("room.json", allList)
        elif data['msg'] == '关机':
            wechat_instance.send_text(to_wxid=room_wxid, content='已关闭--see you ')
            if room_wxid in allList['list']:
                allList['list'].remove(room_wxid)
                save_json("room.json", allList)



def sendMsg(wechat_instance, room_wxid, funname, type, from_wxid, data, it):
    # 发消息之前判断这个人是否在黑名单中
    blist = load_json("blacklist.json")
    pdata = load_json("powerlist.json")
    if from_wxid in blist['list']:
        wechat_instance.send_text(to_wxid=room_wxid, content='您已被拉黑 别发了[微笑]')
    else:
        if it['needPower'] == True:  # 需要权限的指令
            if from_wxid in pdata['list']:  # 有权限
                if (type == 'text'):
                    wechat_instance.send_text(
                        to_wxid=room_wxid, content=eval(funname))
                else:
                    wechat_instance.send_image(
                        to_wxid=room_wxid, file_path=eval(funname))
            else:  # 没权限
                wechat_instance.send_text(
                    to_wxid=room_wxid, content='您没有该指令权限[微笑]')

        else:  # 不需要权限的指令
            if (type == 'text'):
                wechat_instance.send_text(
                    to_wxid=room_wxid, content=eval(funname))
            else:
                wechat_instance.send_image(
                    to_wxid=room_wxid, file_path=eval(funname))


# 监听接收文本消息
wechat.on(ntchat.MT_RECV_TEXT_MSG, on_recv_text_msg)

# 以下是为了让程序不结束，如果有用于PyQt等有主循环消息的框架，可以去除下面代码
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
