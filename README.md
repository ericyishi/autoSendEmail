# autoSendEmail
### 使用
```
 * 运行： python auto_sendEmail.py
 该文件是无法运行的，使用前需要，修改auto_sendEmail.py里面的配置，以下参数根据实际情况修改
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
```
### 功能说明
* 文件一共分为三个功能
  1. 执行测试用例，生成美化报告。可以参考https://github.com/ericyishi/HTMLTestRunner_PY3
  2. 找出最新日期的报告
     ```
      def find_newfile(test_dir):
        """找到最新日期的报告"""
        lists = os.listdir(test_dir)
        ##最后对lists元素，按文件修改时间大小从小到大排序
        lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
        # 获取最新文件【排序后的最后一个】的绝对路径
        file_path = os.path.join(test_dir, lists[-1])
        return file_path
     ```
  3. 以邮件的方式发送

### 备注
  * 可以配合Jenkins完成持续集成


