#!/usr/bin/env python

import sys
import BaseHTTPServer
import json
import subprocess, os
from SimpleHTTPServer import SimpleHTTPRequestHandler

sys.stderr.write("{}".format(os.environ))

with open("/var/packages") as json_file:
    json_data = json.load(json_file)
    print json_data
    
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        if s.path == "/":
            s.wfile.write("<h3> applications </h3>\n")
            for key in json_data["installed"].keys():
                 s.wfile.write("<a href=\"/run/{}\">{}</a></br>".format(key, key))
        if s.path == "/json":
            s.wfile.write(json.dumps(json_data))
        if s.path.split("/")[1] == "run":
            print("run " + s.path.split("/")[2] + " [{}]".format(json_data["installed"][s.path.split("/")[2]]))
            subprocess.Popen(json_data["installed"][s.path.split("/")[2]])

print("Serving on port 8000")

server_class = BaseHTTPServer.HTTPServer
httpd = server_class(("0.0.0.0", 8000), MyHandler)
try:
    httpd.serve_forever()
except:
    pass
