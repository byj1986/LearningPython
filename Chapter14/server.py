import socket

s = socket.socket()

host = socket.gethostname()
print(host)
port = 1234
s.bind((host, port))
s.listen(5)

while True:
    c, address = s.accept()
    print('Got connection form', address)
    c.send('Thank you for connecting')
    c.close()
