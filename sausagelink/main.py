from copy import deepcopy
from hashlib import sha256
from datetime import datetime
from collections import UserList

BREAK = [method for method in dir([]) if not method.startswith('__')]
BREAK.remove('append')

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

class Link(UserList):
    '''A linked container for Sausages'''
    def __init__(self, nub=None):
        if isinstance(nub, Sausage):
            self.data = [nub]
        elif not nub:
            self.data = [Sausage()]
        else:
            self.data = [Sausage(nub)]

    # https://stackoverflow.com/a/5827284/3731467
    def __getattribute__(self, attr):
        if attr in BREAK:
            raise AttributeError(attr)
        else:
            return super().__getattribute__(attr)

    def __dir__(self):
        return ['append', 'data']

    def append(self, item):
        '''Stuff (arbitrary) data into a Sausage and add it to the Link'''
        last_sausage = self[-1]
        sausage = Sausage(
            data=item,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)

#     #TODO: change the name
#     def inspect(self):
#         bad = []
#         for i in range(len(self)-1):
#             if not self[i].sizzle == self[i].grill() == self[i+1].previous_sizzle:
#                 bad.append(f'Link cut between {self[i]} and {self[i+1]}')
#         if not bad:
#             return ['🌭']
#         else:
#             return bad
#
#     # not sold on this
#     def to_sl(sl, path):
#         '''Write object to a pickle (sl) file'''
#         with open(path, 'wb') as f:
#             pickle.dump(sl, f)
#         return path
# #
# # def read_sl(path):
# #     # like pandas.read_csv
# #     with open(path, 'rb') as f:
# #         sl = pickle.load(f)
# #     return sl
