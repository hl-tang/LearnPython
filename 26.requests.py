# 郵便番号を投げて、対する住所を取得
# 郵便番号検索API:  https://zipcloud.ibsnet.co.jp/doc/api
# 直接浏览器 https://zipcloud.ibsnet.co.jp/api/search?zipcode=6068306

# 注意`requests`是第三方库，需要`pip install requests`
import requests

res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=1110053')
print(res) # Response object
print(type(res))
print(res.text) # json字符串
print(type(res.text))
print(res.status_code)
print(type(res.status_code))
print(res.json()) # 返回response json对应的python dict
print(type(res.json()))

# query parameter
base_URL = 'https://zipcloud.ibsnet.co.jp/api/search'
zipcode = "6068306" # a dictionary of strings, 最好都是str
res = requests.get(base_URL, params={"zipcode": zipcode})
print(res.url)
print(res.text)
print(res.json()["message"], res.json()["results"][0]["address1"])

def zipcode2address(zipcode: int) -> str:
    res = requests.get(base_URL, params={"zipcode": str(zipcode)})
    if res.status_code == 200 and res.json()["message"] == None:
        return res.json()["results"][0]["address1"] + \
            res.json()["results"][0]["address2"] + res.json()["results"][0]["address3"]
    else:
        return res.json()["message"] + str(res.status_code) + ' ' +str(res.json()["status"])
        # 这网站提供的api很迷，明明应该status_code返回400的，却还是200

print(zipcode2address(1110052))
print(zipcode2address(11100520))
