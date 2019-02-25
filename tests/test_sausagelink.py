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

def test_nub():
    # nub is not a Sausage
    nub = 'non-sausage'
    link = Link(nub)
    assert isinstance(link[0], Sausage)
    assert isinstance(link[0].data, str)
    # nub is a Sausage
    nub = Sausage('sausage')
    link = Link(nub)
    assert isinstance(link[0], Sausage)
    assert isinstance(link[0].data, str)
    # no nub
    link = Link()
    assert isinstance(link[0], Sausage)
    assert link[0].data is None

def test_dir():
    link = Link()
    link.append({'foo': 'bar'})
    link.append({'bar': 'baz'})
    assert dir(link) == ['append']

def test_broken_list_methods():
    link = Link()
    with pytest.raises(AttributeError):
        link.pop()
#
# import pickle
#
# sausage = Sausage({'foo': 'bar'})
# sausage.data
#
# with open('foo.sl', 'wb') as f:
#     pickle.dump(sausage, f)
#
# del sausage
#
# with open('foo.sl', 'rb') as f:
#     sausage = pickle.load(f)
#
# sausage
# sausage.rancid()
#
#
# ###
#
# import pickle
#
# link = Link()
# link.append({'foo': 'bar'})
# link.append({'bar': 'baz'})
# [sausage.data for sausage in link]
#
# with open('foo.sl', 'wb') as f:
#     pickle.dump(link, f)
#
# del link
#
# with open('foo.sl', 'rb') as f:
#     link = pickle.load(f)
#
# link
#
# dir(link)
#
# # ['__class__',
# #  '__dict__',
# #  '__dir__',
# #  '__doc__',
# #  '__getattribute__',
# #  '__getitem__',
# #  '__init__',
# #  '__iter__',
# #  '__len__',
# #  '__repr__',
# #  '__setattr__',
# #  '__setitem__',
# #  '__sizeof__',
# #  '__str__',
# #  'append']




#
