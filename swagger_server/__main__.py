#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Pollination Web Server'}, pythonic_params=True, base_path="/")
    app.run(port=8443)


if __name__ == '__main__':
    main()
