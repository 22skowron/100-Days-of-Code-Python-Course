import requests
from bs4 import BeautifulSoup
from pprint import pprint

##################################################
    # Some content from website.html
    
with open(file="website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# pprint((soup.findAll("a")))

anchor_tags = soup.find_all("a")
print(type(anchor_tags))

for a in anchor_tags:
    print(a.get("href"))

print("\n")

h1_with_id = soup.find(name="h1", id="name")
print(type(h1_with_id))
print(h1_with_id)

print(type(soup.select_one(selector="p a")))

kwiat_tag = soup.select_one("li[kwiat]")
print(kwiat_tag.attrs)
print(kwiat_tag.string)
print("\n")

##################################################
    # Find the most liked article from Hacker News

response = requests.get(url="https://news.ycombinator.com/news")
soup2 = BeautifulSoup(response.text, "html.parser")

title_spans = soup2.find_all(name="span", class_="titleline")
titles = [span.a.string for span in title_spans]
# pprint(titles)

    # Find the maximum amount of likes scored
score_spans = soup2.find_all(name="span", class_="score")
scores = [int(span.string.split()[0]) for span in score_spans]
max_value = str(max(scores))
# print(max_value)

    # Find the id of the element which contains strived for inf
for score in score_spans:
    if score.string.split()[0] == max_value:
        entry_number = score.get("id").split("_")[1]
        # print(entry_number)

            # Get the desirable inf
        most_liked_entry = soup2.find(id=entry_number).find(name="span", class_="titleline").a
        print(f"The most liked article: '{most_liked_entry.string}'")
        print(f"Likes: {max_value}")
        print(f"Link: {most_liked_entry.get("href")}")







