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
from bot_utils import load_json, save_json, modify_user_list, check_permission, check_blacklist, call_tianapi, tianqi

# ========== 配置区 ==========
CONFIG = {
    "openai_org": "xxxx",
    "openai_key": "xxxx",
    "tianapi_key": "xxxx",
    "img_dir": "./resources/imgList/",
    "log_level": "ERROR"
}
os.environ['NTCHAT_LOG'] = CONFIG["log_level"]

wechat = ntchat.WeChat()


# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)

# ========== 数据加载 ==========
injson = load_json("data.json")
injson2 = load_json("four.json")
allZhiling = load_json("zhiling.json")

chatData = []

def chatgptai(val):
    #用户发言
    data = {"role": "user", "content": val}
    #首次把用户发言加入数组中
    chatData.append(data)
    #组织名及api填写
    openai.organization = CONFIG["openai_org"]
    openai.api_key = CONFIG["openai_key"]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatData
    )
    #把回复内容也加进去，下次用
    chatData.append(completion.choices[0].message)
    return completion.choices[0].message.content.replace('\n', '')

def chatgptimg(val):
    openai.organization = CONFIG["openai_org"]
    openai.api_key = CONFIG["openai_key"]
    completion = openai.Image.create(
        prompt=val,
        n=1,
        size="512x512"
    )
    image_url = completion.data[0].url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    r = requests.get(image_url, headers=headers)
    imgName = val + str(random.randint(1, 999))
    bendi_url = CONFIG["img_dir"] + imgName + '.jpg'
    with open(bendi_url, mode="wb") as f:
        f.write(r.content)  # 图片内容写入文件
    return_url = '本地文件夹路径' + imgName + '.jpg'
    return return_url

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
    return call_tianapi('mgjuzi', {}, CONFIG["tianapi_key"])


def qinghua():
    return call_tianapi('saylove', {}, CONFIG["tianapi_key"])


def shi():
    return call_tianapi('qingshi', {}, CONFIG["tianapi_key"])


def emo():
    return call_tianapi('hsjz', {}, CONFIG["tianapi_key"])


def tiangou():
    return call_tianapi('tiangou', {}, CONFIG["tianapi_key"])


def aini():
    return call_tianapi('caihongpi', {}, CONFIG["tianapi_key"])


def wenan():
    return call_tianapi('pyqwenan', {}, CONFIG["tianapi_key"])


def taici():
    res = call_tianapi('dialogue', {}, CONFIG["tianapi_key"])
    if isinstance(res, dict):
        return f"{res.get('dialogue', '')}—{res.get('source', '')}"
    return res


def penren():
    text_url = "https://v.api.aa1.cn/api/api-wenan-ktff/index.php?type=" + \
        str(random.randint(1, 5))

    response = requests.get(text_url)
    res = response.json()
    text = res['text'].replace('\n', '')
    return text


def saohua():
    text_url = "https://v.api.aa1.cn/api/api-saohua/index.php?type=json"

    response = requests.get(text_url)
    res = response.json()
    text = res['saohua'].replace('\n', '')
    return text


def four():
    return injson2[random.randint(0, len(injson2)-1)]['text']


def kou6():
    return injson[random.randint(0, len(injson)-1)]['text']


def zhiling_text():
    # @property {String}			triggerMode			匹配模式
    # @property {String}			trigger			    匹配关键词
    # @property {String}			functionName	    调用方法名
    # @property {String}			sendType			发送消息类型
    # @property {Boolean}			needPower			是否需要权限

    return '1.6\n2.舔\n3.emo\n4.爱你\n5.文案\n6.情诗\n7.情话\n8.句子\n9.台词\n10.开喷\n11.发烧\n12.星期四\n13.天气-xxx\n15.转图-xxx'


