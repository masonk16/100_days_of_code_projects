from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading) 

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

company_url = soup.select_one(selector="p a")
print(company_url)