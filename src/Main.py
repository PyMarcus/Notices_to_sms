import argparse
from CrawlerNotices import Crawler


def treat_argline() -> None:
    """trata a linha de comandos"""
    parse = argparse.ArgumentParser(description="Send notices to SMS")
    parse.add_argument("-execute", help="Start the bot", required=True, type=str)
    arg = parse.parse_args()
    if arg.execute:
        spider = Crawler("https://www.terra.com.br/noticias/")
        spider.run()


if __name__ == '__main__':
    treat_argline()
