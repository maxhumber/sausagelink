import os
import pytest
from sausagelink import Sausage, Link

@pytest.fixture
def hot_dog():
    sausage = Sausage({'type': 'hot dog', 'origin': 'USA'})
    return sausage

@pytest.fixture
def link_of_sausages():
    link = Link({'hot dog': 0, 'gyurma': 0, 'merguez': 0})
    link.append({'hot dog': 1, 'gyurma': 0, 'merguez': 0})
    link.append({'hot dog': 2, 'gyurma': 0, 'merguez': 0})
    link.append({'hot dog': 2, 'gyurma': 1, 'merguez': 0})
    link.append({'hot dog': 2, 'gyurma': 1, 'merguez': 1})
    return link

def test_hot_dog(hot_dog):
    assert isinstance(hot_dog, Sausage)
    assert hot_dog.grill() == hot_dog.sizzle

def test_rancid(hot_dog):
    hot_dog.data = {'type': 'hot dog', 'origin': 'Canada'}
    assert hot_dog.rancid()

def test_nub_no_data():
    link = Link()
    assert isinstance(link[0], Sausage)
    assert link[0].data is None

def test_nub_data_not_sausage():
    link = Link('non-sausage')
    assert isinstance(link[0], Sausage)
    assert isinstance(link[0].data, str)

def test_nub_sausage():
    link = Link(Sausage('sausage'))
    assert isinstance(link[0], Sausage)
    assert isinstance(link[0].data, str)

def test_link_of_sausages(link_of_sausages):
    assert isinstance(link_of_sausages, Link)
    assert len(link_of_sausages) == 5

def test_refrigerate(link_of_sausages):
    path = 'food.sl'
    link_of_sausages.refrigerate(path)
    del link_of_sausages
    link_of_sausages = Link(path)
    assert isinstance(link_of_sausages, Link)
    os.remove(path)

def test_broken_pop(link_of_sausages):
    with pytest.raises(AttributeError):
        link_of_sausages.pop()

def test_link_dir(link_of_sausages):
    assert dir(link_of_sausages) == ['append', 'rancid', 'refrigerate']

def test_link_middle_rancid(link_of_sausages):
    assert not link_of_sausages.rancid()
    link_of_sausages[2].data = {'hot dog': 99, 'gyurma': 0, 'saucisson': 0}
    assert link_of_sausages.rancid() == [link_of_sausages[2]]

def test_link_end_rancid(link_of_sausages):
    assert not link_of_sausages.rancid()
    link_of_sausages[-1].data = 'bad'
    assert link_of_sausages.rancid() == [link_of_sausages[4]]
