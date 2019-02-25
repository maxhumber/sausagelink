from copy import deepcopy
from datetime import datetime
from hashlib import sha256
from collections import UserList
import pickle

BREAK = [method for method in dir([]) if not method.startswith('__')]
BREAK.remove('append')

class Sausage:
    '''A 'tamper-proof' container for data'''
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

class Link(UserList):
    '''A linked container for Sausages'''
    def __init__(self, nub_or_path=None):
        if isinstance(nub_or_path, str) and nub_or_path.endswith('.sl'):
            with open(nub_or_path, 'rb') as f:
                self.data = pickle.load(f).data
        elif isinstance(nub_or_path, Sausage):
            self.data = [nub_or_path]
        elif not nub_or_path:
            self.data = [Sausage()]
        else:
            self.data = [Sausage(nub_or_path)]

    # https://stackoverflow.com/a/5827284/3731467
    def __getattribute__(self, attr):
        if attr in BREAK:
            raise AttributeError(attr)
        else:
            return super().__getattribute__(attr)

    # expose only these methods to the user
    def __dir__(self):
        return ['append', 'rancid', 'refrigerate']

    def append(self, data):
        '''Stuff (arbitrary) data into a Sausage and add it to the Link'''
        last_sausage = self[-1]
        sausage = Sausage(
            data=data,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)

    # TODO: rename to something better
    def rancid(self):
        bad = []
        for i in range(len(self)-1):
            if not self[i].sizzle == self[i].grill() == self[i+1].previous_sizzle:
                bad.append(f'{self[i]}')
        return bad

    def refrigerate(self, path):
        '''Perserve the Link for later consumption'''
        if not path.endswith('.sl'):
            path += '.sl'
        with open(path, 'wb') as f:
            pickle.dump(self, f)
        return path
