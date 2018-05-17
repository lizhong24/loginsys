import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'loginsys.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自lz的测试邮件', 'xxx@163.com', 'xxx@qq.com'
    text_content = '欢迎访问，人生苦短，我学Python！'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.baidu.com</a>，这里是百度！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
