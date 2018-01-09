# coding: Latin-1
# Copyright © 2018 The Things Network
# Use of this source code is governed by the
# MIT license that can be found in the LICENSE file.


from jose import jwt, JWTError
from utils import read_key as rk


def is_token(string, path):
    key = rk.read_key(path)
    try:
        return bool(jwt.decode(string, key))
    except JWTError:
        return False
