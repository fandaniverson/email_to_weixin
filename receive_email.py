import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import time
import itchat
import difflib
from tkinter import *
from tkinter import ttk
import _thread
again=''

def connect_popserver():
    email='fand@1ycloud.net'
    password='15533317492Huan'
    pop3_server='pop.exmail.qq.com'
    server = poplib.POP3_SSL(pop3_server,port=995)
    print(server.getwelcome)
    server.user(email)
    server.pass_(password)
    return server
	
def get_mail(server):
    resp, mails, octets = server.list()
    index=len(mails)
    resp, lines, octets = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
#    server.quit()
    msg = Parser().parsestr(msg_content)
    return msg

def get_listbox(master):
    cb = Listbox(master, font=14,height=30,width=40)
    cb.pack(side=LEFT, fill=X, expand=YES)
    f = Frame(master)
    f.pack(side=RIGHT, fill=BOTH, expand=YES)
    lab = Label(master, text='消息记录', font=24)
    lab.pack(side=TOP, fill=BOTH, expand=YES)
    bn = Button(master, text='清除')
    bn.pack()
    return cb



def get_tkinter(cb,msg):
    cb.insert(END,msg)



	

def login_weixin():
    itchat.auto_login(hotReload=True)
    print('login success')
	
def send_error(username,msgs):
#    user=itchat.search_friends(name=username)
    user=itchat.search_chatrooms(name=username)
    un=user[0]['UserName']
    a=itchat.send_msg(msg=msgs,toUserName=un)
    return a

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
	
def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg,indent=0):
    global again
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    # 需要解码Subject字符串:
                    value = decode_str(value).replace(' ','')
                    if value!=again:
                        if ('故障' in value or '失败' in value) and ('中六医院' in value or '中大六院' in value):
                            response=send_error('中六问题反馈群',value)
                            again=value
                            if response['BaseResponse']['ErrMsg']=='请求成功':
                                print(response['BaseResponse']['ErrMsg'])
                            else:
                                print(response['BaseResponse']['ErrMsg'])
                else:
                    print('非法邮件')

if __name__=='__main__':
    try:
        login_weixin()
    except:
        print('login failure')
        time.sleep(60)
        login_weixin()
    while True:
        try:
            server=connect_popserver()
            msg=get_mail(server)
            print_info(msg)
        except:
            print('get_mail exception')
            server=connect_popserver()
            msg=get_mail(server)
            print_info(msg)
            time.sleep(60)
            pass
