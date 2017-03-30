import uuid
import json
import base64
from .socket import *


class TimeoutException(Exception):
    pass

class Directory(object):
    def __init__(self, path=None):
        self._socket = Socket(path)

    def ls(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'ls',
            'args': [
                name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def set(self, name, value):
        if value is None:
            raise RuntimeError('Invalid value')

        request = {
            'id': str(uuid.uuid1()),
            'command': 'set',
            'args': [
                name,
                value
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def get(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'get',
            'args': [
                name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def delete(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'del',
            'args': [
                name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

    def rm(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'rm',
            'args': [
                name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

    def wait(self, name, timeout=0):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'wait',
            'args': [
                name,
                round(timeout * 1000)
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def touch(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'touch',
            'args': [
                name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

    def set_attr(self, var_name, attr_name, value):
        if value is None:
            raise RuntimeError('Invalid value')

        request = {
            'id': str(uuid.uuid1()),
            'command': 'set-attr',
            'args': [
                var_name,
                attr_name,
                value
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def get_attr(self, var_name, attr_name=None):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'get-attr',
            'args': [
                var_name,
                attr_name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def delete_attr(self, var_name, attr_name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'del-attr',
            'args': [
                var_name,
                attr_name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

    def upload(self, var_name, fd):
        contents = fd.read()
        if isinstance(contents, str):
           raise RuntimeError('File should be opened in binary mode')

        request = {
            'id': str(uuid.uuid1()),
            'command': 'upload',
            'args': [
                var_name,
                base64.b64encode(contents).decode('ascii')
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        return response['results'][0]

    def download(self, var_name, fd):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'download',
            'args': [
                var_name
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        fd.write(base64.b64decode(response['results'][0].encode('ascii')))
