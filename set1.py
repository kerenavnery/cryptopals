# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:37:49 2020

@author: Keren
"""
import codecs
def hex_to_base_64_conv(hex_stream):
    raw = codecs.decode(hex_stream, 'hex')
    b64 = codecs.encode(raw, 'base64')
    b64string = b64.decode().replace('\n', '')
    
    return b64string

    
def fixed_xor(in1, in2):
    bytes_in1 = codecs.decode(in1, 'hex')
    bytes_in2 = codecs.decode(in2, 'hex')
    int_out = int.from_bytes(bytes_in1, 'little') ^ int.from_bytes(bytes_in2, 'little')
    bytes_out = int_out.to_bytes(len(bytes_in1), 'little')
    out = codecs.encode(bytes_out,'hex')
    return out