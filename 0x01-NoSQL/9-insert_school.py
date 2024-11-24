#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    :param mongo_collection:
    :param kwargs:
    :return:
    """
    return mongo_collection.insert_one(kwargs)
