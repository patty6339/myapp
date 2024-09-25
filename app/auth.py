from flask import Flask
from flask_oidc import OpenIDConnect

oidc = OpenIDConnect()

def init_oidc(app):
    app.config.update({
        'SECRET_KEY': 'Your_Secret_Key',
        'OIDC_CLIENT_SECRETS': 'client_secrets.json',
        'OIDC_RESOURCE_CHECK_AUD': True,
        'OIDC_SCOPES': ['openid', 'email', 'profile'],
        'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
    })
    oidc.init_app(app)
