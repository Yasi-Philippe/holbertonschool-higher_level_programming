#!/usr/bin/python3
"""Script to set up a local server to handle a small API"""


import http.server
import socketserver
import json


class my_server_handler(http.server.BaseHTTPRequestHandler):
    """A class to handle the server"""
    def do_GET(self):
        """Function to handle GET requests"""
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"name": "John",
                                         "age": 30,
                                         "city": "New York"}).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        elif self.path == "/":
            message = "Hello, this is a simple API!"
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("localhost", PORT), my_server_handler) as httpd:
    httpd.serve_forever()
