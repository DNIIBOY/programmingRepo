from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import json


class TestHTTPHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self) -> None:
        """
        Handles POST requests
        """
        content_length = int(self.headers["Content-Length"])  # Gets the size of data
        post_data = self.rfile.read(content_length)  # Gets the data itself
        post_data = json.loads(post_data.decode("utf-8"))  # Parse as json
        print("Receive: ", post_data, "\n")
        response = {
            'id': 'fakechat',
            'object': 'chat.completion',
            'created': 12345678,
            'model': 'FAKEGPT',
            'choices': [
                {
                    'index': 0,
                    'message': {
                        'role': 'assistant',
                        'content': 'This is a test response'
                    },
                    'finish_reason': 'stop'
                }
            ],
            'usage': {
                'prompt_tokens': -1,
                'completion_tokens': -1,
                'total_tokens': -2
            }
        }

        self._set_response()
        self.wfile.write(json.dumps(response).encode("utf-8"))  # Send response


def main():
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    server_address = ("", port)
    httpd = HTTPServer(server_address, TestHTTPHandler)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()