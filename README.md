# bhdir-lib-python3

```python
#!/usr/bin/env python3

#
# git clone https://github.com/breedhub/bhdir-lib-python3 bhdir
#

import time
import sys
import bhdir

dir = bhdir.Directory()

dir.use('sync')
dir.cd('/')

print("Set: %s" % dir.set('/foo/bar', 'test'))
print("Get: %s" % dir.get('/foo/bar'))

print("Set attr: %s" % dir.set_attr('/foo/bar', 'custom', 123))
print("Get attr: %d" % dir.get_attr('/foo/bar', 'custom'))

# get all: dir.get_attr('/foo/bar')
# delete: dir.delete_attr('/foo/bar', 'custom')

print("LS: %s" % dir.ls('/foo'))
print("Exists: %s" % dir.exists('/foo'))

with open('/etc/shells', 'rb') as fd:
    print("Upload by fd: %s" % dir.put_fd(fd, '/foo/bar'))

print("Upload by path: %s" % dir.put_file('/etc/shells', '/foo/bar'))

# get descriptor
fd = dir.get_fd('/foo/bar')
fd.close()

# get file
dir.get_file('/foo/bar', '/tmp/test')

# dir.wait('/foo/bar')
# dir.touch('/foo/bar')

# dir.del_attr('/foo/bar', 'custom')
# dir.delete('/foo/bar')
# dir.rm('/foo/bar')
```
