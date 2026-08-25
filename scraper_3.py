import requests
from bs4 import BeautifulSoup

number_dict = {"One":"1", "Two":"2","Three":"3","Four":"4", "Five":"5"}

book_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

res = requests.get(book_url)
res.encoding="utf-8"
content= res.text
soup = BeautifulSoup(content, "lxml")

book_inner_content = soup.find("div", class_="product_main")
h1 = book_inner_content.h1.text #name
price = book_inner_content.find("p", class_="price_color").text
ul_container = soup.find("ul", class_="breadcrumb")
li_items = ul_container.find_all("li")
category = li_items[2].a.text
star_p_element = book_inner_content.find("p", class_="star-rating")
star_class_name_list = star_p_element["class"]
star_rating = int(number_dict[star_class_name_list[-1]])
product_details = soup.find("article", "product_page")
upc = product_details.table.find("th", string="UPC").find_next_sibling().text
availability = soup.find("th", string="Availability").find_next_sibling().text
in_stock = int(availability.split("(")[1].split(" ")[0])
image_link = "https://books.toscrape.com"+soup.find("img")["src"][5:]
print(image_link)