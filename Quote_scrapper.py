import requests
from bs4 import BeautifulSoup as bs
import csv
import time

url = "https://quotes.toscrape.com/page/1/"
###Create and open excel csv file
with open('quotes_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    file.write("sep=,\n")
    ###Using Quoting style to keep commas and avoid excess coloumns
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Author", "Quote"])
    
    while url: 
        print(f"Looking into: {url}")
        response = requests.get(url)   ### get info from the given link
        soup = bs(response.text, "html.parser")  
        
        containers = soup.find_all("div", class_="quote")
        ###loop on each quote and extract the text and author 
        for item in containers:
            text = item.find("span", class_="text").text   
            author = item.find("small", class_="author").text
            writer.writerow([author, text])
        
        #Automating navigation throgh multiple pages
        next_btn = soup.find("li", class_="next")
        if next_btn:
            relative_url = next_btn.find("a")["href"]
            url = "https://quotes.toscrape.com" + relative_url
            time.sleep(1)
        else:
            url = None
            print("All pages done!")