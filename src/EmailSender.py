import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(to, msg, subj = "Fakes", user="mail@gmail.com", pwd="1234"):
        emsg = MIMEMultipart()
        emsg['From'] = user
        emsg['To'] = to
        emsg['Subject'] = subj
        emsg.attach(MIMEText(msg, 'plain'))
        text = emsg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, text)
        server.quit()
