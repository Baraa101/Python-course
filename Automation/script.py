import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


now = datetime.datetime.now()

# email content
content = ''


# extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News Storie....')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text + '\n'+'<br>')
                if tag.text != 'More' else '')
    return (cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# sending the email
print('Composing Email')

# update your email detils

SERVER = 'smtp.gmail.com'  # smtp server
PORT = 587  # port number
FROM = 'garmian.game@gmail.com'
TO = 'garmian.game@gmail.com'
PASS = 'ohgjbvxypijkuafw'

# fp = open (file_name,'rb)
# create a text/plain message
# msg=MIMEText('')
msg = MIMEMultipart()

# msg.add header('Contrent-Disposition', 'attachment,filename='empty.txt)
msg['Subject'] = 'Top News Stories HN [Automated Email]' + \
    ' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

# fo.close()

print('Intitiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP SLL('smtp.gmail.com,456)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
