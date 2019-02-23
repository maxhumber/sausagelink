from copy import deepcopy
from hashlib import sha256
from datetime import datetime

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
        else:
            # create an empty Sausage to start the Link
            super().append(Sausage())

    def __getattribute__(self, attr):
        # hide everything that isn't self.append()
        if attr not in ['append']:
            raise AttributeError(attr)
        return super().__getattribute__(attr)

    def append(self, data):
        '''Stuff (arbitrary) data into a Sausage and add it to the Link'''
        last_sausage = self[-1]
        sausage = Sausage(
            data=data,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)
