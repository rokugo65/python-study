import sys
import json
import requests

class AddressRetrieval :

    def ZipCode2Address(self, _inPostalCode):
        zipCode = _inPostalCode
        url = 'http://zipcloud.ibsnet.co.jp/api/search'
        param = {'zipcode': zipCode}

        proxies = {
        "http":"http://name:pass@proxy.toppan.co.jp:8088",
        "https":"http://name:pass@proxy.toppan.co.jp:8088"
        }

        res = requests.get(url, params=param, proxies=proxies)
        response = json.loads(res.text)
        address = response["results"][0]

        return address['address1']+address['address2']+address['address3']

