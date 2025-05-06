import json
import requests
import os
import logging
import urllib.request as request
import urllib.parse

# 日志配置
logger = logging.getLogger("BotUtils")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# JSON文件读写

def load_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"读取JSON文件失败: {file}, {e}")
        return {}

def save_json(file, data):
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.warning(f"写入JSON文件失败: {file}, {e}")

# 权限/黑名单管理

def modify_user_list(filename, user, revoke_msg, grant_msg, wechat, room_wxid):
    data = load_json(filename)
    if user in data.get('list', []):
        data['list'].remove(user)
        wechat.send_text(to_wxid=room_wxid, content=revoke_msg)
    else:
        data.setdefault('list', []).append(user)
        wechat.send_text(to_wxid=room_wxid, content=grant_msg)
    save_json(filename, data)

def check_permission(user, powerlist):
    return user in powerlist.get('list', [])

def check_blacklist(user, blacklist):
    return user in blacklist.get('list', [])

# 天行API请求统一封装
def call_tianapi(endpoint, params, api_key):
    params['key'] = api_key
    api_url = f'https://apis.tianapi.com/{endpoint}/index'
    try:
        resp = requests.post(api_url, data=params, timeout=5)
        result = resp.json()
        if result.get('code') == 200:
            return result['result']
        else:
            return f"接口异常: {result.get('msg', '未知错误')}"
    except Exception as e:
        logger.warning(f"天行API请求异常: {e}")
        return f"请求异常: {e}"

# 兼容原有的urllib方式天气API
def tianqi(city, api_key):
    api_url = 'https://api.tianapi.com/tianqi/index'
    params_dict = {
        "city": city,
        "key": api_key,
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
                    temperature = result['newslist'][0]['lowest'] + '—' + result['newslist'][0]['highest']
                    sunrise = result['newslist'][0]['sunrise']
                    sunset = result['newslist'][0]['sunset']
                    weather = result['newslist'][0]['weather']
                    wind = result['newslist'][0]['wind']
                    windsc = result['newslist'][0]['windsc']
                    tips = result['newslist'][0]['tips']
                    return (f"城市：{area}\n日期：{date}\n温度：{temperature}\n日出：{sunrise}\n日落：{sunset}\n天气：{weather}\n风向：{wind}\n风力：{windsc}\n提示：{tips}")
                else:
                    return ("nono查不到")
            except Exception as e:
                return (f"解析结果异常：{e}")
        else:
            return ("阿,别查了")
    except Exception as err:
        return (f"天气API请求异常: {err}") 