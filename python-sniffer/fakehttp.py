#Copyright Jon Berg , turtlemeat.com

import time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import pri

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if "connectivity.txt" in self.path:
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("AV was here!")
                return
            elif "generate_204" in self.path:   #our dynamic content
                self.send_response(204)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("")
                return
            elif "netdetect" in self.path:
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("MobileQQ2")
                return
            elif "connCheck" in self.path:
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("MobileQQ1")
                return
            else:
                self.send_response(404)
                self.wfile.write("")
                return
        except:
            pass
     

    def do_POST(self):
        try:
            if "netdetect" in self.path:
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("MobileQQ2")
                return
            elif "connCheck" in self.path:
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("MobileQQ1")
                return
            else:
                self.send_response(404)
                self.wfile.write("")
                return
        except:
            pass

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

