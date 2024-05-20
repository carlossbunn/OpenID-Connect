from flask import Flask, request, redirect, session
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # You should use a more secure and random key in production

# Google OAuth configuration
client_id = "-"
client_secret = "-"
default_redirect_uri = "http://localhost:8000/callback"
scope = "openid email profile"
token_url = "https://oauth2.googleapis.com/token"
auth_url = "https://accounts.google.com/o/oauth2/auth"

@app.route("/login")
def login():
    try:
        redirect_uri = request.args.get('redirect_uri', default_redirect_uri)
        session['redirect_uri'] = redirect_uri
        redirect_url = f"{auth_url}?client_id={client_id}&redirect_uri={default_redirect_uri}&response_type=code&scope={scope}"
        print(f"Redirecting to Google OAuth URL: {redirect_url}")  # Debug log
        return redirect(redirect_url)
    except Exception as e:
        print(f"Error in login route: {e}")  # Debug log
        return f"Internal Server Error in login: {e}", 500

@app.route("/callback")
def callback():
    try:
        code = request.args.get("code")
        if not code:
            print("Missing authorization code")  # Debug log
            return "Missing authorization code", 400

        print(f"Authorization code received: {code}")  # Debug log

        # Exchange the authorization code for an access token
        token_data = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": default_redirect_uri,
            "grant_type": "authorization_code"
        }

        try:
            token_response = requests.post(token_url, data=token_data)
            token_response.raise_for_status()
            token_info = token_response.json()
            access_token = token_info['access_token']
            redirect_uri = session.get('redirect_uri', 'http://localhost:8001/callback')
            print(f"Access token received: {access_token}")  # Debug log
            return redirect(f"{redirect_uri}?access_token={access_token}")
        except requests.RequestException as e:
            print(f"Error obtaining token: {e}")  # Debug log
            return f"Error obtaining token: {e}", 400
    except Exception as e:
        print(f"Error in callback route: {e}")  # Debug log
        return f"Internal Server Error in callback: {e}", 500

if __name__ == "__main__":
    app.run(port=8000)
