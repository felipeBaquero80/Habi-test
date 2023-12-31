import http.server
import socketserver
from filters import Filter_manage as Filtros
import json


class ManageApi(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle incoming GET requests.

        Returns:
            str: A personalized greeting message.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hola, esta es mi API en Python sin framework.')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Ruta no encontrada.')

    def do_POST(self):
        """
        Handle incoming POST requests.

        Returns:
            str: A response based on the request.
        """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        # json format 
        try:

            parametros = json.loads(body)
            filter_city = parametros.get('filter_city', '')
            filter_address = parametros.get('filter_address', '')
            filter_year = parametros.get('filter_year', '')

            if self.path == '/filtros':
                result = Filtros().consult_db(filter_city, filter_address, filter_year)
                self.send_response_method(result)

            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Ruta no encontrada.')
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Solicitud JSON invalida.')

    def send_response_method(self, result):
        """
        Send an HTTP response based on the result.

        Args:
            result (Json): The response data.

        Returns:
            str: An HTTP response with the given result.
        """
        print(result)
        if len(result) == 2:
            self.send_response(204)
        else:
            self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))


# port config
port = 8080
with socketserver.TCPServer(("", port), ManageApi) as httpd:
    print(f"Servidor en el puerto {port}")
    httpd.serve_forever()
