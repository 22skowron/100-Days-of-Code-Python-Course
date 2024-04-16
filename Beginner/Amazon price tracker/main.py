import requests
from bs4 import BeautifulSoup
from pprint import pprint


URL = ("https://www.amazon.pl/LEGO-21028-Architecture-Doroslych-Kolekcjonerski/"
       "dp/B012NOGGHQ/ref=pd_bxgy_img_d_sccl_1/259-0703604-0426542?pd_rd_w=Nj78O"
       "&content-id=amzn1.sym.faf33128-2883-499e-8326-de79a730baf8&pf_rd_p=faf33128"
       "-2883-499e-8326-de79a730baf8&pf_rd_r=C1P1AGKCR46VEQAAHM5V&pd_rd_wg=8tpYX"
       "&pd_rd_r=59224d8a-c050-4ecb-9716-6bae78f2042e&pd_rd_i=B012NOGGHQ&th=1")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
          "Accept-Language": "pl,de;q=0.9,pl-PL;q=0.8,en-US;q=0.7,en;q=0.6"}

response = requests.get(url=URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find(name="span", class_="a-offscreen")
# print(price_tag)

price_whole = int(price_tag.string.split(",")[0])
price_fraction = int(price_tag.string.split(",")[1].strip("zł"))

price = price_whole + price_fraction / 100

if price < 150:
       print("ITEM ON SALE !!!")
       print(f"Current price: {price}zł")
else:
       print("Price still not low enough.")
       print(f"Current price: {price}zł")

