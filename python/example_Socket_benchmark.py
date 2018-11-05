# -*- coding: utf-8 -*-
"""
@authors: [Lxbot]
"""

import socket
from datetime import datetime

port = 9411

sock = socket.socket()
sock.bind(("127.0.0.1", port))
sock.listen(10)

# в бесконечном цикле ждем и читаем данные
while True:
    X = []
    conn, addr = sock.accept()
    data = conn.recv(16384)
    if not data:
        print("No data")
        conn.close()
        continue
    else:
        udata = data.decode("utf-8")
        X = udata.replace('\x00', '').split(',')
        print('DATA in', datetime.now().strftime('%H:%M:%S.%f')[:-3], 'len:', len(X),)
        