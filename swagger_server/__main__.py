#!/usr/bin/env python3

import connexion
from OpenSSL import SSL

from swagger_server import encoder


def main():
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file('/etc/letsencrypt/live/pollination.live/pollinaiton.live.key')
    context.use_certificate_file('/etc/letsencrypt/live/pollination.live/pollination.live.crt')
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Pollination Web Server'}, pythonic_params=True)
    app.run(port=8443, ssl_context=context)
    # app.run(port=8443)


if __name__ == '__main__':
    main()
