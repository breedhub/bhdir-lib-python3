import uuid
import json
from .socket import *


class TimeoutException(Exception):
    pass

class Directory(object):
    def __init__(self, path=None):
        self._socket = Socket(path)

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

    def unset(self, name):
        request = {
            'id': str(uuid.uuid1()),
            'command': 'unset',
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
                timeout
            ]
        }

        self._socket.send(json.dumps(request))
        response = json.loads(self._socket.receive())

        if response['id'] != request['id']:
            raise RuntimeError('Invalid response from daemon')

        if not response['success']:
            raise RuntimeError('Error: %s' % response['message'])

        if response['timeout']:
            raise TimeoutException()

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
