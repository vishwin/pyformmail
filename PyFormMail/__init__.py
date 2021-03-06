from flask import Flask, request, Response, redirect
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
def email_form():
	for field, data in request.form.items():
		app.config[fields[field]]=data
	msg=EmailMessage()
	msg['Subject']=app.config['FM_SUBJECT']
	msg['To']=Address(addr_spec=app.config['FM_RECIPIENT'])
	msg['From']=Address(display_name=app.config['FM_REALNAME'], addr_spec=app.config['FM_EMAIL'])
	msg_body=app.config['FM_COMMENT']
	msg.set_content(msg_body + """

*********************
Sent from a web form.""")
	with smtplib.SMTP(host=app.config['MAIL_SERVER'], port=app.config['MAIL_PORT']) as s:
		if app.config['MAIL_USE_TLS']:
			s.starttls()
		s.send_message(msg)
	try:
		return redirect(app.config['FM_REDIRECT'])
	except:
		return Response("Your message has been sent. The complete email source code is below:\n\n" + msg.as_string(), mimetype='text/plain')
