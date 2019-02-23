![](https://raw.githubusercontent.com/maxhumber/sausagelink/master/images/logo.png)

## About

sausagelink is like Blockchain, but tastier. The package allows you to maintain a `Link` (chain) of `Sausage` (blocks) such that the data contained within each `Sausage` cannot be tampered with.

## (sa)usage is simple ☉ ‿ ⚆

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

## Install

`pip install sausagelink`
