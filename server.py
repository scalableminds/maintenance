import os
import posixpath
import urllib
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class RequestHandler(SimpleHTTPRequestHandler):

    def translate_path(self, path):
        """translate all paths to single file"""

        return os.path.join(os.getcwd(), "index.html")

    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.
        """
        path = self.translate_path(self.path)
        f = None
        ctype = 'text/html'
        try:
            f = open(path, 'r')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(503)
        self.send_header("Content-type", ctype)
        self.end_headers()
        return f

if __name__ == '__main__':
    BaseHTTPServer.test(RequestHandler, BaseHTTPServer.HTTPServer)