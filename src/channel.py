import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key = os.getenv('YT_API_KEY')  # Получаем ключ из переменных окружения
        self.channel = self.youtube().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=4, ensure_ascii=False))

    def youtube(self):
        return build('youtube', 'v3', developerKey=self.api_key)
