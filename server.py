from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import requests
import json

client_id = "923868102690-4m4fgdqh0g4g5l48bo8i5esatgch0goa.apps.googleusercontent.com"
client_secret = "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"
redirect_uri = "http://localhost:8000/callback"
token_url = "https://oauth2.googleapis.com/token"
userinfo_url = "https://openidconnect.googleapis.com/v1/userinfo"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        code = query_components["code"][0]

        payload = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code"
        }
        token_response = requests.post(token_url, data=payload)
        token_data = token_response.json()
        access_token = token_data["access_token"]

        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_response = requests.get(userinfo_url, headers=headers)
        userinfo_data = userinfo_response.json()

        # Retorna todas as informações do usuário
        user_info_json = json.dumps(userinfo_data, indent=4)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(user_info_json.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"O servidor está rodando na porta {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
