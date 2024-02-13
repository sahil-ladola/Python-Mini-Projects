from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os

GMAIL = os.environ.get("GMAIL")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/121.0.0.0 Safari/537.36"
}
URL = ("https://www.amazon.in/Spigen-Lithium-Polymer-Wireless-Charging/dp/B0C5D9734Q/"
       "ref=sr_1_3?keywords=spigen%2Bpower%2Bbank&sr=8-3&th=1")
response = requests.get(url=URL, headers=headers)

webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

product_name = soup.select_one("#productTitle").getText().strip()

price = soup.select_one(".a-price-whole").getText().replace(".", "").replace(",", "")

current_price = int(price)
price_alert = 2100
if current_price < price_alert:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(GMAIL, PASSWORD)
        connection.sendmail(from_addr=GMAIL,
                            to_addrs=GMAIL,
                            msg=f"Subject: Amazon Price Drop Alert!!!\n\n{product_name}\n{URL}\n"
                                f"Current price is below 2100/-".encode("utf-8"))
