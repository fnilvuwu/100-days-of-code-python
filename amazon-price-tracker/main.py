import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = ""
password = ""
url = "https://www.amazon.com/Instant-Pot-Programmable-Pressure-Steamer/dp/B01B1VC13K/ref=pd_vtp_sccl_4/142-0349101-7757720?pd_rd_w=gbCmz&pf_rd_p=016e3697-91be-4dc2-9533-ef9350e7e73d&pf_rd_r=TC1N7ETR1D8ZWH40NK85&pd_rd_r=5ac42233-80a4-43bd-bcea-1465b94dd413&pd_rd_wg=sSxai&pd_rd_i=B01B1VC13K&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "en-US,en;q=0.5"
}

connection = smtplib.SMTP("smtp.gmail.com")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
title = soup.find(name="span", id="productTitle").getText().encode(
    'utf-8').strip()
price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(title)
print(price_as_float)

if price_as_float < 100:
    message = f'{title} is now {price}'

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"""Subject:Amazon Price Alert!\n\n{message}\n{url}"""
    )
    connection.close()
