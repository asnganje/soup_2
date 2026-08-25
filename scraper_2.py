import requests
from bs4 import BeautifulSoup

# BASE_URL = "https://books.toscrape.com/"

# res = requests.get(BASE_URL)
# content = res.text
# print(content)

# soup = BeautifulSoup(content, 'lxml')

BASE_URL = "https://quotes.toscrape.com/"

res = requests.get(BASE_URL)
content = res.text
soup = BeautifulSoup(content, "lxml")
title = soup.find('title')
# print(title.text)
quote_1 = soup.find("div", class_="quote")
quote_1_txt = quote_1.find("span", attrs={
  "itemprop":"text"
})
# print(quote_1_txt.text)

tags_title = soup.find("h2", string="Top Ten tags")
tag_box = tags_title.parent
first_tag_span = tags_title.find_next_sibling()
h2_again = first_tag_span.find_previous_sibling()
tag_children = tag_box.children
list_children = list(tag_children)
for child in list_children:
  # print(child)
  pass
final_children = [x for x in list_children if x != "\n"]
for child in final_children:
  # print(child)
  pass
top_tag_a = first_tag_span.a
top_tag_a_href = top_tag_a["href"]
print(top_tag_a_href)