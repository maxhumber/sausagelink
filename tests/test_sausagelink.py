import pytest

from sausagelink import Sausage, Link

def test_sausage():
    data = 'Hi!'
    sausage = Sausage(data)
    assert sausage.grill() == sausage.sizzle
    assert not sausage.rancid()
    sausage.data = 'Bye'
    assert sausage.grill() != sausage.sizzle
    assert sausage.rancid()

def test_link():
    link = Link()
    link.append('Yay!')
    assert len(link) == 2
    sausage = link[-1]
    assert isinstance(sausage, Sausage)
    assert link[0].sizzle == link[1].previous_sizzle
