#!/usr/bin/python3

'''
This python script looks up a key from a nested object and returns its value. If the key doesn't exist, it returns `None`.
'''

import sys
import json
import argparse
import logging
from functools import reduce


logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger('challenge-3')
logger.setLevel(logging.INFO)


class ObjectKeyStartsOrEndsWithUnexpectedChar(Exception):
    '''
    Raised when nested object key starts or ends with a non-alphabet character
    '''
    pass


def is_object_key_valid(object_key):
    if not object_key[0].isalnum() or not object_key[-1].isalnum():
        raise ObjectKeyStartsOrEndsWithUnexpectedChar(
            'Object key starts or ends with an unexpected character'
        )
    return True


def get_nested_object_val(nested_object, object_key, default=None):
    logger.info(f'Nested object: {nested_object}')
    logger.info(f'Nested object key to retrieve its value: {object_key}')

    assert is_object_key_valid(object_key)

    return reduce(
        lambda nested_obj, obj_key: nested_obj.get(obj_key, default)
        if isinstance(nested_obj, dict) else default, object_key.split("/"),
        nested_object
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--nested_object",
        type=json.loads,
        required=True,
        help="Nested object data"
    )
    parser.add_argument(
        "--object_key",
        type=str,
        required=True,
        help="Nested object data key to retrieve its value"
    )
    args = parser.parse_args()
    nested_object = args.nested_object
    object_key = args.object_key

    object_value = get_nested_object_val(
        nested_object, object_key, default=None
    )
    logger.info(f'Nested object value for {object_key} is {object_value}')


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
