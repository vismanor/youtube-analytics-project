import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key = os.getenv('YT_API_KEY')  # Получаем ключ из переменных окружения
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/'+self.__channel_id
        self.subscriber_counter = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """
            метод для операции сложения
        """
        return int(self.subscriber_counter) + int(other.subscriber_counter)

    def __sub__(self, other):
        """
            метод для операции вычитания
        """
        return int(self.subscriber_counter) - int(other.subscriber_counter)

    def __eq__(self, other):
        """
            метод для операции равенства
        """
        return int(self.subscriber_counter) == int(other.subscriber_counter)

    def __gt__(self, other):
        """
            метод для операции сравнения «больше»
        """
        return int(self.subscriber_counter) > int(other.subscriber_counter)

    def __ge__(self, other):
        """
            метод для операции сравнения «больше или равно»
        """
        return int(self.subscriber_counter) >= int(other.subscriber_counter)

    def __lt__(self, other):
        """
            метод для операции сравнения «меньше»
        """
        return int(self.subscriber_counter) < int(other.subscriber_counter)

    def __le__(self, other):
        """
            метод для операции сравнения «меньше или равно»
        """
        return int(self.subscriber_counter) <= int(other.subscriber_counter)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=4, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value

    @classmethod
    def get_service(cls):
        load_dotenv()
        api_key = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        data = self.__dict__
        del (data['channel'])
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
