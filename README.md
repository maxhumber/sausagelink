# sausagelink

## About

sausagelink is a like Blockchain, but tastier. The package allows you to maintain a Link (chain) of Sausages (blocks) such that the data contained within each Sausage cannot be tampered with.

## Usage is simple

```
>>> from sausagelink import Sausage, Link
>>> link = Link(Sausage())
>>> link.append('sausagelink is the best!')
>>> print(link)
[⎨0⎬, ⎨1⎬]
>>> print(link[1].data)
sausagelink is the best!
>>> sausage = link[-1]
>>> print(sausage.rancid())
False
>>> sausage.data = 'sausagelink is the worst!'
>>> print(sausage.rancid())
True
```

## Install

`pip install sausagelink`
