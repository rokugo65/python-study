import json
import requests

print('郵便番号を入力してください')
zipcode = input()

url = 'http://zipcloud.ibsnet.co.jp/api/search'
param = {'zipcode': zipcode}

proxies = {
    "http":"http://name:pass@proxy.toppan.co.jp:8088",
    "https":"http://name:pass@proxy.toppan.co.jp:8088"
}

res = requests.get(url, params=param)
response = json.loads(res.text)
address = response['results'][0]

print(response)
print(address['address1'] + address['address2'] + address['address3'])
