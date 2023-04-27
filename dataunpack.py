import msgpack
import json

with open('data.msgpack', 'rb') as f:
    data = msgpack.unpack(f, raw=False)
    with open('data.json','a') as jf:
        jf.write(data)

print(data)
