import time

MAX_BLOCK_ENTRIES = 2500


class Block:
    def __init__(self, prev_block):
        self.prev_block = prev_block
        self.nxt_block = None

        self.creator = None
        self.block_signature = None

        self.entries = []

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
            if name == payee:
                balance += amount
        return balance


def get_blockchain_length(block):
    len = 0

    while isinstance(block, Block):
        block = block.prev_block
        len += 1
    return len
    


def verify_signature(text, signature, pk):
    pass


def lookup_pk(name):
    pass
