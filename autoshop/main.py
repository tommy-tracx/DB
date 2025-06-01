"""Simple HTTP server exposing diagnostics and vision analysis."""

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from .config import AppConfig
from .diagnostics import interpret_codes
from .vision import analyze_image


class AutoShopHandler(BaseHTTPRequestHandler):
    config = AppConfig()

    def _set_json(self, status=HTTPStatus.OK):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''

        if parsed.path == '/diagnostics':
            try:
                payload = json.loads(body.decode())
                codes = payload.get('codes', [])
                data = interpret_codes(codes, self.config)
                self._set_json()
                self.wfile.write(json.dumps({'results': data}).encode())
            except Exception as exc:
                self._set_json(HTTPStatus.BAD_REQUEST)
                self.wfile.write(json.dumps({'error': str(exc)}).encode())
        elif parsed.path == '/inspect':
            try:
                data = analyze_image(body)
                self._set_json()
                self.wfile.write(json.dumps({'analysis': data}).encode())
            except Exception as exc:
                self._set_json(HTTPStatus.BAD_REQUEST)
                self.wfile.write(json.dumps({'error': str(exc)}).encode())
        else:
            self._set_json(HTTPStatus.NOT_FOUND)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())


def run_server(config: AppConfig = AppConfig()):
    """Run the HTTP server."""
    server = HTTPServer((config.host, config.port), AutoShopHandler)
    print(f'Serving on {config.host}:{config.port}')
    server.serve_forever()


if __name__ == '__main__':
    run_server()
