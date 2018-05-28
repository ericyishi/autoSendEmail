import base64
import os
import smtplib
import unittest
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from HTMLTestRunner import HTMLTestRunner


def create_report(testcase_dir,test_report_dir):
    """执行测试用例，生成新的报告"""
    discover=unittest.defaultTestLoader.discover(testcase_dir, pattern='test_*.py')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    isExists=os.path.exists(test_report_dir)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(test_report_dir)
    filename = test_report_dir+'\\'+ now + 'result.html'
    fp=open(filename ,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    runner.run(discover)

def find_newfile(test_dir):
    """找到最新日期的报告"""
    lists = os.listdir(test_dir)
    ##最后对lists元素，按文件修改时间大小从小到大排序
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件【排序后的最后一个】的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path

def send_email(filepath):
    """邮件发送"""
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码
    user = 'xxx@163.com'
    # 修改成你自己邮箱的授权码
    password = 'xxx'
    # 发送邮箱
    sender = 'xxx@163.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['xxx@qq.com', 'xxx@163.com']
    # 发送邮件主题
    subject ='xx系统报告：'+ get_filename(filepath).split(".")[0]
    # 邮件正文
    content='<html><div>各位领导，同事：你们好！</div><div>这是xx系统的报告，请查看附件！</div></html>'

    att = MIMEText(open(filepath, 'rb').read(), 'base64', 'UTF-8')
    att["Content-Type"] = 'application/octet-stream'
    # 定义附件的名字，同时使用base64转码这样传输中文才不乱码
    att.add_header('Content-Disposition', 'attachment',
                   filename='=?utf-8?b?' + str(base64.b64encode(get_filename(filepath).encode('UTF-8')), encoding="utf8") + '?=')

    msgRoot = MIMEMultipart('alternative')
     # 正文
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
    # 邮件的标题
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = sender
    msgRoot['to'] = ','.join(receiver)
    msgRoot.attach(att)

    # 连接发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

def get_filename(filepath):
    filename=filepath.split("\\")[-1]
    return filename

if(__name__=="__main__"):
    testcase_dir=r'D:\yis_python\autoSendEmail\test_case'
    test_report_dir=r'D:\yis_python\autoSendEmail\testReport'
    create_report(testcase_dir,test_report_dir)
    report=find_newfile(test_report_dir)
    # print(report)
    send_email(report)

