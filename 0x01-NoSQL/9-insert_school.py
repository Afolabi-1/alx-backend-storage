#!/usr/bin/env python3
'''Adetunji Afolabi
'''


def insert_school(mongo_collection, **kwargs):
    '''
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
