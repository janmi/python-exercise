from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
	sender = '627943558@qq.com'
	receivers = ['joy@mmldigi.com']
	message = MIMEText('用python发送邮件实力代码', 'plain', 'utf-8')
	message['From'] = Header('完大锤', 'utf-8')
	message['To'] = Header('赵晓玫', 'utf-8')
	smtper = SMTP('smtp.qq.com')
	smtper.login(sender, '123456')
	smtper.sendmail(sender, receivers, message.as_string())
	print('邮件发送成功')

if __name__ == '__main__':
	print('开始发送邮件')
	main()