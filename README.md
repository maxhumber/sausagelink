<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/sausagelink/master/images/logo.png" width="704px" height="116px" alt="sausagelink">
</h3>
<p align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/sausagelink.svg">
  <img alt="Travis" src="https://img.shields.io/travis/maxhumber/sausagelink.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/sausagelink.svg">
  <img alt="Downloads" src="https://img.shields.io/pypi/dw/sausagelink.svg">
</p>


### About

sausagelink is like Blockchain, but tastier. The package allows you to maintain a `Link` (chain) of `Sausage` (blocks) such that the data contained within each `Sausage` and the order of the `Link` cannot be tampered with.

### Usage

```python
from sausagelink import Sausage, Link

link = Link()
link.append('Hello, World!')
link.append(2019)
link.append({'foo': 'bar'})

print(link)
# [⎨0⎬, ⎨1⎬, ⎨2⎬, ⎨3⎬]

print([sausage.data for sausage in link])
# [None, 'Hello, World!', 2019, {'foo': 'bar'}]

link.refrigerate('foo.sl')
del link
link = Link('foo.sl')

print([sausage.data for sausage in link])
# [None, 'Hello, World!', 2019, {'foo': 'bar'}]
```

### Audit

```python
print(link.rancid())
# []

sausage = link[2]
print(sausage.data)
# 2019
print(sausage.rancid())
# False

sausage.data = 2020
print(sausage.rancid())
# True

print(link.rancid())
# ['⎨2⎬']
```

### Install

`pip install sausagelink`
