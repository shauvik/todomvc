#!/usr/bin/env python
import SimpleHTTPServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Content-Security-Policy", "script-src 'self' https://staging.fullstory.com 'sha256-R2EJrrc1Xe7kp1EihvCYwjaX0CsK1PmTmU5TakO9XeU=' 'nonce-EDNnf03nceIOfn39fn3e9h3sdfa'") #'unsafe-inline'   https://staging.fullstory.com


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)
