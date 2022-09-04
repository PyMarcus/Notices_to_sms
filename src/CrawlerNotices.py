import time
import httpx
from bs4 import BeautifulSoup
from Whatsapp import WhatsappSender


class Crawler:
    """Crawler de notícias"""
    def __init__(self, site: str) -> None:
        self.__site = site

    @property
    def site(self) -> str:
        return self.__site

    def __get(self) -> bytes:
        """Faz o crawler de noticias"""
        response = httpx.get(self.site)
        if response.status_code == 200:
            return response.content
        else:
            return b'ERROR'

    def __parse(self) -> dict:
        """Trata o html e retorna um dicionario com as informações principais"""
        response = self.__get()
        result: dict = dict()
        if response != b'ERROR':
            parse = BeautifulSoup(response, 'html.parser')
            result['Titulo'] = [i.text for i in parse.findAll('a', {"class": "card-news__text--title main-url"})[10]]
            #result['Imagem'] = [i.attr['src'] for i in parse.findAll('img', {"alt": result['Titulo']})]
            return result
        else:
            return {"Type": "ERROR - BAD CONNECTION OR SOMETHING"}

    def run(self):
        """Executa a busca a cada 3h"""
        while True:
            print(f"Crawling the site")
            WhatsappSender.sendMessage(self.__parse())
            time.sleep(10800)


if __name__ == '__main__':
    spider = Crawler("https://www.terra.com.br/noticias/")
    spider.run()