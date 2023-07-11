# import pandas as pd
import requests
from urllib.parse import urlparse
import telegram 
import pyshorteners

proxies = {
    'http': 'https://51.159.195.117/search?q=%27https%3A%2F%2Fcatalog.wb.ru%2Fcatalog%2Felectronic22%2Fcatalog%3FappType%3D1%26curr%3Drub%26dest%3D-1257786%26regions%3D80%2C38%2C4%2C64%2C83%2C33%2C68%2C70%2C69%2C30%2C86%2C75%2C40%2C1%2C66%2C110%2C22%2C31%2C48%2C71%2C114%26sort%3Dpopular%26spp%3D0%26subject%3D515%26page&__cpo=aHR0cHM6Ly93d3cuYmluZy5jb20',
}

def get_category(page_number):
    # url = f'https://catalog.wb.ru/catalog/electronic22/catalog?appType=1&curr=rub&dest=-1257786&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&sort=popular&spp=0&subject=515&page={page_number}'
    # headers = {
    #     'Accept': '*/*',
    #     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'Connection': 'keep-alive' ,
    #     'Origin': 'https://www.wildberries.ru', 
    #     'Referer': 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony', 
    #     'Sec-Fetch-Dest': 'empty', 
    #     'Sec-Fetch-Mode': 'cors' ,
    #     'Sec-Fetch-Site': 'cross-site' ,
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    #     'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': 'Windows' 
    #     }
    url = f'https://catalog.wb.ru/catalog/kitchen15/catalog?appType=1&cat=8705&curr=rub&dest=-1257786&page=1&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&sort=popular&page={page_number}' 
    headers = {'Accept' : '*/*', 
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': 'https://www.wildberries.ru/catalog/dom-i-dacha/kuhnya/kuhonnaya-utvar',
            'Sec-Fetch-Dest': 'empty', 
            'Sec-Fetch-Mode': 'cors', 
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
            'sec-ch-ua-mobile' : '?0', 
            'sec-ch-ua-platform': 'Windows'
            }
# фирма экструдер
    # url =  f'https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=main_page_rates&TestID=186&appType=1&curr=rub&dest=-1257786&page={page_number}&query=%27rcnhelth&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&resultset=catalog&sort=popular&spp=0&suppressSpellcheck=false'
    # headers = {'Accept': '*/*', 
    #     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'Connection': 'keep-alive', 
    #     'Origin': 'https://www.wildberries.ru', 
    #     'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%27rcnhelth', 
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'cross-site',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    #     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"', 
    #     'sec-ch-ua-mobile': '?0', 
    #     'sec-ch-ua-platform': '"Windows"', 
    #     }
    
    response = requests.get(url=url, headers=headers, proxies=proxies)

    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)
    # print(products_raw)
    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None),
                'id': product.get('id', None),
                'priceU': float(product.get('priceU', None)) / 100 if product.get('priceU', None) != None else None,
                'salePriceU': float(product.get('salePriceU', None)) / 100 if product.get('salePriceU',
                                                                                          None) != None else None,
            })

    return products

def main():
    all_data = {
        'brand': [],
        'name': [],
        'sale': [],
        # 'id': [],
        'priceU': [],
        'salePriceU': [],
        'href' : []
    }

    for page_number in range(1, 101):
        response = get_category(page_number)
        products = prepare_items(response)
        
        for product in products:
        
            if (int(product['priceU']) - (int(product['priceU']) / 100 * 80)) >= int(product['salePriceU']):
                string = ('https://www.wildberries.ru/catalog/' + str(product['id']) + '/detail.aspx')
             
                # all_data['brand'].append(product.get('brand', None))
                all_data['name'].append(product.get('name', None))
                all_data['brand'].append(product.get('brand', None))
                all_data['sale'].append(product.get('sale', None))
    
        
                all_data['priceU'].append(float(product.get('priceU', None))  if product.get('priceU', None) != None else None)
                all_data['salePriceU'].append(float(product.get('salePriceU', None))  if product.get('salePriceU', None) != None else None)
                all_data['href'].append(string)
        data_list = list(zip(*all_data.values()))
        
        data_list1 = []
        for i in data_list:
            # if i[0] == 'EXTRUDER':
                data_list1.append(i[5])
                # print(i)
    return data_list1
    # делаем короткую ссылку
    #     data_list2_short = []
    #     def shorten_url(url):
    #         s = pyshorteners.Shortener()
    #         shortened_url = s.tinyurl.short(url)
    #         return shortened_url

    #         # Пример использования
    #     for long_url in data_list1:
    #         short_url = shorten_url(long_url)
    #         data_list2_short.append(short_url)
    # return data_list2_short
        
            
if __name__ == '__main__':
    main()