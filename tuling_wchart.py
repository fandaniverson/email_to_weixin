# coding:utf-8  
import json
import requests
from wxpy import *

def auto_ai(text):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    api_key="4ef7b54743b94d859f5da6356a314a4e"
    payload={
	"reqType":0,
    "perception": {
        "inputText": {
            "text": text
        }
    },
    "userInfo": {
        "apiKey": "4ef7b54743b94d859f5da6356a314a4e",
        "userId": "397604"
    }
}
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return result["text"]+result["url"]
    else:
        return result['results'][0]['values']['text']
 
 
bot = Bot(None,1,None,None,None,None)#登录缓存
#bot.file_helper.send('[奸笑][奸笑]')
boring_group2=bot.groups().search(u'股票交流群')
boring_group3=bot.groups().search(u'学术交流群')
#frind_dear=bot.friends().search(u'小胸弟')[0]
frind_xiaobo=bot.friends().search(u'卜小波')[0]
frind_daiqiang=bot.friends().search(u'戴强')[0]
frind_feixiong=bot.friends().search(u'飞雄')[0]
@bot.register(boring_group3)
def group_message(msg):
    print('[接收]'+str(msg))
    if(msg.type!='Text'):
        ret= '[奸笑][奸笑]'
    else:
        ret= auto_ai(msg.text)
    print('[发送]'+str(ret))
    return ret

@bot.register(boring_group2)
def group_message(msg):
    print('[接收]'+str(msg))
    if(msg.type!='Text'):
        ret= '[奸笑][奸笑]'
    else:
        ret= auto_ai(msg.text)
    print('[发送]'+str(ret))
    return ret
	
@bot.register(frind_daiqiang)
def forward_message(msg):
    print('[接收]'+str(msg))
    if(msg.type!='Text'):
        ret= '[奸笑][奸笑]'
    else:
        ret= auto_ai(msg.text)
    print('[发送]'+str(ret))
    return ret

@bot.register(frind_xiaobo)
def forward_message(msg):
    print('[接收]'+str(msg))
    if(msg.type!='Text'):
        ret= '[奸笑][奸笑]'
    else:
        ret= auto_ai(msg.text)
    print('[发送]'+str(ret))
    return ret 
 
@bot.register(frind_feixiong)
def forward_message(msg):
    print('[接收]'+str(msg))
    if(msg.type!='Text'):
        ret= '[奸笑][奸笑]'
    else:
        ret= auto_ai(msg.text)
    print('[发送]'+str(ret))
    return ret
embed()
