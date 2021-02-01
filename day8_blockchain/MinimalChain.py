#ref: https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
#ref: https://github.com/edenau/minimal-blockchain/blob/master/main.ipynb

import copy # fork a chain
import datetime # get real time for timestamps
import hashlib # hash

class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()

    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()

class MinimalChain():
    def __init__(self): # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return MinimalBlock(0,
                            datetime.datetime.utcnow(),
                            'Genesis',
                            'arbitrary')

    def add_block(self, data):
        self.blocks.append(MinimalBlock(len(self.blocks),
                                        datetime.datetime.utcnow(),
                                        data,
                                        self.blocks[len(self.blocks)-1].hash))

    def get_chain_size(self): # exclude genesis block
        return len(self.blocks)-1

    def verify(self, verbose=True):
        flag = True
        for i in range(1,len(self.blocks)):
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i}.')
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous hash at block {i}.')
            if self.blocks[i].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i}.')
            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i}.')
        return flag

    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self) # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head+1]
            return c

c = MinimalChain() # Start a chain
for i in range(1,20+1):
    c.add_block(f'This is block {i} of my first chain.')

print(c.blocks[3].timestamp)
print(c.blocks[7].data)
print(c.blocks[9].hash)
