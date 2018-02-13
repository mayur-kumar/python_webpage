import requests
from bs4 import BeautifulSoup

def get_pice():
    request = requests.get("https://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("span", {"itemprop":"price", "class":"now-price"})
    string_price = element.text.strip() #The price with pound sign
    return float(string_price[1:])

def compare_price():
    current_price = get_pice()
    if current_price > 200:
        print("The chair is very expensive !!")
    elif current_price == 200:
        print("The price is exactly 200. Make your decision.")
    else:
        print("Buy it right away")

def string_experiments():
    random_string = "this is a random string."
    print(random_string.endswith("ng"))

string_experiments()