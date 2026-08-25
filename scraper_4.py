import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl

book_dict = {
    "name": [],
    "price": [],
    "category": [],
    "stars": [],
    "upc": [],
    "availability": [],
    "in_stock": [],
    "image_link": []
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

number_dict = {"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5"}

books_url = "https://books.toscrape.com/"
res = requests.get(books_url, headers=headers)
res.encoding = "utf-8"
content = res.text
soup = BeautifulSoup(content, "lxml")
pages_str = soup.find("li", class_="current").text.strip().split(" ")[-1]
pages_count = int(pages_str)
# books = soup.find_all("h3")
# # urls = [url.a["href"] for url in books]
# print(urls)

# https://books.toscrape.com/catalogue/page-1.html

for page_no in range(1, pages_count-44):
    print(f"Page no:{page_no}...")
    page_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
    res = requests.get(page_url, headers=headers)
    res.encoding = "utf-8"
    content = res.text
    soup = BeautifulSoup(content, "lxml")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        book_url = "https://books.toscrape.com/catalogue/" + \
            book.find("a")["href"]
        res = requests.get(book_url, headers=headers)
        res.encoding = "utf-8"
        content = res.text
        soup = BeautifulSoup(content, "lxml")

        book_inner_content = soup.find("div", class_="product_main")
        book_name = book_inner_content.h1.text  # name
        book_dict["name"].append(book_name)
        price = book_inner_content.find("p", class_="price_color").text
        book_dict["price"].append(price)
        ul_container = soup.find("ul", class_="breadcrumb")
        li_items = ul_container.find_all("li")
        category = li_items[2].a.text
        book_dict["category"].append(category)
        star_p_element = book_inner_content.find("p", class_="star-rating")
        star_class_name_list = star_p_element["class"]
        star_rating = int(number_dict[star_class_name_list[-1]])
        book_dict["stars"].append(star_rating)
        product_details = soup.find("article", "product_page")
        upc = product_details.table.find(
            "th", string="UPC").find_next_sibling().text
        book_dict["upc"].append(upc)
        availability = soup.find(
            "th", string="Availability").find_next_sibling().text
        book_dict["availability"].append(availability)
        in_stock = int(availability.split("(")[1].split(" ")[0])
        book_dict["in_stock"].append(in_stock)
        image_link = "https://books.toscrape.com"+soup.find("img")["src"][5:]
        book_dict["image_link"].append(image_link)
df = pd.DataFrame(book_dict)
df.to_excel("book.xlsx")

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
