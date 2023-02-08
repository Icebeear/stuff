import smtplib
class NotificationManager:
    def send_mail(self, subject, sms):
        with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
            connection.starttls()
            connection.login(user="example", password="example")
            connection.sendmail(
            from_addr="example", 
            to_addrs="example", 
            msg=f"Subject:{subject}\n\n{sms}"
            )