import smtplib

my_email = "test@gmail.com"
password = "abcdzyx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="somebodysemail@wp.pl",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

