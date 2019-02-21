from copy import deepcopy
from hashlib import sha256
from datetime import datetime

class Sausage:
    def __init__(self, data=None, index=0, previous_sizzle=None):
        self.data = deepcopy(data)
        self.index = index
        self.previous_sizzle = previous_sizzle
        self.timestamp = datetime.now()
        self.sizzle = self.grill()

    def grill(self):
        sha = sha256()
        sha.update((
            str(self.data) +
            str(self.index) +
            str(self.previous_sizzle) +
            str(self.timestamp)
        ).encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return f'⎨{self.index}⎬'

class Link(list):
    def __init__(self, nub=None):
        if not nub:
            super().append(Sausage())
        else:
            super().append(nub)

    def append(self, data):
        last_sausage = self[-1]
        sausage = Sausage(
            data=data,
            index=last_sausage.index + 1,
            previous_sizzle=last_sausage.sizzle
        )
        return super().append(sausage)
