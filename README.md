<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/sausagelink/master/images/logo.png" width="704px" height="116px" alt="sausagelink">
</h3>

<p align="center">
  <a href="https://pypi.python.org/pypi/sausagelink"><img src="https://badge.fury.io/py/sausagelink.svg"></a>
  <a href="https://travis-ci.org/maxhumber/sausagelink"><img src="https://img.shields.io/travis/maxhumber/sausagelink.svg"></a>
  <a href="http://unlicense.org/"><img src="https://img.shields.io/pypi/l/sausagelink.svg"></a>
  <a href="https://pypi.python.org/pypi/sausagelink"><img src="https://img.shields.io/pypi/pyversions/sausagelink.svg"></a>
</p>

### About

sausagelink is like Blockchain, but tastier. The package allows you to maintain a `Link` (chain) of `Sausage` (blocks) such that the data contained within each `Sausage` and the order of the `Link` cannot be tampered with.

### <sub>sa</sub>Usage is simple

```
from sausagelink import Sausage, Link
link = Link()
# link = Link(Sausage())
link.append({'foo': 'bar'})
print(link)
# [⎨0⎬, ⎨1⎬]
print(link[0].data)
# None
print(link[1].data)
# {'foo': 'bar'}
link[0].sizzle == link[1].previous_sizzle
# True
sausage = link[-1]
print(sausage.rancid())
# False
sausage.data = {'foo': 'baz'}
print(sausage.rancid())
# True
```

### Install

`pip install sausagelink`
