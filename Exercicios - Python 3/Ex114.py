import requests

def verificar_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'O site: {url}, \033[32mestá acessivel!\033[m ')
        else:
            print(f'O site {url} retornou o status {response.status_code}. ')
    except requests.exceptions.ConnectionError:
        print(f'O site: {url}, \033[31mnão está acessivel!\033[m ')


verificar_site('http://www.youtube.com')