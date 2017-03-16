# bhdir-lib-python3

```python
#!/usr/bin/env python3

#
# git clone https://github.com/breedhub/bhdir-lib-python3 bhdir
#

import bhdir

dir = bhdir.Directory()

dir.set('/test/foo', 'bar')
print(dir.get('/test/foo'))

print('Waiting for /test/foo...')
dir.wait('/test/foo')
print('Got /test/foo event')
```
