from flask import Flask, request
from os import environ

import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

app=Flask(__name__)
app.config.from_pyfile('default.cfg')
if 'FORMMAIL_CONFIG' in environ:
	app.config.from_envvar('FORMMAIL_CONFIG')
from PyFormMail.fieldmap import fields

@app.route('/', methods=['POST'])
def root():
	for field, data in request.form.items():
		app.config[fields[field]]=data
	msg=EmailMessage()
	msg['Subject']=app.config['FM_SUBJECT']
	msg['To']=Address(addr_spec=app.config['FM_RECIPIENT'])
	msg['From']=Address(display_name=app.config['FM_REALNAME'], addr_spec=app.config['FM_EMAIL'])
	msg.set_content("""If you are reading this, the Flask app successfully sent this test message. You may now delete this message.

-- 
Your friendly Flask app""")
	with smtplib.SMTP(host=app.config['MAIL_SERVER'], port=app.config['MAIL_PORT']) as s:
		s.send_message(msg)
	return "Check your inbox; message has sent"
