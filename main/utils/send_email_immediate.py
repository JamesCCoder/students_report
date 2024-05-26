import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os



def send_email(subject, body, to, file_path, email_user, email_pass, email_host, email_port):

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ', '.join(to)
    msg['Subject'] = subject


    msg.attach(MIMEText(body, 'plain'))


    part = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as file:
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        msg.attach(part)

    # Link to SMTP server and send email
    try:
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, to, msg.as_string())
        server.quit()
        print(f"The report is sending to: {', '.join(to)}")
    except Exception as e:
        print(f"The sending is failed: {e}")
