from copy import deepcopy
from hashlib import sha256
from datetime import datetime
import pickle

class Sausage:
    '''A "tamper-proof" container for data'''
    def __init__(self, data=None, index=0, previous_sizzle=None):
        self.data = deepcopy(data)
        self.index = index
        self.previous_sizzle = previous_sizzle
        self.timestamp = datetime.now()
        # A grilled sausage is called a sizzle (｡◕‿‿◕｡)
        self.sizzle = self.grill()

    def grill(self):
        '''Hash the entire object with sha256 (should match self.sizzle)'''
        sha = sha256()
        sha.update((
            str(self.data) +
            str(self.index) +
            str(self.previous_sizzle) +
            str(self.timestamp)
        ).encode('utf-8'))
        return sha.hexdigest()

    def rancid(self):
        '''Check if the result of self.grill() and self.sizzle are different.'''
        if self.grill() != self.sizzle:
            return True
        else:
            return False

    def __repr__(self):
        # looks like sausage ☉ ‿ ⚆
        return f'⎨{self.index}⎬'

class Link(list):
    '''A linked container for Sausages'''
    def __init__(self, nub=None):
        if isinstance(nub, Sausage):
            super().append(nub)
        elif not nub:
            # create an empty Sausage to start the Link
            super().append(Sausage())
        else:
            super().append(Sausage(nub))

    # https://stackoverflow.com/a/5827284/3731467
    def __getattribute__(self, attr):
        # break everything that isn't append or dunder
        if attr.startswith('__'):
            return super().__getattribute__(attr)
        elif attr in ['append']:
            return super().__getattribute__(attr)
        else:
            raise AttributeError(attr)

    def __dir__(self):
        return ['append']

    def append(self, data):
        '''Stuff (arbitrary) data into a Sausage and add it to the Link'''
        last_sausage = self[-1]
        sausage = Sausage(
            data=data,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)

def inspect(link):
    bad = []
    for i in range(len(link)-1):
        if not link[i].sizzle == link[i].grill() == link[i+1].previous_sizzle:
            bad.append(f'Link cut between {link[i]} and {link[i+1]}')
    if not bad:
        return ['🌭']
    else:
        return bad
        
#
# def to_sl(sl, path):
#     '''Write object to a pickle (sl) file'''
#     with open(path, 'wb') as f:
#         pickle.dump(sl, f)
#     return path
#
# def read_sl(path):
#     # like pandas.read_csv
#     with open(path, 'rb') as f:
#         sl = pickle.load(f)
#     return sl
