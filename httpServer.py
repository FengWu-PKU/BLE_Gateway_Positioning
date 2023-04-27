import http.server
import socketserver
import threading
import msgpack
import json


PORT = 8080
id=0

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        global id
        with open('DATA/data.json', 'a') as f:
            f.write('"data')
            f.write(str(id))
            f.write('": ')
        id+=1
        with open('DATA/data.json', 'ab') as f:
            f.write(data)
        with open('DATA/data.json', 'a') as f:
            f.write(',')
            f.write('\n')
        # with open('DATA/data.msgpack', 'ab') as f:
        #     f.write(data)

        # # Store the data in an json file
        # decoded_data = msgpack.unpackb(data, raw=False)
        # with open('DATA/data.json', 'a') as jf:
        #     json.dump(decoded_data, jf)
        #     jf.write('\n')


        self.send_response(200)
        self.end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

Handler = RequestHandler
httpd = ThreadedHTTPServer(("", PORT), Handler)

print("serving at port", PORT)

# Start a thread with the server -- that thread will then start one
# more thread for each request
server_thread = threading.Thread(target=httpd.serve_forever)
# Exit the server thread when the main thread terminates
server_thread.daemon = True
server_thread.start()
httpd.serve_forever()


