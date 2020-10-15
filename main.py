import requests
import json
import time

class Parser5ka:
    __params = {
        'records_per_page': 50
    }
    __headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    def __init__(self, start_url):
        self.start_url = start_url

    def parse(self, url=None):
        if not url:
            url = self.start_url
        params = self.__params
        while url:
            response = requests.get(url, params=params, headers = self.__headers)
            time.sleep(500)
            if params:
                params = {}
            data: dict = response.json()
            url = data['next']

            for product in data['results']:
                self.save_to_json_file(product)

            def save_to_json_file(self, product: dict):
                with open(f'products/{product["id"]}.json', 'w', encoding='UTF-8') as file:
                    json.dump(product, file, ensure_ascii=False)

if __name__ == '__main__':
    parser = Parser5ka('https://5ka.ru/special_offers/')
    parser.parse()