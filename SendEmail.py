import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Watch GPU situation
YesGPU = False
NoGPU = 1
availableMemory=[]
i = 0
while YesGPU == False and i != 6:
    time.sleep(10)
    r = os.popen("nvidia-smi")
    text = r.read()
    availableMemory.clear()
    for i in range (0,6): # I have 6 GPUs
        index = text.find('/ 11441')  # Each one is 11441mb
        availableMemory.append(int(text[int(index)-9:int(index)-4]))
        print(availableMemory[i])
        text = text[index+10:]
        if int(availableMemory[i]) < 8000: # less than 8000 regard as available
            YesGPU = True
    r.close()
    print(availableMemory)

# Send email
MemorySize = min(availableMemory) # find the most available GPU No.
MemoryNo = availableMemory.index(min(availableMemory))
print(MemorySize,MemoryNo)
sender = '*********@163.com' # Sender email address
receiver = list()
receiver.append('**********@qq.com') # Receiver email address
copyReceive = list()
copyReceive.append(sender)
username = '******@163.com' # log in to the email sever
password = '*********'# password
mailall=MIMEMultipart()
mailall['Subject'] = 'GPU' + str(MemoryNo) + 'Avaliable' + str(MemorySize) + 'MB' # Subject of the email
mailall['From'] = sender
mailall['To'] = ';'.join(receiver)
mailall['CC'] = ';'.join(copyReceive)
mailcontent = 'None'
mailall.attach(MIMEText(mailcontent, 'plain', 'utf-8'))
mailAttach = 'None'
contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)
# filename = '????.txt'#????????
# attfile = MIMEBase(maintype, subtype)
# attfile.set_payload(open(filename, 'rb').read())
# attfile.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', filename))
# mailall.attach(attfile)
fullmailtext = mailall.as_string()
smtp = smtplib.SMTP_SSL()
print("Connecting")
smtp.connect("smtp.163.com")
print("Logining")
smtp.login(username, password)
print("Sending")
smtp.sendmail(sender, receiver, fullmailtext)
smtp.quit()
print("finished")