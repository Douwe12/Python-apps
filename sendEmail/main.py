import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email and password
sender_email = "vandencaviadouwe@gmail.com"
sender_password = "1009isBieb"

# Create the MIME object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = sender_email
message['Subject'] = "Test email from Python"

# Add the email body
body = "This is a test email sent from Python."
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server (in this case, Gmail's SMTP server)
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, sender_email, text)

print("Email sent successfully.")
