import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
my_email = os.environ["my_email"]
password = os.environ["password"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url="https://www.amazon.in/Cetaphil-Cleansing-Non-Irritating-Dermatologist-Recommended/dp/B01CCGW732/ref=sr_1_5?cr"
                            "id=2K8NX0W6HY0A9&dib=eyJ2IjoiMSJ9.RNvdgy5V2sIkdN7ov1Y8OZIoNO8q88X8su6xq5hHD7adqXVT681VAn62xCchNPAmwIs4OA6g2OG0"
                            "Jn5A1VrbvjAwRE2YcfY3xsSncyAiB1hQzI6-dWMwvPVgAi6AllwWsGbFeKlSXJ9eXdmcn38hwBmkG8jr5FrQGCKRyNc9q-9bqTVLdzH9LrQppQwzp"
                            "dG6pGAgSY5t0kjw3m-V2NJzocKPWuERMMJBh8sXLvnQZlmATNhfT0D_z5jdItHO0OzgBl38f5h7cT6phqqOd_-9jc210a4dbQpbBSVcJF8hKHs.vJI1kZQO6jWQKhoQ_2VXPh28Mj4cSmL12p1TxRlQ-D4&dib_tag=se&k"
                            "eywords=cetaphil%2Bface%2Bwash%2Bfor%2Boily%2Bskin&qid=1771471988&sprefix=cet%2Caps%2C358&sr=8-5&th=1", headers=headers)
web_txt=(response.text)
soup = BeautifulSoup(web_txt, "html.parser")
price = soup.find(name="span", class_="a-price-whole")

final_price=(float(price.text))
if final_price<= 540:
     print(True)
     with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(my_email, password)
         connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"Subject: Price Drop!!! {final_price}")
