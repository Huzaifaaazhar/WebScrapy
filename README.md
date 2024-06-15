# WebScrapy

##### The application is a web scraper that extracts book titles and prices from the website `https://books.toscrape.com/` using BeautifulSoup, optionally interacts with the website through a Chrome browser using Selenium, and securely stores the scraped data into a MySQL database using credentials managed by environment variables loaded from a `.env` file.

*The application starts by importing necessary libraries and modules. These include `requests` for sending HTTP requests, `BeautifulSoup` from the `bs4` library for parsing HTML content, `webdriver` and `By` from Selenium for automating browser interactions, `pymysql` for interacting with a MySQL database, and `load_dotenv` from the `dotenv` package along with the `os` module to manage environment variables. This setup ensures that the application has all the tools it needs to perform web scraping, browser automation, and database interactions.*

*Next, the application loads environment variables from a `.env` file using `load_dotenv()`. These environment variables include database credentials such as host, user, password, and database name. This approach securely manages sensitive information without hardcoding it into the script, enhancing security and flexibility when deploying the application across different environments.*

*The core of the application involves web scraping a website that lists books. It sends a GET request to `https://books.toscrape.com/` and parses the returned HTML content with BeautifulSoup. The application identifies and extracts data on individual books by locating `article` elements with the class `product_pod`. It then iterates through these elements to retrieve the title and price of each book, storing this data in a list named `book_data`.*


###### Finally, the application connects to a MySQL database using credentials loaded from the environment variables. It creates a table named `books` if it doesn't already exist, ensuring that there is a place to store the scraped data. The application then iterates over the `book_data` list, inserting each book's title and price into the database. After committing the transaction to save these changes, it closes the cursor and the database connection. The application concludes by printing a confirmation message indicating that the data has been successfully scraped and stored in the database.
