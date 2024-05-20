from flask import Flask, request, redirect, url_for, session as flask_session
import requests
from requests.exceptions import RequestException

# Keycloak login details
keycloak_url = "http://localhost:8080"
username = '-'
password = '-'

# Google OAuth configuration
login_service_url = "http://localhost:8000"
redirect_uri = "http://localhost:8001/callback"

# Prepare for Flask app
app = Flask(__name__)
app.secret_key = '-'  # This key should be more secure in production
requests_session = requests.Session()


@app.route("/")
def index():
    if not keycloak_login():
        return "Keycloak login failed", 401

    # Redirect to the OIDC login service
    redirect_url = f"{login_service_url}/login?redirect_uri={redirect_uri}"
    print(f"Redirect URL: {redirect_url}")  # Debug log
    return redirect(redirect_url)


# Function to login to Keycloak
def keycloak_login():
    login_data = {
        'client_id': 'admin-cli',  # Common client ID used in Keycloak for administrative tasks
        'username': username,
        'password': password,
        'grant_type': 'password'
    }
    try:
        login_response = requests_session.post(keycloak_url, data=login_data)
        if login_response.ok:
            print("Successfully logged into Keycloak")
        else:
            print(f"Login failed: {login_response.text}")
        return login_response.ok
    except RequestException as e:
        print(f"Error during Keycloak login: {e}")
        return False



@app.route("/callback")
def callback():
    try:
        access_token = request.args.get("access_token")
        if not access_token:
            print("Missing access token")  # Debug log
            return "Missing access token", 400

        flask_session['access_token'] = access_token
        print(f"Access token received: {access_token}")  # Debug log
        return redirect(url_for('OidcToken'))
    except Exception as e:
        print(f"Error in callback route: {e}")  # Debug log
        return f"Internal Server Error in callback: {e}", 500

@app.route("/OidcToken")
def OidcToken():
    try:
        access_token = flask_session.get('access_token')
        if not access_token:
            print("No access token in session, redirecting to login")  # Debug log
            return redirect(f"{login_service_url}/login?redirect_uri={redirect_uri}")

        # Display the access token
        return f"Sensitive resource accessed with token: {access_token}"
    except Exception as e:
        print(f"Error in OidcToken route: {e}")  # Debug log
        return f"Internal Server Error in OidcToken: {e}", 500

if __name__ == "__main__":
    app.run(port=8001)
