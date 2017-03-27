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

dir.set('/foo/bar', 'test')
print(dir.get('/foo/bar'))

dir.set_attr('/foo/bar', 'custom', 123)
print(dir.get_attr('/foo/bar', 'custom'))

# get all: dir.get_attr('/foo/bar')

print(dir.ls('/foo'))

with open('/etc/shells', 'rb') as fd:
    dir.upload('/foo/bar', fd)

with open('/tmp/test', 'wb') as fd:
    dir.download('/foo/bar', fd)

# dir.del_attr('/foo/bar', 'custom')
# dir.delete('/foo/bar')
# dir.rm('/foo/bar')
```
