from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
