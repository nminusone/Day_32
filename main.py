import smtplib
import datetime as dt
import random

now = dt.datetime.now()
print(now.weekday())

my_email = "omar.python1@yahoo.com"
with open('quotes.txt', 'r') as quotes:
    # quote_list = [quotes.readline() for quote in quotes]
    quote_list = quotes.readlines()
daily_quote = random.choice(quote_list)

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
if now.weekday() == 0:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="nagwtkkjtefbonum")
        connection.sendmail(from_addr=my_email, to_addrs="omar.python1@gmail.com",
                            msg=f"Subject: Very Bigly quote of the Day\n\n {daily_quote}")
# connection.close()

# now=dt.datetime.now()
# year=now.year
# print(year)