def yiqing(val):
    api_url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    params_dict = {}
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            result = json.loads(content)
            if result['ret'] == 0:
                china_data = result['data']['diseaseh5Shelf']['areaTree'][0]['children']
                for item in china_data:
                    if (val in item['name']):
                        return (f"城市：{item['name']}\n今日新增确诊：{item['today']['local_confirm_add']}\n今日本地确诊：{item['today']['confirm']}\n今日无症状新增：{item['today']['wzz_add']}\n中风险地区数量：{item['total']['mediumRiskAreaNum']}\n高风险地区数量：{item['total']['highRiskAreaNum']}\n数据更新时间：{item['total']['mtime']}")
                    if (item['children']):
                        for it in item['children']:
                            if (val in it['name']):
                                return (f"城市：{it['name']}\n今日新增确诊：{it['today']['local_confirm_add']}\n今日本地确诊：{it['today']['confirm']}\n今日无症状新增：{it['today']['wzz_add']}\n中风险地区数量：{it['total']['mediumRiskAreaNum']}\n高风险地区数量：{it['total']['highRiskAreaNum']}\n数据更新时间：{it['total']['mtime']}")
            else:
                return "交一下钱谢谢"
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
        bendi_url = CONFIG["img_dir"] + val + '.jpg'
        with open(bendi_url, mode="wb") as f:
            f.write(r.content)  # 图片内容写入文件
        return_url = '替换为本地图片路径既可/' + val + '.jpg'
        return return_url


def jiqi(val):
    api_url = 'https://apis.tianapi.com/robot/index'
    params_dict = {
        "key": CONFIG["tianapi_key"],
        "question": val
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            result = json.loads(content)
            if result['code'] == 200:
                return result['result']['reply']
            else:
                return "我卡啦卡啦"
        else:
            return "我卡啦卡啦"
    except error.HTTPError as err:
        return ('我卡啦卡啦')
    except error.URLError as err:
        # 其他异常
        return (err)


# ========== 指令函数映射 ==========
FUNC_MAP = {
    'minguo': minguo,
    'qinghua': qinghua,
    'shi': shi,
    'emo': emo,
    'tiangou': tiangou,
    'aini': aini,
    'wenan': wenan,
    'taici': taici,
    'penren': penren,
    'saohua': saohua,
    'four': four,
    'kou6': kou6,
    'zhiling_text': zhiling_text,
    'texttoimg': texttoimg,
    'jiqi': jiqi,
    'yiqing': yiqing,
    'chatgptai': chatgptai,
    'chatgptimg': chatgptimg,
    'tianqi': lambda val: tianqi(val, CONFIG["tianapi_key"]),
}

# ========== 消息处理 ==========
def sendMsg(wechat_instance, room_wxid, funname, type, from_wxid, data, it):
    blist = load_json("blacklist.json")
    pdata = load_json("powerlist.json")
    if check_blacklist(from_wxid, blist):
        wechat_instance.send_text(to_wxid=room_wxid, content='您已被拉黑 别发了[微笑]')
        return
    if it['needPower']:
        if check_permission(from_wxid, pdata):
            result = call_func(funname, data)
            if type == 'text':
                wechat_instance.send_text(to_wxid=room_wxid, content=result)
            else:
                wechat_instance.send_image(to_wxid=room_wxid, file_path=result)
        else:
            wechat_instance.send_text(to_wxid=room_wxid, content='您没有该指令权限[微笑]')
    else:
        result = call_func(funname, data)
        if type == 'text':
            wechat_instance.send_text(to_wxid=room_wxid, content=result)
        else:
            wechat_instance.send_image(to_wxid=room_wxid, file_path=result)

def call_func(funname, data):
    # 解析函数名和参数
    if '(' in funname:
        fname = funname.split('(')[0]
        argstr = funname[funname.find('(')+1:funname.find(')')]
        if argstr:
            # 只支持data['xxx']或data['msg'].split('xxx')[1]等简单表达式
            try:
                arg = eval(argstr, {}, {'data': data})
                return FUNC_MAP[fname](arg)
            except Exception as e:
                return f"指令参数解析错误: {e}"
        else:
            return FUNC_MAP[fname]()
    else:
        return FUNC_MAP[funname]()

@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
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
                    modify_user_list("powerlist.json", data['at_user_list'][0],
                                     '微信:'+data['at_user_list'][0]+'已取消管理员',
                                     '微信:'+data['at_user_list'][0]+'添加管理员成功\n可指令控制开关机', wechat_instance, room_wxid)
                else:
                    modify_user_list("blacklist.json", data['at_user_list'][0],
                                     '微信:'+data['at_user_list'][0]+'已解除',
                                     '微信:'+data['at_user_list'][0]+'已被拉黑', wechat_instance, room_wxid)

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

# ========== 主循环 ==========
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
