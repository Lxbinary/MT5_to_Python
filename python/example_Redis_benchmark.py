# -*- coding: utf-8 -*-
"""
@authors: [Lxbot]
"""
import ast
import redis
from datetime import datetime

pair = 'EURUSD_i'

r = redis.StrictRedis('localhost', 6379, db=0, decode_responses=True)
X = {}

while True:
    X = r.get(pair)
    if X is not None:
        X = ast.literal_eval(X)
        print('Data in:', datetime.now().strftime('%H:%M:%S.%f')[:-3], 'len:', len(X),)
        r.flushdb()