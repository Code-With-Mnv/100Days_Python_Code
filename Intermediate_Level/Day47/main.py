import smtplib

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}
access_the_site = requests.get(
    url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
    headers=headers,
)
soup = BeautifulSoup(access_the_site.text, "html.parser")

price = float(soup.find(name="span", class_="a-price-whole").getText())

MSG = f"SUBJECT: Price Drop Notification\n\nTHe product that your was looking for, is available at {price}$."

if price < 100.00:
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(user="codewithmanav70@gmail.com", password="sfgy ussm cqcy seps")
    server.sendmail(
        from_addr="codewithmanav70@gmail.com", to_addrs="manavfun0@gmail.com", msg=MSG
    )
