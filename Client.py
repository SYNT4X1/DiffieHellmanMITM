import socket
from random import randint

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

base = 1000
print("Using base:", base)
secret = randint(999, 9999)
print("Client secret:", secret)

try:

    # Send data
    message = bytes(str(base * secret), 'ascii')
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('received {!r}'.format(data))
        print("Common secret:", int(data) * secret)

finally:
    print('closing socket')
    sock.close()
