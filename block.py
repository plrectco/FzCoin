import utils
import crypto

n_byte = 16
MAX_BLOCK_ENTRIES = 2500
MINER_REWARD = 10
MINER_REWARD_PAYER = b'\x00' * n_byte
NUM_LEADING_ZERO_BYTES = 2


class Block:
    def __init__(self, prev_block, name, pk):
        self.prev_hash = None
        self.entries = []
        self.nounce = None

        self.prev_block = prev_block
        self.nxt_block = None

        init_entry = (MINER_REWARD_PAYER, name, MINER_REWARD, utils.get_timestamp())
        signature = crypto.sign_entry(init_entry, pk)
        self.add_entry(init_entry, signature)

    def __bytes__(self):
        if self.prev_hash is None or self.nounce is None:
            raise TypeError("prev_hash' or 'nounce' Cannot be None")
        return bytes((self.prev_hash, self.entries, self.nounce))

    def proof_of_work(self):
        while(1):
            self.nounce = i
            hash = crypto.dhash(bytes(self))
            if hash[:NUM_LEADING_ZERO_BYTES] == b'\x00' * NUM_LEADING_ZERO_BYTES:
                self.hash = hash
                break
            i += 1

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


def get_blockchain_length(block):
    len = 0

    while isinstance(block, Block):
        block = block.prev_block
        len += 1
    return len


def lookup_pk(name):
    pass
