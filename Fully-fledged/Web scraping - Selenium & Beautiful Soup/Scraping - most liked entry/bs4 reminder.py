import requests
from bs4 import BeautifulSoup
from pprint import pprint

with open(file="website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

elements = soup.find_all("li")
elements = soup.select_one("body")

# print(elements)
print(elements.p)
# pprint(type(elements))