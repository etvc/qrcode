#!/usr/bin/env python
# -*- coding:utf-8 -*-

import qr

print('Content-Type: ' + qr.mimetype(qr.FMT_ASCII))
print(qr.qrcode('spam, egg', format = qr.FMT_ASCII))
