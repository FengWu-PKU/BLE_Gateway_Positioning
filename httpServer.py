import http.server
import socketserver
import threading
import msgpack
import json

PORT = 8080

class RequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        # with open('data.json', 'ab') as f:
        #     f.write(data)
        with open('DATA/data.msgpack', 'ab') as f:
            f.write(data)

        # Store the data in an json file
        decoded_data = msgpack.unpackb(data, raw=False)
        json_data=json.dumps(decoded_data)
        with open('DATA/data.json', 'a') as jf:
            jf.write(json_data)
            jf.write('\n')


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
