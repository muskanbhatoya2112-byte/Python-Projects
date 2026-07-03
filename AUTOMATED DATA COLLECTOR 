import requests
from bs4 import BeautifulSoup
import csv


url = "https://books.toscrape.com/"


response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


books = soup.find_all("article", class_="product_pod")


with open("books.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

   
    writer.writerow(["Book Name", "Price", "Rating"])

   
    for book in books:

        name = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        writer.writerow([name, price, rating])

print("Data collected successfully!")
print("Saved in books.csv") 