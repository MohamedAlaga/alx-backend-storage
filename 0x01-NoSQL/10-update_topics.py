#!/usr/bin/env python3
"""
Insert a document in Python
"""


def update_topics(mongo_collection, name, topics):
    """
    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
