import datetime as dt
import smtplib

my_email = "motivationlists14@yahoo.com"
password = "pleasedonotgotothisaccount"

with smtplib.SMTP("smtp.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject:Hello\n\nThis is the body of my email."
    )

