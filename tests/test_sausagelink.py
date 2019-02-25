import pytest

from sausagelink import Sausage, Link
# from sausagelink import to_sl, read_sl

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

def test_broken_list_pop():
    link = Link()
    with pytest.raises(AttributeError):
        link.pop()

def test_broken_list_copy():
    link = Link()
    with pytest.raises(AttributeError):
        link.copy()
#
# def test_to_and_read_sl():
#     link = Link()
#     link.append({'foo': 'bar'})
#     link.append({'bar': 'baz'})
#     to_sl(link, 'foo.sl')
#     del link
#     link = read_sl('foo.sl')

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
# #
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
