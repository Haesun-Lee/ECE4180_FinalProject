import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

fromaddr = "dydrkfl9797@gmail.com"
toaddr = "jjjleee10@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Today's attendance"

body = "Today's attendance"

msg.attach(MIMEText(body, 'plain'))

now = datetime.today().strftime('%Y-%m-%d')
now = now +'.xls'

filename = now
path = '/home/heyjueun/opencv-3.3.0/data/haarcascades/'
path = path + now
attachment = open(path, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(fromaddr, "@2Ne1090517")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()