import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    _r = redis.Redis()

    def __init__(self):
        self._r.flushdb(True)

    def store(self, data : Union[str,bytes,int,float]) -> str:
        key = str(uuid.uuid4())
        self._r.set(key, data)
        return key
