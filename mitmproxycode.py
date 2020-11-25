import json
from mitmproxy import http
from pprint import pprint


def respone(flow: http.HTTPFlow):
    if "quote.json" in flow.request.url:
        # 接收返回信息
        data = json.loads(flow.response.content)
        # 对数据进行修改
        newData = jsonTravel(data, num=10, text=2)
        # 格式化数据，方便打印
        dataMess = json.dumps(newData, indent=2, ensure_ascii=False)
        print(dataMess)
        # 替换返回值
        flow.response.text= dataMess


def jsonTravel(data, array=None, num=1, text=1):
    # 如果是字典，对字典进行遍历
    if isinstance(data, dict):
        newData = dict()
        for k, v in data.items():
            newData[k] = jsonTravel(v, array, num, text)
            if k == 'name':
                newData[k] = jsonTravel(v, array, num, text=2)
    # 如果是列表，对列表进行遍历
    elif isinstance(data, array):
        newData = list()
        for i in data:
            newItem = jsonTravel(i, array, num, text)
            if array is None:
                newData.append(newItem)
            else:
                pass
    # 如果是字符串，则和text相乘，实现对字符串的修改
    elif isinstance(data, str):
        newData = data * text
    # 如果是个整形或者浮点型，则和num相乘
    elif isinstance(data, int) or isinstance(data, float):
        newData = data * num
    # 传入什么返回什么
    else:
        newData = data
    return newData


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.url:
        # 获取请求返回的json
        data = json.loads(flow.response.content)
        # 修改name字段，拼接test
        data['data']['items'][1]['quote']['name'] = data['data']['items'][1]['quote']['name'] * 2
        data['data']['items'][2]['quote']['name'] = " "
        # 打印修改后的data
        pprint(data)
        # 替换response data
        flow.response.text = json.dumps(data)



# def request(flow: http.HTTPFlow):
#     # redirect to different host
#     if "quote.json" in flow.request.url:
#         with open("/Users/lixu/project/tmp/quote.json") as f:
#             flow.response = http.HTTPResponse.make(200, f.read(), )
