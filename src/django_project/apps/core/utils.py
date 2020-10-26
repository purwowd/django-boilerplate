import fileinput
import os
import re
import sys

from django.conf import settings
from django.utils.crypto import get_random_string


def generate_secret_key(length=50):
    """
    Return a 50 character random string
    usable as a `SECRET_KEY` setting value.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    if not isinstance(length, int):
        raise TypeError(
            f'invalid literal for int() with base 10: {length}')
    return get_random_string(length, chars)
