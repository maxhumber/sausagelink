from copy import deepcopy
from hashlib import sha256
from datetime import datetime

class Sausage:
    '''A block of data'''
    def __init__(self, data=None, index=0, previous_sizzle=None):
        self.data = deepcopy(data)
        self.index = index
        self.previous_sizzle = previous_sizzle
        self.timestamp = datetime.now()
        # A sizzle is what you get after you grill a sausage
        self.sizzle = self.grill()

    def grill(self):
        '''Leverage the sha256 algorithm to hash the data block'''
        sha = sha256()
        sha.update((
            str(self.data) +
            str(self.index) +
            str(self.previous_sizzle) +
            str(self.timestamp)
        ).encode('utf-8'))
        # hexdigest will allow comparisons to the saved sizzle
        return sha.hexdigest()

    def rancid(self):
        '''Checks to see if the hash is the same'''
        if self.grill() != self.sizzle:
            # if the Sausage has been tampered with return True
            return True
        else:
            return False

    def __repr__(self):
        return f'⎨{self.index}⎬'

class Link(list):
    '''A container that extends the list type'''
    def __init__(self, nub=None):
        if not nub:
            super().append(Sausage())
        else:
            super().append(nub)

    def append(self, data):
        '''Append data to a Link using a Sausage block'''
        last_sausage = self[-1]
        sausage = Sausage(
            data=data,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)
