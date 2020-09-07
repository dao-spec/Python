from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email.mime.multipart import  MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'liu.weitao@cesgroup.com.cn'
password = 'wasd1234Ces'
to_addr = 'skyline_dao@163.com' 
smtp_server = 'smtp.mxhichina.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Python test <%s>' % from_addr)
msg['To'] = _format_addr('接收者 <%s>' % to_addr)
msg['Subject'] = Header('通知:图文')

msg.attach(MIMEText('hello, this mail is send by liu-wt!', 'plain', 'utf-8'))

with open('/Users/Dao/Project/Project/python-demo/thumbnail.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='thumbnail.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='thumbnail.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    print(f)
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.starttls()
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr,from_addr], msg.as_string())
# server.quit()