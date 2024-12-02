import redis
import uuid
from typing import Union


class Cache:
    _r = redis.Redis()

    def __init__(self):
        self._r.flushdb()

    def store(self, data : Union[str,bytes,int,float]) -> str:
        key = uuid.uuid4()
        self._r.set(str(key), data)
        return str(key)
