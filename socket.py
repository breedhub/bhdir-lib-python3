import os
import socket

class Socket:
    def __init__(self, path=None):
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if path is None:
            self._path = '/var/run/bhdir/daemon.sock'
        else:
            self._path = path
        self._connected = False

    def connect(self):
        if self._connected:
            return

        if not os.path.exists(self._path):
            raise RuntimeError('Daemon is not listening to socket')

        self._sock.connect(self._path)
        self._connected = True

    def disconnect(self):
        if not self._connected:
            return

        self._sock.close()
        self._connected = False

    def send(self, msg, leave_open=True):
        self.connect()

        buff = str.encode(msg)
        length = len(buff).to_bytes(4, byteorder='big', signed=False)
        sent = self._sock.send(length)
        if sent != 4:
            raise RuntimeError("Socket terminated")
        sent = self._sock.send(buff)
        if sent != len(buff):
            raise RuntimeError("Socket terminated")

        if not leave_open:
            self.disconnect()

    def receive(self, leave_open=True):
        self.connect()

        chunk = self._sock.recv(4)
        if chunk == b'':
            raise RuntimeError("socket terminated")
        length = int.from_bytes(chunk, byteorder='big', signed=False)

        chunks = []
        bytes_recd = 0
        while bytes_recd < length:
            chunk = self._sock.recv(min(length - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket terminated")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)

        if not leave_open:
            self.disconnect()

        return b''.join(chunks).decode('utf-8')
