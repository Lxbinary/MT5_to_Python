# -*- coding: utf-8 -*-
"""
@authors: [Lxbot]
"""
import ast
import redis

pair = 'EURUSD_i'
# Setup Redis
redis_db = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )

pair_data = redis_db.get(pair)
print("Source data from Redis po ", pair)
print(pair_data)
print("__________________")

# обработка в словарь
pair_data = ast.literal_eval(pair_data)

# обращаемся к конкретному значению словаря
print("data RSI_2 : ")
print(pair_data['RSI_2'])
print("__________________")