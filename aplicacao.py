import requests

# Google OpenID Connect configuration
client_id = "923868102690-4m4fgdqh0g4g5l48bo8i5esatgch0goa.apps.googleusercontent.com"
redirect_uri = "http://localhost:8000/callback"
#api google
scope = "openid email profile"

# URL for initiating Google OAuth 2.0 flow
auth_url = "https://accounts.google.com/o/oauth2/auth"

# Constructing the URL for redirection with extended scopes
extended_scope = " ".join([scope, "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"])
redirect_url = f"{auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={extended_scope}"

print("Please go to the following URL and login:")
print(redirect_url)

# Server will handle the callback and receive the code
