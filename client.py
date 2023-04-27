import http.client
import msgpack

data = {'name': 'Alice', 'age': 25}
encoded_data = msgpack.packb(data, use_bin_type=True)

while(True):
    conn = http.client.HTTPConnection("localhost:8080")
    conn.request("POST", "/", encoded_data)
    response = conn.getresponse()
    print(response.status, response.reason)

conn.close()
