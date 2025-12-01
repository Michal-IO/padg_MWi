

class Airport:
    def __init__(self, name:str, location: str, code: str):
        self.name = name
        self.location = location
        self.code = code
        self.coords = self.get_coordinates()

    def get_coordinates(self):
            import requests
            from bs4 import BeautifulSoup
            url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/123.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            # print(response.text)
            response_html = BeautifulSoup(response.text, "html.parser")
            # print(response_html.prettify())
            latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
            # print(latitude)
            longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
            # print(longitude)
            return [latitude, longitude]


def add_airport(airports_list: list):
    print('Adding airports...')
    name = input('Wprowadź nazwe lotniska: ')
    location = input('Wprowadź miasto: ')
    code = input('Wprowadź kod lotniska: ')
    print("Lotnisko dodane")
    airports_list.append(Airport(name, location, code))

def airport_info(airports_list: list):
    for airport in airports_list:
        print(f'Lotnisko {airport.name} w miejscowości {airport.location}')

def delete_airport(airports_list: list):
    tmp_name = input('Wprowadz nazwe lotniska do usunięcia: ')
    for airport in airports_list:
        if airport.name == tmp_name:
            airports_list.remove(airport)

def update_airport(airports_list: list):
    tmp_name = input('Wprowadz nazwe: ')
    for airport in airports_list:
        if airport.name == tmp_name:
            airport.name = input('Wprowadz nazwe: ')
            airport.location = input('Wprowad<UNK> miasto: ')
            airport.code = input('Wprowad<UNK> kod lotniska: ')
            airport.coords = airport.get_coordinates()