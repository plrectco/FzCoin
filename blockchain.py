
class Blockchain:
    def __init__(self, block):
        self.block = block

    def check_balance(self, name):
        if lookup_pk(name) is None:
            raise ValueError('Name %s Not exists.' % name)

        balance = 0.
        block = self.block

        while isinstance(block, Block):
            balance += block.check_block_balance(name)
            block = block.prev_block

        return balance

    def __len__(self):
        block = self.block

        while isinstance(block, Block):
            block = block.prev_block
            len += 1
        return len
