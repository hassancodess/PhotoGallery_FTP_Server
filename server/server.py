import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# This must be greater than 1023 unless you run this script as root.
FTP_PORT = 21

# The name of the FTP user that can log in.
FTP_USER = "abc"

# The FTP user's password.
FTP_PASSWORD = "123"

# The directory the FTP user will have full read/write access to.
FTP_DIRECTORY = os.getcwd()


def main():
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions.
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftp ready."

    # Optionally specify range of ports to use for passive connections.
    # handler.passive_ports = range(60000, 65535)

    address = ('', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()


# # Define the FTP server parameters
# FTP_HOST = '127.0.0.1'
# FTP_PORT = 21
# FTP_USER = 'user'
# FTP_PASSWORD = 'password'
# FTP_DIRECTORY = '../../Development/'

# # Create a dummy authorizer for managing 'virtual' users
# authorizer = DummyAuthorizer()
# authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmwMT')

# # Instantiate FTP handler class
# handler = FTPHandler
# handler.authorizer = authorizer

# # Start the FTP server
# with FTPServer((FTP_HOST, FTP_PORT), handler) as ftp_server:
#     print(f'Started FTP server on {FTP_HOST}:{FTP_PORT}')
#     ftp_server.serve_forever()
