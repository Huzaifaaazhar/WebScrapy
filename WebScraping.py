#Importing necessary libraries.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql
from dotenv import load_dotenv
import os

# Load environment variables and retrieving database credentials from environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Web scraping with BeautifulSoup
response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')

# Extract book titles and prices
book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_data.append((title, price))

# Automate browser interaction with Selenium
driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/')
driver.quit()

# Store data in MySQL using pymysql
conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (title VARCHAR(255), price VARCHAR(255))")

#Insert scraped book data in the database.
for book in book_data:
    cursor.execute("INSERT INTO books (title, price) VALUES (%s, %s)", book)

conn.commit()
cursor.close()
conn.close()
print("Data scraped and stored in database")
