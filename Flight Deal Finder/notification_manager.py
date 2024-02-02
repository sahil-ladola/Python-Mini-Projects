import smtplib
import os
MY_GMAIL = os.environ.get("MY_GMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_GMAIL = os.environ.get("TO_GMAIL")


class NotificationManager:
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_GMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_GMAIL,
                                to_addrs=TO_GMAIL,
                                msg=f"Subject:Flight Lowest Price Alert\n\n{message}"
                                )
