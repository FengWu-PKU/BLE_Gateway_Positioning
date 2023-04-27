import msgpack
import json

with open('DATA/data.msgpack', 'rb') as f:
    data = msgpack.unpack(f, raw=False)
    with open('DATA/data.json','a') as jf:
        json.dump(data, jf)

# print(data)
