from email.parser import Parser
import poplib

email = 'liu.weitao@cesgroup.com.cn'
password = 'wasd1234Ces'
pop3_server = 'pop3.mxhichina.com'

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message: %s.size: %s' % server.stat())

resp, mails, octets = server.list()
print(mails)

index = len(mails)
print('index', index)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)


server.quit()
