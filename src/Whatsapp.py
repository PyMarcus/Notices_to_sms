from twilio.rest import Client
from os import getenv
from dotenv import load_dotenv


load_dotenv("./config/.env")


class WhatsappSender:
    """Recebe e envia msg para o whatsapp"""
    def __init__(self) -> None:
        self.__const_account_id = getenv("TWILIO_ACCOUNT_SID")
        self.__const_auth_token = getenv("TWILIO_AUTH_TOKEN")

    @property
    def const_account_id(self) -> str:
        return self.__const_account_id

    @property
    def const_auth_token(self) -> str:
        return self.__const_auth_token

    @staticmethod
    def sendMessage(text: dict) -> None:
        """Envia mensagem para o número determinado"""
        client = Client()
        from_zap_number = getenv("FROM")
        to_zap_number = getenv("TO")
        client.messages.create(body=str(text), from_=from_zap_number, to=to_zap_number)


if __name__ == '__main__':
    wp = WhatsappSender()
    wp.sendMessage()
