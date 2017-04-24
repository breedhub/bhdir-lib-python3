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
dir.cd('/foo')

print("Set: %s" % dir.set('bar', 'test'))
print("Get: %s" % dir.get('bar'))

print("Set attr: %s" % dir.set_attr('bar', 'custom', 123))
print("Get attr: %d" % dir.get_attr('bar', 'custom'))

# get all: dir.get_attr('bar')
# delete: dir.delete_attr('bar', 'custom')

print("LS: %s" % dir.ls('/foo'))
print("Exists: %s" % dir.exists('/foo'))

with open('/etc/shells', 'rb') as fd:
    print("Upload by fd: %s" % dir.put_fd(fd, 'bar'))

print("Upload by path: %s" % dir.put_file('/etc/shells', 'bar'))

# get descriptor
fd = dir.get_fd('bar')
fd.close()

# get file
dir.get_file('bar', '/tmp/test')

# dir.wait('bar')
# dir.touch('bar')

# dir.del_attr('bar', 'custom')
# dir.delete('bar')
# dir.rm('bar')
```
