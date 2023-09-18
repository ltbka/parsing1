import requests
from bs4 import BeautifulSoup as BS
import csv


#requests - библиотека помогает нам работать с http запросами
# # bs4 - позволяет нам извлекать информацию из html
# данная библиотека разбирается в тэгах , различает от обычного текста
# она может извлекать данные из нужных нам тегов
 
 
def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a', class_='catalog-list-item')
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = ''
        try:
            price = car.find('span', class_="catalog-item-price").text.strip()
        except:
            price = ''
        try:
            img = car.find('img', class_="catalog-item-cover-img").get('src')
        except:
            img = 'нет картинки'
        try:
            info = car.find('span',class_='catalog-item-info').text.strip()
        except:
            info = ''
        try:
            description = car.find('span', class_='catalog-item-descr').text.strip()
        except:
            description = ''

        data = {'title': title,
                'price': price,
                'image':img,
                'info':info,
                'description':description

        }
        write_csv(data)
        
        
def write_csv(data: dict) -> None:
    with open('cars.csv', 'a') as csv_file:
        fieldnames = ['title','price','image','description','info']
        writer = csv.DictWriter(csv_file, delimiter=',',fieldnames=fieldnames)
        writer.writerow(data)
            
            
            
def main():
    # url = 'https://cars.kg/offers'https://cars.kg/offers
    # html = get_html(url)
    # data = get_data(html)
    for page in range(1,20):
        url = f'https://cars.kg/offers/{page}'
        print(f'Парсинг {page} страницы!!')
        html = get_html(url)
        get_data(html)
        print(f'Парсинг {page} страницы завершен!!')   
main()
    
    
    
    
    
    
    
    
    
    
html = get_html('https://cars.kg/offers')
get_data(html)

