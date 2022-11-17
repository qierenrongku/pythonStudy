# _*_ coding:utf-8 _*_
'''
@File       :Convert_hex_to_base64.py
@Time       :2022/11/13 0:30
@Author     :且任荣枯
@Version    :1.0

'''
import struct

import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('原始值:', values)
print('格式符:', s.format)
print('占用字节:', s.size)
print('打包结果:', binascii.hexlify(packed_data))