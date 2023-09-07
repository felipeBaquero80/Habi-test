import http.server
import socketserver
import urllib.parse
from filters import Filter_manage as filtros
import json

class ManageApi(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
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
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        # json format 
        try:

            parametros = json.loads(body)
            filter_city = parametros.get('filter_city', '')
            filter_address = parametros.get('filter_address', '')
            filter_year = parametros.get('filter_year', '')


            if self.path == '/filtros':
                result = filtros().consult_db(filter_city, filter_address, filter_year)
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



    def send_response_method(self,result):
        print(len(result), result)
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