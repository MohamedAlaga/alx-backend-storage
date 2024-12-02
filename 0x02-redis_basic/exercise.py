import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    """
    class to handle caching to redis db
    """
    _r = redis.Redis()

    def __init__(self) -> None:
        """
        method to initialize redis db
        """
        self._r.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method to store data to redis db
        :param data: data to store
        :return: the id of the stored data
        """
        key = str(uuid.uuid4())
        self._r.set(key, data)
        return key
