import requests
import pandas as pd
from bs4 import BeautifulSoup

# to see all column printed in the terminal
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',None)

def fetch_and_save_to_file(url,path):
    r = requests.get(url)
    with open(path,'w',encoding='utf-8') as file:
        file.write(r.text)

# WE WILL SAVE THIS IN THE FILE SO THAT WE DON'T NEED TO MAKE THE WEB REQUEST MULTIPLE TIMES
url_address = 'https://books.toscrape.com/'
fetch_and_save_to_file(url_address,'data/input/books.html')

with open('data/input/books.html',encoding='utf-8') as f:
    html_doc = f.read()

# soupify the html file, so that BeautifulSoup can understand it
soup = BeautifulSoup(html_doc,'html.parser')
book_categories = soup.find('div',class_="side_categories")

categories_list = book_categories.find_all('ul')

# GET THE CATEGORY & THEIR URL
categories = categories_list[1].find_all('li')
category_wise_urls = []
for list_item in categories:
    if list_item:
        list_a = list_item.find('a')
        if list_a:
            category_name = list_a.string.strip()
            category_url = 'https://books.toscrape.com/'+list_a.get('href').strip()
            category_wise_urls.append([category_name,category_url])


# print(category_wise_urls)
category_wise_url_df = pd.DataFrame(category_wise_urls,columns=['category','category_url'])
# saving this data in the csv file in output folder
category_wise_url_df.to_csv('data/output/book_category_urls.csv',index=False)


# STORE THE CATEGORY WISE BOOKS IN THE data folder with category name
for category in category_wise_urls:
    name,url = category
    category_books_path = f'data/input/{name}.html'
    fetch_and_save_to_file(url,category_books_path)


# NOW WE WILL GO TO EACH OF THE BOOK & WILL READ THE BOOK NAME, IT'S URL AND
# first we will get all the books i.e. article tag with class name "product_pod"
category_wise_book_list = []
for category in category_wise_urls:
    name = category[0]
    file_name = f"data/input/{name}.html"
    with open(file_name,encoding='utf-8') as f:
        file_web_data = f.read()

    book_category_soup = BeautifulSoup(file_web_data,'html.parser')
    book_articles = book_category_soup.find_all('article',class_='product_pod')
    category_wise_book_list.append([name,book_articles])

book_list = []
for category,books in category_wise_book_list:
    for book in books:
        book_title = book.find('h3').find('a').get('title').strip()
        book_title_shown = book.find('h3').find('a').string.strip()
        url = 'https://books.toscrape.com/catalogue/'+book.find('h3').find('a').get('href')[9:].strip()
        rating = book.find('p').get('class')[1].strip()
        product_price = book.find('p',class_='price_color').text.replace('Â','').strip()
        availability = book.find('p',class_='instock availability').text.strip()
        # adding the book detail in the list
        book_list.append({
            'full_title':book_title,
            'title_shown':book_title_shown,
            'book_url':url,
            'rating':rating,
            'price':product_price,
            'availability':availability})
#   creating the dataframe & saving the books in a csv file
    books_df = pd.DataFrame(book_list)
    books_df.to_csv(f"data/output/{category}.csv")




