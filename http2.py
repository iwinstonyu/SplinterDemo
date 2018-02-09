#!/usr/bin/env python
#coding=utf-8
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urllib

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")
        
        if '?' in self.path:
			query = urllib.splitquery(self.path)
			action = query[0]
 
        if query[1]:#接收get参数
			queryParams = {}
			for qp in query[1].split('&'):
				kv = qp.split('=')
				queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
				content+= kv[0]+':'+queryParams[kv[0]]+"\r\n"
 
        #指定返回编码
        enc="UTF-8"
        content = content.encode(enc)
        f = io.BytesIO()
        f.write(content)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        shutil.copyfileobj(f,self.wfile)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.unquote(datas).decode("utf-8", 'ignore')#指定编码方式
        datas = transDicts(datas)#将参数转换为字典
        if datas.has_key('data'):
			content = "data:"+datas['data']+"\r\n"
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()