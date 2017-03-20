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

start = time.time()
foo = dir.get('/test/foo')
end = time.time()
print('/test/foo = %s (%.3f ms)' % (foo, round(end - start, 3)))

start = time.time()
dir.set('/test/foo', 'bar')
end = time.time()
print('Setting to "bar" (%.3f ms)' % round(end - start, 3))

start = time.time()
foo = dir.get('/test/foo')
end = time.time()
print('/test/foo = %s (%.3f ms)' % (foo, round(end - start, 3)))

sys.stdout.write('Waiting for /test/foo... ')
sys.stdout.flush()
try:
    print(dir.wait('/test/foo', 10000))
except bhdir.TimeoutException:
    print('timeout')

print('Deleting')
dir.unset('/test/foo')
```
