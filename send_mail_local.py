#!/bin/usr/env python
# -*- coding=UTF-8 -*-

import smtplib
from email import encoders
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
 
mailto_list=["chris@company.com","andy@company.com"] 
#mail_host="smtp.company.local:25" #"smtp.XXX.com"  #设置服务器
mail_host="127.0.0.1" #"smtp.XXX.com"  #设置服务器
#mail_user="mobile-reportdata"    #用户名
mail_user="nobody_butyou"    #用户名
#mail_pass="3%redDog$#"   #口令 
mail_pass="any"   #口令 
mail_postfix="company.com"  #发件箱的后缀
    

def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me= mail_user+"@"+mail_postfix   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器        
        s.login(mail_user,mail_pass)  #登陆服务器
        s.set_debuglevel(True)
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        #s.send_raw_email(msg.as_string(), source=me, destinations=to_list)
        s.close()
        return True  
    except Exception, e:  
        print str(e)  
        return False  

def send_multipart(to_list,sub,content):
    me= mail_user+"@"+mail_postfix   #这里的hello可以任意设置，收到信后，将按照设置显示
    
    msg = MIMEMultipart()
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)    
    #msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()
    
    # 邮件正文是MIMEText:
    msg.attach(MIMEText(content, 'html', 'utf-8'))
    
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('baidu.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='baidu.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<tupian1>')
        mime.add_header('X-Attachment-Id', 'tupian1')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)   

    with open('baidu.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='tupian2.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='tupian2.png')
        mime.add_header('Content-ID', '<tupian2>')
        mime.add_header('X-Attachment-Id', 'tupian2')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
        
    try:  
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器        
        #s.login(mail_user, mail_pass)  #登陆服务器
        s.set_debuglevel(True)
        s.sendmail(me, to_list, msg.as_string())  #发送邮件        
        s.close()
        return True  
    except Exception, e:  
        print str(e)  
        return False  


if __name__ == '__main__':  
    #if send_mail(mailto_list,"hello",u"<a href='www.company.com'>本地邮件测试</a>"):  
    #    print u"发送成功"  
    #else:
    #    print u"发送失败"  
    
    if send_multipart(mailto_list,"hello",u"<a href='www.company.com'>本地邮件测试</a> <img src='cid:tupian1'>"):  
        print u"发送成功"  
    else:
        print u"发送失败"  
