import requests

def get_cotacao(destino):

    url = 'https://api.exchangerate-api.com/v4/latest/' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:       
        
        return data["rates"]

    else:
        print('erro ao obter cotações: ', response.status_code)
        return None

def converter_cotacao(origem = 'USD', destino = 'BRL', valor = 1): 
    rates = get_cotacao(destino)
    return round(1 / rates[origem], 4)