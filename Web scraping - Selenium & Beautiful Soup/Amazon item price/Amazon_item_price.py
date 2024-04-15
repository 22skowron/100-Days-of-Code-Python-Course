from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = ("https://www.amazon.pl/LEGO-21028-Architecture-Doroslych-Kolekcjonerski/"
       "dp/B012NOGGHQ/ref=pd_bxgy_img_d_sccl_1/259-0703604-0426542?pd_rd_w=Nj78O"
       "&content-id=amzn1.sym.faf33128-2883-499e-8326-de79a730baf8&pf_rd_p=faf33128"
       "-2883-499e-8326-de79a730baf8&pf_rd_r=C1P1AGKCR46VEQAAHM5V&pd_rd_wg=8tpYX"
       "&pd_rd_r=59224d8a-c050-4ecb-9716-6bae78f2042e&pd_rd_i=B012NOGGHQ&th=1")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
          "Accept-Language": "pl,de;q=0.9,pl-PL;q=0.8,en-US;q=0.7,en;q=0.6"}

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

product_title = driver.find_element(by=By.ID, value="productTitle")
price_whole = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction")
print(f"{product_title.text} is now available for {price_whole.text},{price_fraction.text}.")

time.sleep(3)
driver.close()