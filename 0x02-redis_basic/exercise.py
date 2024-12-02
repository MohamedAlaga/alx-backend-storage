#!/usr/bin/env python3
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any


def count_calls(func: Callable) -> Callable:
    """wrapper to count the number of times a given function is called."""

    @wraps(func)
    def invoker(self, *args, **kwargs) -> Any:
        """invoker"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(func.__qualname__)
        return func(self, *args, **kwargs)

    return invoker


class Cache:
    """Represents an object for storing data in a Redis data storage.
    """

    def __init__(self) -> None:
        """Initializes a Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage using key."""
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """Retrieves a value from a Redis data storage using key."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage.
        """
        return self.get(key, lambda x: int(x))
