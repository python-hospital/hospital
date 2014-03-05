# -*- coding: utf-8 -*-
"""WSGI utilities to collect and run healthchecks as web service.

.. warning::

   Implementation is not mature, i.e. this part of hospital API may change
   in future releases. That said, it does the job ;)

"""
import os
from wsgiref.simple_server import make_server

from hospital.cli import base_parser
from hospital.wsgi import HealthCheckApp


def wsgi_parser(program=None):
    parser = base_parser(program)
    parser.add_argument(
        '--port',
        action='store',
        nargs='?',
        type=int,
        default='1515',
        help="Port for webserver.",
    )
    return parser


def main(program=None, args=None):
    parser = wsgi_parser(program)
    arguments = parser.parse_args(args)
    healthchecks = arguments.healthchecks
    if not healthchecks:
        healthchecks = [os.path.abspath(os.getcwd())]
    app = HealthCheckApp(discover=healthchecks)
    httpd = make_server('', arguments.port, app)
    server_address = httpd.socket.getsockname()
    print("Serving on {ip} port {port}...".format(
        ip=server_address[0],
        port=server_address[1]))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
