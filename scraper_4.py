import requests
from bs4 import BeautifulSoup

books_url = "https://books.toscrape.com/"
res = requests.get(books_url)
res.encoding = "utf-8"
content= res.text
soup = BeautifulSoup(content, "lxml")
pages_str = soup.find("li", class_="current").text.strip().split(" ")[-1]
pages_count = int(pages_str)
# books = soup.find_all("h3")
# # urls = [url.a["href"] for url in books]
# print(urls)

#https://books.toscrape.com/catalogue/page-1.html

for page_no in range(1, pages_count+1):
  print(f"Page.....->{page_no}")
  page_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
  res = requests.get(page_url)
  res.encoding = "utf-8"
  content= res.text
  soup = BeautifulSoup(content, "lxml")
  books = soup.find_all("article", class_="product_pod")
  print(len(books))

# page_no = 45
# while True:
#     print(f"Page.....->{page_no}")
#     page_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
#     res = requests.get(page_url)
#     res.encoding = "utf-8"
#     content= res.text
#     soup = BeautifulSoup(content, "lxml")
#     books = soup.find_all("article", class_="product_pod")
#     next_btn = soup.find("li", class_="next")
#     print(len(books))
#     if next_btn is None:
#       break
#     else:
#       page_no += 1

