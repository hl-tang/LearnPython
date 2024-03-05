# https://docs.python.org/3/library/json.html
# https://www.youtube.com/watch?v=WsenyJ18ykU JSONを解説！( jsonモジュール ) 〜VTuberと学習〜
# https://www.w3schools.com/python/python_json.asp

import json
# json也就是键值对，就和python的dict(hash map)的数据结构是一样
# python中处理json对象是把它作为字符串，str(json)和dict(python)之间変換

# 幾つかの注意点

""" JSON对象作为字符串,最外面用单引号包起来.直接用dict格式{k: v}报错
TypeError: the JSON object must be str, bytes or bytearray, not dict """

""" 注意JSON的key-value若是字符串必须是双引号"包起来的，不能是'否则
JSONDecodeError: Expecting property name enclosed in double quotes
所以里面的key-val都是双引号(当然key即属性,肯定都是"),最外面单引号表示JSON字符串 """

'''
JSON: null, true/false
Python: None, True/False
'''

# 1. Convert from Python(dict) to JSON(str)    json.dumps()
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# a Python object (dict)
x = {
    "name": "ジョン",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "福特 Edge", "mpg": 24.1}
    ]
}
# convert into JSON
print(json.dumps(x))    # 非英语字符变unicode了
x_json = json.dumps(x, indent=4, ensure_ascii=False)
print(x_json)
# the result is a JSON string
print(type(x_json))

# 2. Convert from JSON(str) to Python(dict)    json.loads()
# some JSON
x = '{"id": 123, "is_student": true}'
# parse json
x_obj = json.loads(x)
# the result is a Python dictionary
print(x_obj)
print(x_obj['is_student'])
print(type(x_obj))

print(json.loads(x_json)["cars"][1]["model"])
