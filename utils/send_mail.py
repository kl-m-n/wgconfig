# Send mail utility

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText, MIMEBase
from email import encoders
from wgconfig.utils.vars import logger, mail_server, mail_port, mail_username, mail_password, mail_from

# Send mail with attachment
def send_mail(to, subject, body, attachment=None):
	# Create a message
	msg = MIMEMultipart()
	msg['From'] = mail_from
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))

	# Attach file
	if attachment:
		with open(attachment, 'rb') as f:
			part = MIMEBase('application', 'octet-stream')
			part.set_payload(f.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', f'attachment; filename=vpn_domain_com.conf')
		msg.attach(part)

	# Send the message
	try:
		if mail_port == 465:
			server = smtplib.SMTP_SSL(mail_server, mail_port)
		else:
			server = smtplib.SMTP(mail_server, mail_port)
			if mail_port == 587:
				server.starttls()
		if mail_username and mail_password:
			server.login(mail_username, mail_password)
		server.sendmail(mail_from, to, msg.as_string())
		server.quit()
		logger.info(f'Mail sent to {to}')
	except Exception as e:
		logger.error(f'Error sending mail to {to}: {e}')
		raise