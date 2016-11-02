# -*- coding=utf-8 -*-
import ajax_crawler
import urllib
import requests
import base64
import json
opfile=open("/home/yang/下载/test2.wav")
voiceString=opfile.read()
voiceString=voiceString[0:len(voiceString)]
orig_length=len(voiceString)
voice_base64=base64.b64encode(voiceString)
client_key="entAG8dAdTi4VMOc85QREmRZ"
secret_key="0Cg3Tu5OMw0TU7xl8chazfd44Njtzvza"
requrl = "https://openapi.baidu.com/oauth/2.0/token?"
grant_data="grant_type=client_credentials&client_id="+client_key+"&client_secret="+secret_key
r2=requests.post(requrl,data=grant_data)
js=json.loads(r2.text)
access_token=js["access_token"]
url='http://vop.baidu.com/server_api'
data={
        "format":"wav",
        "rate":16000,
        "channel":1,
        "token":access_token,
        "cuid":"8835005",
        "len":orig_length,
        "speech":voice_base64,
}
if __name__=="__main__":
	update=json.dumps(data)
#	print ajax_crawler.http_post(url,update)

	data_encode=urllib.urlencode(data)
	content_length=str(len(data))
	r=requests.post(url,data=update)
	print r.text