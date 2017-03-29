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

print("Set: %s" % dir.set('/foo/bar', 'test'))
print("Get: %s" % dir.get('/foo/bar'))

print("Set attr: %s" % dir.set_attr('/foo/bar', 'custom', 123))
print("Get attr: %d" % dir.get_attr('/foo/bar', 'custom'))

# get all: dir.get_attr('/foo/bar')

print("LS: %s" % dir.ls('/foo'))

with open('/etc/shells', 'rb') as fd:
    print("Upload: %s" % dir.upload('/foo/bar', fd))

with open('/tmp/test', 'wb') as fd:
    dir.download('/foo/bar', fd)

# dir.del_attr('/foo/bar', 'custom')
# dir.delete('/foo/bar')
# dir.rm('/foo/bar')
```
