# encoding=utf-8

from concurrent.futures import ThreadPoolExecutor, wait
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import base64
from email import encoders as Encoders

import logging

logger = logging.getLogger(__name__)

number_threads = 2
pool = ThreadPoolExecutor(number_threads)
futures = []


def log_result(future):
    logger.info(future.result())


def send_email(subject, text_content, to_list, alternatives=None, attachments=None, images=None):
    logger.info("email of {} will be sent asynchronously".format(subject))
    future = pool.submit(send_email, subject, text_content, to_list, alternatives, attachments, images)
    future.add_done_callback(log_result)


def _invoke_send_email(from_address, passwd, to_addresses, subject, msg_body, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = ",".join(to_addresses) if isinstance(to_addresses, list) else to_addresses
    msg['Subject'] = subject
    msg.attach(MIMEText(msg_body, 'plain'))

    for file in attachments:
        with open(file, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        filename = os.path.basename(file)
        name_base64 = base64.b64encode(filename.encode('utf-8'))
        name_format = "=?UTF-8?B?" + name_base64.decode() + "?="
        part.add_header('Content-Disposition', 'attachment', filename=name_format)
        Encoders.encode_base64(part)
        msg.attach(part)
    # smtp = smtplib.SMTP()
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login(from_address, passwd)
    smtp.sendmail(from_address, to_addresses, msg.as_string())
    smtp.quit()
