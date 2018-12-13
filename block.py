import utils
import crypto

n_byte = 16
MAX_BLOCK_ENTRIES = 2500
MINER_REWARD = 10
MINER_REWARD_PAYER = b'\x00' * n_byte
NUM_LEADING_ZERO_BYTES = 2


class Block:
    def __init__(self, prev_block, name, pk):
        if not isinstance(prev_block, Block):
            raise TypeError("'prev_block' is Not a Valid Block.")

        self.prev_hash = prev_block.hash
        prev_block.nxt_block = self

        self.entries = []

        self.prev_block = prev_block
        self.nxt_block = None

        init_entry = (MINER_REWARD_PAYER, name, MINER_REWARD, utils.get_timestamp())
        signature = crypto.sign_entry(init_entry, pk)
        self.add_entry(init_entry, signature)


    def build_merkle_tree(self):
	L = len(self.entries) # Number of leave
	N = 2 * L - 1 # Number of nodes
        self.merkle_tree = [None] * (N + 1)
		
	for i in range(L):
	    self.merkle_tree[i-L] = crypto.dhash(bytes(self.entries[i]))

	for i in reversed(range(1,N-L)):
	    self.merkle_tree[i] = crypto.dhash(self.merkle_tree[2*i] ^ self.merkle_tree[2*i+1])

	self.merkle_root = self.merkle_tree[1] 

    def proof_of_work(self):
        self.nounce = 0
        while(1):
            hash = crypto.dhash(bytes(self))
            if hash[:NUM_LEADING_ZERO_BYTES] == b'\x00' * NUM_LEADING_ZERO_BYTES:
                self.hash = hash
                break
            self.nounce += 1

    def add_entry(self, payer, payee, amount, timestamp, signature):
        if len(self.entries) >= MAX_BLOCK_ENTRIES:
            raise ValueError('Block Entries Exceed Maximum Length.')

        entry = (payer, payee, amount, timestamp)
        payer_pk = lookup_pk(payer)

        if payer_pk is None or lookup_pk(payee):
            raise ValueError('Payer or Payee Not exists.')

        if not verify_signature(entry, signature, payer_pk):
            raise ValueError('Not Signed by Actural Payer')

        if check_balance(name) <= amount:
            raise ValueError('Not Enough Balance')

        self.entries.append((entry, signature))

    def check_block_balance(self, name):
        balance = 0.

        for entry, signature in self.entries:
            payer, payee, amount, timestamp = entry
            if name == payer:
                balance -= amount
            elif name == payee:
                balance += amount
        return balance

    def __len__(self):
        return len(self.entries)

    def __bytes__(self):
        if self.prev_hash is None or self.nounce is None:
            raise TypeError("prev_hash' or 'nounce' Cannot be None")
        return bytes((self.prev_hash, self.entries, self.nounce))

    def __str__(self):
        return self.hash
